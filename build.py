"""Wraps the page fragments in src/ into full HTML documents for GitHub Pages.

Edit the files in src/ and assets/, then run:  python build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{body}
</body>
</html>
"""

for src in (ROOT / "src").rglob("*.html"):
    head, _, body = src.read_text(encoding="utf-8").partition("<!-- /head -->")
    out = ROOT / src.relative_to(ROOT / "src")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEMPLATE.format(head=head.strip(), body=body.strip()), encoding="utf-8")
    print("built", out.relative_to(ROOT))
