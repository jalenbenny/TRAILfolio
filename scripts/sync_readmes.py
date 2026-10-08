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
    return "\n".join(lines).strip() + "\n"

def via_git(repo):
    tmp = tempfile.mkdtemp()
    try:
        r = subprocess.run(["git", "clone", "--depth", "1", "-q", "%s/%s.git" % (BASE, repo), tmp + "/r"],
                           capture_output=True, text=True, env=dict(os.environ, GIT_TERMINAL_PROMPT="0"))
        if r.returncode != 0:
            raise RuntimeError(r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "clone failed")
        for name in sorted(os.listdir(tmp + "/r")):
            if name.lower() in ("readme.md", "readme.markdown", "readme.txt", "readme"):
                return open(os.path.join(tmp, "r", name), encoding="utf-8", errors="replace").read()
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
        data[pid] = clean(via_git(repo) if LOCAL else via_api(repo))
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
