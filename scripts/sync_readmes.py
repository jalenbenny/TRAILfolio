#!/usr/bin/env python3
"""Copy each project's README from its private TootooniLab repo into _data/readmes.yml.

Reads the `repo:` field from every _projects/*.md file and stores the repo's README
text by project id.

Two ways to run it:
  python3 scripts/sync_readmes.py --local   uses git clone with YOUR GitHub login
                                            (you are a TootooniLab member, so it works)
  python3 scripts/sync_readmes.py           uses the GitHub API with ORG_READ_TOKEN
                                            (this is what the scheduled Action uses)

A repo that cannot be read keeps whatever was stored before.
"""
import glob, json, os, re, subprocess, sys, tempfile, shutil, urllib.request, urllib.error

ORG = os.environ.get("LAB_ORG", "TootooniLab")
BASE = os.environ.get("REPO_BASE", "https://github.com/%s" % ORG)
TOKEN = os.environ.get("ORG_READ_TOKEN", "")
LOCAL = "--local" in sys.argv
OUT = "_data/readmes.yml"

try:
    data = json.load(open(OUT))   # the file is JSON written in YAML-compatible form
except Exception:
    data = {}

def field(text, name):
    m = re.search(r"^%s:\s*\"?([^\"\n]+?)\"?\s*$" % name, text, re.M)
    return m.group(1).strip() if m else None

def clean(md):
    md = md.replace("\r\n", "\n").replace("\u2014", ", ")
    lines = md.split("\n")
    for i, l in enumerate(lines):          # drop the first H1, the page already has a title
        if l.startswith("# "):
            del lines[i]
            break
    # The project page already shows the one-line description, status, tags and team,
    # so drop the README's intro lines (everything before the first "## " heading)
    first = next((i for i, l in enumerate(lines) if l.startswith("## ")), None)
    if first is not None:
        lines = lines[first:]
    # drop a "## Team" section (the info panel on the page already lists the team)
    out, skip = [], False
    for l in lines:
        if l.startswith("## "):
            skip = l[3:].strip().lower() == "team"
        if not skip:
            out.append(l)
    return "\n".join(out).strip() + "\n"

IMG_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")
MAX_IMG = 5 * 1024 * 1024
IMG_DIR = "assets/img/readmes"

def is_remote(u):
    return re.match(r"^(https?:|data:|mailto:|#|//)", u) is not None

def localize(md, pid, root, readme_dir):
    """Copy images the README points to into the site and rewrite their paths.
    Relative links to other repo files are turned into plain text (they would 404)."""
    from urllib.parse import quote, unquote
    copied = []
    def grab(ref):
        ref = unquote(ref.split("#")[0].split("?")[0]).strip()
        if not ref or is_remote(ref) or not ref.lower().endswith(IMG_EXT):
            return None
        src = os.path.normpath(os.path.join(readme_dir, ref.lstrip("/")) if not ref.startswith("/") else os.path.join(root, ref.lstrip("/")))
        if not src.startswith(os.path.normpath(root)) or not os.path.isfile(src):
            print("   missing image: %s" % ref); return None
        if os.path.getsize(src) > MAX_IMG:
            print("   image too large, skipped: %s" % ref); return None
        rel = os.path.relpath(src, root).replace(os.sep, "/")
        dest = os.path.join(IMG_DIR, pid, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(src, dest)
        copied.append(rel)
        return "/" + IMG_DIR + "/" + pid + "/" + quote(rel)
    def md_img(m):
        new = grab(m.group(2))
        return m.group(0) if new is None else "![%s](%s)" % (m.group(1), new)
    md = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", md_img, md)
    def html_img(m):
        new = grab(m.group(2))
        return m.group(0) if new is None else m.group(1) + new + m.group(3)
    md = re.sub(r"(<img\b[^>]*?\bsrc=[\"'])([^\"']+)([\"'])", html_img, md, flags=re.I)
    md = re.sub(r"(?<!!)\[([^\]]+)\]\((?!https?:|mailto:|#|/%s/)([^)]+)\)" % IMG_DIR, r"\1", md)
    return md, copied

def via_git(repo, pid):
    tmp = tempfile.mkdtemp()
    try:
        r = subprocess.run(["git", "clone", "--depth", "1", "-q", "%s/%s.git" % (BASE, repo), tmp + "/r"],
                           capture_output=True, text=True, env=dict(os.environ, GIT_TERMINAL_PROMPT="0"))
        if r.returncode != 0:
            raise RuntimeError(r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "clone failed")
        root = tmp + "/r"
        for name in sorted(os.listdir(root)):
            if name.lower() in ("readme.md", "readme.markdown", "readme.txt", "readme"):
                text = open(os.path.join(root, name), encoding="utf-8", errors="replace").read()
                text, copied = localize(text, pid, root, root)
                if copied:
                    print("   copied %d image(s)" % len(copied))
                return text
        raise RuntimeError("no README in repo")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

def via_api(repo):
    req = urllib.request.Request(
        "https://api.github.com/repos/%s/%s/readme" % (ORG, repo),
        headers={"Accept": "application/vnd.github.raw+json",
                 "Authorization": "Bearer " + TOKEN,
                 "X-GitHub-Api-Version": "2022-11-28"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %s" % e.code)

if not LOCAL and not TOKEN:
    print("ORG_READ_TOKEN is not set (or run with --local)"); sys.exit(1)

ok, failed = 0, []
for path in sorted(glob.glob("_projects/*.md")):
    text = open(path, encoding="utf-8").read()
    pid, repo = field(text, "pid"), field(text, "repo")
    if not pid or not repo:
        continue
    try:
        data[pid] = clean(via_git(repo, pid) if LOCAL else via_api(repo))
        ok += 1
        print("ok      %s" % repo)
    except Exception as e:
        failed.append("%s (%s): %s" % (pid, repo, e))

os.makedirs("_data", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=1, sort_keys=True)   # ASCII-escaped JSON is valid YAML
    f.write("\n")

print("\nREADMEs synced: %d" % ok)
for x in failed:
    print("could not read: " + x)
