#!/usr/bin/env python3
"""Pull each project's README from its (private) TootooniLab repo into _data/readmes.json.

Reads the `repo:` field from every _projects/*.md file, asks the GitHub API for that
repo's README using the token in ORG_READ_TOKEN, and stores the markdown by project id.
A repo that cannot be read keeps whatever was stored before, so one failure never
wipes a page.
"""
import glob, json, os, re, sys, urllib.request, urllib.error

ORG = os.environ.get("LAB_ORG", "TootooniLab")
TOKEN = os.environ.get("ORG_READ_TOKEN", "")
OUT = "_data/readmes.json"

try:
    data = json.load(open(OUT))
except Exception:
    data = {}

def field(text, name):
    m = re.search(r"^%s:\s*\"?([^\"\n]+?)\"?\s*$" % name, text, re.M)
    return m.group(1).strip() if m else None

def clean(md):
    md = md.replace("\r\n", "\n")
    md = md.replace("\u2014", ", ")  # site rule: no em dashes
    lines = md.split("\n")
    for i, l in enumerate(lines):          # drop the first H1, the page already has a title
        if l.startswith("# "):
            del lines[i]
            break
    return "\n".join(lines).strip() + "\n"

ok, failed = 0, []
for path in sorted(glob.glob("_projects/*.md")):
    text = open(path, encoding="utf-8").read()
    pid, repo = field(text, "pid"), field(text, "repo")
    if not pid or not repo:
        continue
    req = urllib.request.Request(
        "https://api.github.com/repos/%s/%s/readme" % (ORG, repo),
        headers={"Accept": "application/vnd.github.raw+json",
                 "Authorization": "Bearer " + TOKEN,
                 "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data[pid] = clean(r.read().decode("utf-8"))
            ok += 1
    except urllib.error.HTTPError as e:
        failed.append("%s (%s, HTTP %s)" % (pid, repo, e.code))
    except Exception as e:
        failed.append("%s (%s, %s)" % (pid, repo, e))

os.makedirs("_data", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=1, ensure_ascii=False, sort_keys=True)
    f.write("\n")

print("READMEs synced: %d" % ok)
for f_ in failed:
    print("could not read: " + f_)
if not TOKEN:
    print("ORG_READ_TOKEN is not set"); sys.exit(1)
