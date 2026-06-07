#!/usr/bin/env python3
"""Audit every link in README.md.

- GitHub org/repo links  -> verified via `gh api` (also prints ⭐ stars + SPDX license)
- Everything else        -> HTTP status via curl

Usage:
    python3 scripts/audit.py            # audit README.md
    python3 scripts/audit.py PATH.md

Exit code is non-zero if any link is broken, so CI/pre-commit can gate on it.
The stars/license columns let a maintainer eyeball whether the 🟢/🟡/🔴 tag
still matches the project's actual declared license.
"""
import json
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

README = sys.argv[1] if len(sys.argv) > 1 else "README.md"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
# Hosts that routinely 403/429 a bot but are fine in a browser — don't fail on these.
SOFT_HOSTS = (
    "aliyun.com", "volcengine.com", "baidu.com", "tencent.com", "huaweicloud.com",
    "hiascend.com", "mindspore.cn", "cambricon.com", "mthreads.com", "hygon.cn",
    "birentech.com", "modelscope.cn", "gitee.com", "atomgit.com", "kaggle.com",
    "siliconflow.cn", "ai.gitcode.com", "groq.com",
)
OK_CODES = {200, 201, 202, 203, 204, 206, 301, 302, 307, 308}


def links(text):
    seen, out = set(), []
    for url in re.findall(r"\]\((https?://[^)\s]+)\)", text):
        url = url.rstrip("/")
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out


def gh_match(url):
    m = re.match(r"https?://github\.com/([^/]+)(?:/([^/#?]+))?$", url)
    if not m:
        return None
    return m.group(1), m.group(2)


def check_repo(owner, repo):
    try:
        data = json.loads(subprocess.run(
            ["gh", "api", f"repos/{owner}/{repo}"],
            capture_output=True, text=True, timeout=30).stdout)
        if "full_name" in data:
            lic = (data.get("license") or {}).get("spdx_id") or "NONE"
            return True, f"⭐{data.get('stargazers_count', 0):>6}  {lic}"
        return False, data.get("message", "not found")
    except Exception as e:  # noqa: BLE001
        return False, f"error: {e}"


def check_user(owner):
    try:
        out = subprocess.run(["gh", "api", f"users/{owner}"],
                             capture_output=True, text=True, timeout=30).stdout
        data = json.loads(out)
        return ("login" in data), data.get("type", data.get("message", "?"))
    except Exception as e:  # noqa: BLE001
        return False, f"error: {e}"


def check_http(url):
    try:
        code = subprocess.run(
            ["curl", "-sL", "-o", "/dev/null", "-w", "%{http_code}",
             "-A", UA, "--max-time", "25", url],
            capture_output=True, text=True, timeout=30).stdout.strip()
        code = int(code or 0)
    except Exception:  # noqa: BLE001
        code = 0
    ok = code in OK_CODES or (any(h in url for h in SOFT_HOSTS) and code in (403, 429, 503))
    return ok, f"HTTP {code}"


def audit(url):
    gh = gh_match(url)
    if gh:
        owner, repo = gh
        ok, info = check_repo(owner, repo) if repo else check_user(owner)
    else:
        ok, info = check_http(url)
    return url, ok, info


def main():
    with open(README, encoding="utf-8") as f:
        urls = links(f.read())
    print(f"Auditing {len(urls)} unique links in {README}\n")
    with ThreadPoolExecutor(max_workers=12) as ex:
        results = list(ex.map(audit, urls))
    bad = []
    for url, ok, info in sorted(results, key=lambda r: r[0]):
        mark = "OK  " if ok else "FAIL"
        if not ok:
            bad.append(url)
        print(f"{mark}  {info:<22}  {url}")
    print(f"\n{len(results) - len(bad)}/{len(results)} OK")
    if bad:
        print("\nBROKEN:")
        for u in bad:
            print("  " + u)
        sys.exit(1)
    print("All links resolve. 🎉")


if __name__ == "__main__":
    main()
