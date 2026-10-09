#!/usr/bin/env python3
"""Add lab members' papers to _bibliography/papers.bib using OpenAlex.

Google Scholar has no API and blocks scripts, so this uses OpenAlex (free, open).
Entries you wrote by hand stay above the AUTO marker and are never touched.
Everything below the marker is regenerated on each run.

Only papers co-authored by the lab's PI are kept (the "anchor" in
publication_authors.json), so members' work from before or outside the lab is left out.
Pass --all to keep every paper found for every listed person.

Usage (from the repo root):
  python3 scripts/sync_publications.py          # asks before writing
  python3 scripts/sync_publications.py --yes    # no prompt (for automation)
"""
import json, re, sys, unicodedata, urllib.parse, urllib.request

API = "https://api.openalex.org"
BIB = "_bibliography/papers.bib"
AUTHORS = "scripts/publication_authors.json"
MARK = "% ===== AUTO-GENERATED FROM OPENALEX BELOW. Edit above this line only. ====="
SKIP_TYPES = {"dataset", "paratext", "erratum", "peer-review", "editorial", "letter", "retraction"}


def get(path, **params):
    url = API + path + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "TRAILfolio-sync"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def esc(s):
    return re.sub(r"([&%#_$])", r"\\\1", s or "")


def find_author(a):
    if a.get("openalex"):
        return a["openalex"], None
    res = get("/authors", search=a["search"], **{"per-page": 10}).get("results", [])
    if not res:
        return None, []
    def score(c):
        insts = " ".join((i.get("display_name") or "") for i in (c.get("last_known_institutions") or []))
        return (("loyola" in insts.lower()), c.get("works_count", 0))
    res.sort(key=score, reverse=True)
    return res[0]["id"].rsplit("/", 1)[-1], res[:3]


def describe(c):
    insts = ", ".join((i.get("display_name") or "") for i in (c.get("last_known_institutions") or [])) or "no institution listed"
    return f'{c["display_name"]} ({c["id"].rsplit("/",1)[-1]}), {c.get("works_count",0)} works, {insts}'


def fetch_works(aid):
    out, cursor = [], "*"
    while cursor:
        d = get("/works", filter=f"author.id:{aid}", **{"per-page": 100, "cursor": cursor})
        out += d.get("results", [])
        cursor = d.get("meta", {}).get("next_cursor")
        if not d.get("results"):
            break
    return out


def bib_name(display):
    parts = display.replace(".", ". ").split()
    if len(parts) < 2:
        return display
    return f'{parts[-1]}, {" ".join(parts[:-1])}'


def to_bibtex(w, used):
    title = (w.get("title") or w.get("display_name") or "").strip()
    if not title:
        return None
    year = w.get("publication_year") or ""
    auths = [bib_name(x["author"]["display_name"]) for x in w.get("authorships", []) if x.get("author")]
    if not auths:
        return None
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or ""
    typ = w.get("type") or ""
    stype = ((w.get("primary_location") or {}).get("source") or {}).get("type") or ""
    kind = "inproceedings" if (typ == "proceedings-article" or stype == "conference") else ("article" if src else "misc")
    first = re.sub(r"[^a-z]", "", norm(auths[0].split(",")[0]).replace(" ", "")) or "paper"
    word = next((x for x in norm(title).split() if len(x) > 3), "paper")
    key = f"{first}{year}{word}"
    n, base = 1, key
    while key in used:
        n += 1
        key = f"{base}{n}"
    used.add(key)
    f = [("title", "{" + esc(title) + "}"), ("author", "{" + " and ".join(esc(a) for a in auths) + "}")]
    if src:
        f.append(("booktitle" if kind == "inproceedings" else "journal", "{" + esc(src) + "}"))
    if year:
        f.append(("year", "{%s}" % year))
    bib = w.get("biblio") or {}
    if bib.get("volume"):
        f.append(("volume", "{%s}" % bib["volume"]))
    if bib.get("issue"):
        f.append(("number", "{%s}" % bib["issue"]))
    if bib.get("first_page"):
        pg = bib["first_page"] + (("--" + bib["last_page"]) if bib.get("last_page") else "")
        f.append(("pages", "{%s}" % pg))
    doi = (w.get("doi") or "").replace("https://doi.org/", "")
    if doi:
        f.append(("doi", "{%s}" % doi))
    body = ",\n".join(f"  {k} = {v}" for k, v in f)
    return f"@{kind}{{{key},\n{body}\n}}\n"


def main():
    auto_yes = "--yes" in sys.argv
    authors = json.load(open(AUTHORS, encoding="utf-8"))
    text = open(BIB, encoding="utf-8").read()
    manual = text.split(MARK)[0].rstrip() + "\n"
    seen = {norm(m) for m in re.findall(r"(?is)title\s*=\s*\{+(.*?)\}+\s*,", manual)}
    used = set(re.findall(r"(?m)^@\w+\{([^,]+),", manual))

    works = {}
    for a in authors:
        try:
            aid, cands = find_author(a)
        except Exception as e:
            print(f"Could not reach OpenAlex for {a['name']}: {e}")
            return 1
        if not aid:
            print(f"No OpenAlex match for {a['name']}; skipping.")
            continue
        a["_id"] = aid
        print(f"\n{a['name']}: using {aid}")
        for c in cands or []:
            print("   candidate:", describe(c))
        for w in fetch_works(aid):
            works[w["id"]] = w

    anchors = [norm(a["name"]).split()[-1] for a in authors if a.get("anchor")]
    def in_lab(w):
        if "--all" in sys.argv or not anchors:
            return True
        names = [norm((x.get("author") or {}).get("display_name")) for x in w.get("authorships", [])]
        return any(n.split() and n.split()[-1] in anchors for n in names)

    kept = []
    skipped = 0
    for w in works.values():
        if (w.get("type") or "") in SKIP_TYPES:
            continue
        if not in_lab(w):
            skipped += 1
            continue
        t = norm(w.get("title") or w.get("display_name"))
        if not t or t in seen:
            continue
        seen.add(t)
        kept.append(w)
    print(f"\nLeft out {skipped} papers without the PI as an author.")
    kept.sort(key=lambda w: (w.get("publication_year") or 0), reverse=True)
    entries = [e for e in (to_bibtex(w, used) for w in kept) if e]

    print(f"\n{len(entries)} new papers beyond the {len(re.findall(r'(?m)^@', manual))} already listed by hand:")
    for w in kept[:40]:
        print(f"  {w.get('publication_year')}  {(w.get('title') or '')[:90]}")
    if not entries:
        print("Nothing to add.")
        return 0

    if not auto_yes:
        if not sys.stdin.isatty():
            print("Not interactive; rerun with --yes to write.")
            return 0
        if input("\nWrite these to papers.bib and pin these author IDs? [y/N] ").strip().lower() != "y":
            print("Skipped; papers.bib unchanged.")
            return 0

    open(BIB, "w", encoding="utf-8").write(manual + "\n" + MARK + "\n\n" + "\n".join(entries))
    for a in authors:
        if a.get("_id"):
            a["openalex"] = a.pop("_id")
    json.dump(authors, open(AUTHORS, "w", encoding="utf-8"), indent=2)
    print("papers.bib updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
