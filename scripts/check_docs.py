"""Check local Markdown links and basic repository documentation consistency."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MD_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
issues = []
files = list(ROOT.rglob('*.md'))

for doc in files:
    content = doc.read_text(encoding='utf-8')
    if not content.strip():
        issues.append(f'{doc.relative_to(ROOT)}: empty document')
    for match in MD_LINK.finditer(content):
        target = match.group(1).strip().split(' ', 1)[0].strip('<>')
        if not target or target.startswith(('https://', 'http://', 'mailto:', '#')):
            continue
        path = unquote(target.split('#', 1)[0])
        if path and not (doc.parent / path).exists():
            issues.append(f'{doc.relative_to(ROOT)}: missing local link {target}')

print(f'Checked {len(files)} Markdown files.')
if issues:
    for issue in issues:
        print(f'ERROR: {issue}')
    sys.exit(1)
print('Documentation checks passed. No files changed.')
