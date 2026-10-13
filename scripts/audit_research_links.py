#!/usr/bin/env python3
"""Audit repository Markdown links and optionally probe external URLs.

Usage:
    python scripts/audit_research_links.py
    python scripts/audit_research_links.py --external --output docs/link-audit-report.md

No third-party dependencies. Reports failures; does not edit source documents.
External checks are network-dependent and may return false negatives (403/429).
"""
import argparse
import datetime
import pathlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]]*\]\((<?[^)]+>?)\)')
CODE_FENCE = re.compile(r'^\s*```')
HEADERS = {"User-Agent": "human-cyber-risk-research-link-audit/1.0"}


def extract(path):
    inside = False
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if CODE_FENCE.match(line):
            inside = not inside
            continue
        if inside:
            continue
        for match in LINK.finditer(line):
            raw = match.group(1).strip().strip("<>")
            target = raw.split(' "')[0].split(" '")[0]
            if target:
                yield line_number, target


def probe(url):
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, headers=HEADERS, method=method)
            with urllib.request.urlopen(req, timeout=12) as response:
                return f"HTTP {response.status}", response.geturl()
        except urllib.error.HTTPError as err:
            if err.code in (403, 405, 429) and method == "HEAD":
                continue
            return f"HTTP {err.code}", url
        except (urllib.error.URLError, TimeoutError) as err:
            if method == "HEAD":
                continue
            return f"ERROR {type(err).__name__}", url
    return "ERROR unknown", url


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--external", action="store_true", help="Probe HTTP(S) destinations")
    parser.add_argument("--output", type=pathlib.Path, help="Write a Markdown audit report")
    args = parser.parse_args()
    files = sorted(ROOT.rglob("*.md"))
    results = []
    cache = {}
    for path in files:
        for line, link in extract(path):
            source = path.relative_to(ROOT).as_posix()
            if link.startswith(("https://", "http://")):
                if args.external:
                    if link not in cache:
                        cache[link] = probe(link)
                    status, resolved = cache[link]
                else:
                    status, resolved = "NOT CHECKED", link
            elif link.startswith(("mailto:", "tel:", "#")):
                status, resolved = "SKIPPED", link
            else:
                parsed = urllib.parse.urlsplit(link)
                destination = (path.parent / urllib.parse.unquote(parsed.path)).resolve()
                try:
                    destination.relative_to(ROOT.resolve())
                    status = "OK" if destination.is_file() else "MISSING"
                except ValueError:
                    status = "OUTSIDE REPOSITORY"
                resolved = destination.as_posix()
            results.append((source, line, link, status, resolved))
    failures = [r for r in results if r[3] in ("MISSING", "OUTSIDE REPOSITORY") or r[3].startswith(("HTTP 4", "HTTP 5", "ERROR"))]
    report = [
        "# Repository Markdown link audit",
        "",
        f"Generated UTC: {datetime.datetime.now(datetime.timezone.utc).isoformat()}",
        f"Markdown files: {len(files)}; link occurrences: {len(results)}; unique external links probed: {len(cache)}.",
        f"Flagged links: {len(failures)}.",
        "",
        "HTTP errors can reflect anti-bot restrictions, rate limits or transient failures; verify flagged URLs manually.",
        "This checks URL reachability and internal file paths, not citation metadata, anchor fragments or factual accuracy.",
        "",
        "## Flagged links",
        "",
        "| Source | Line | Link | Result |",
        "| --- | ---: | --- | --- |",
    ]
    for source, line, link, status, _ in failures:
        report.append(f"| `{source}` | {line} | `{link.replace('|', '%7C')}` | {status} |")
    report.extend(["", "## External status", "", "| URL | Status |", "| --- | --- |"])
    for url, (status, _) in sorted(cache.items()):
        report.append(f"| `{url.replace('|', '%7C')}` | {status} |")
    body = "\n".join(report) + "\n"
    if args.output:
        target = args.output if args.output.is_absolute() else ROOT / args.output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
    else:
        print(body)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
