#!/usr/bin/env python3
"""Convert a proposal markdown file to a board-ready PDF.

Pipeline: markdown -> HTML (with tables/fenced-code extensions) -> WeasyPrint -> PDF.
Designed for the DefendableOS proposal package.

Usage:
    python3 build_pdf.py 05_EXCLUSIVE_LISTING_PROPOSAL.md
    python3 build_pdf.py --all   # builds PDFs for 04 and 05 (board-facing)
"""
import argparse
import sys
from pathlib import Path

import markdown
from weasyprint import HTML, CSS

CSS_STYLES = """
@page {
    size: Letter;
    margin: 0.75in 0.6in 0.85in 0.6in;
    @bottom-center {
        content: "DefendableOS Listing Package · CONFIDENTIAL · Page " counter(page) " of " counter(pages);
        font-family: "Helvetica", "Arial", sans-serif;
        font-size: 8pt;
        color: #888;
    }
    @top-right {
        content: "DDEED-LIST-DOS-001-v1";
        font-family: "Helvetica", "Arial", sans-serif;
        font-size: 8pt;
        color: #888;
    }
}
body {
    font-family: "Helvetica", "Arial", sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #1a1a1a;
}
h1 {
    font-size: 22pt;
    color: #0a0a0a;
    border-bottom: 3px solid #d4a017;
    padding-bottom: 8px;
    margin-top: 0;
    page-break-after: avoid;
}
h2 {
    font-size: 15pt;
    color: #2a2a2a;
    margin-top: 24px;
    border-bottom: 1px solid #d4a017;
    padding-bottom: 4px;
    page-break-after: avoid;
}
h3 {
    font-size: 12pt;
    color: #444;
    margin-top: 18px;
    page-break-after: avoid;
}
h4, h5, h6 {
    font-size: 10.5pt;
    color: #555;
    page-break-after: avoid;
}
p {
    margin: 8px 0;
    orphans: 3;
    widows: 3;
}
strong { color: #0a0a0a; }
em { color: #5a3e00; }
hr {
    border: none;
    border-top: 1px solid #d4a017;
    margin: 18px 0;
}
blockquote {
    border-left: 3px solid #d4a017;
    padding-left: 14px;
    margin-left: 0;
    color: #444;
    font-style: italic;
}
code {
    font-family: "Menlo", "Monaco", "Courier New", monospace;
    font-size: 9pt;
    background: #f5f1e6;
    padding: 1px 4px;
    border-radius: 2px;
    color: #5a3e00;
}
pre {
    background: #f7f3e6;
    border: 1px solid #e0d5b0;
    border-radius: 3px;
    padding: 10px;
    font-family: "Menlo", "Monaco", "Courier New", monospace;
    font-size: 8.5pt;
    line-height: 1.35;
    overflow-wrap: break-word;
    page-break-inside: avoid;
}
pre code {
    background: none;
    padding: 0;
    color: #1a1a1a;
}
table {
    border-collapse: collapse;
    margin: 14px 0;
    width: 100%;
    font-size: 9pt;
    page-break-inside: avoid;
}
th, td {
    border: 1px solid #d4d4d4;
    padding: 6px 8px;
    text-align: left;
    vertical-align: top;
}
th {
    background: #f7f3e6;
    color: #0a0a0a;
    font-weight: 700;
    border-bottom: 2px solid #d4a017;
}
tr:nth-child(even) td {
    background: #fafafa;
}
ul, ol {
    margin: 8px 0;
    padding-left: 22px;
}
li {
    margin: 3px 0;
}
a { color: #5a3e00; text-decoration: none; }
a:hover { text-decoration: underline; }

/* First page banner */
h1:first-of-type {
    text-align: center;
    margin-bottom: 4px;
}
h1:first-of-type + h3 {
    text-align: center;
    color: #5a3e00;
    margin-top: 0;
    border: none;
    font-weight: normal;
    font-style: italic;
}

/* Avoid awkward page breaks */
h2, h3 { page-break-after: avoid; }
table, pre, blockquote { page-break-inside: avoid; }
"""

EXTENSIONS = [
    "tables",
    "fenced_code",
    "attr_list",
    "def_list",
    "admonition",
    "toc",
    "sane_lists",
    "smarty",
]


def md_to_html(md_text: str) -> str:
    body = markdown.markdown(md_text, extensions=EXTENSIONS, output_format="html5")
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>DefendableOS Listing Proposal</title>
</head>
<body>
{body}
</body>
</html>
"""


def build_pdf(md_path: Path, out_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    html_text = md_to_html(md_text)
    HTML(string=html_text, base_url=str(md_path.parent)).write_pdf(
        target=str(out_path),
        stylesheets=[CSS(string=CSS_STYLES)],
    )
    size_kb = out_path.stat().st_size / 1024
    print(f"  built: {out_path.name} ({size_kb:.1f} KB)")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build PDF from proposal markdown.")
    parser.add_argument("markdown", nargs="?", help="Markdown file to convert")
    parser.add_argument("--all", action="store_true", help="Build all board-facing proposals")
    args = parser.parse_args()

    here = Path(__file__).resolve().parent

    if args.all:
        targets = [
            here / "04_BOARD_PROPOSAL.md",
            here / "05_EXCLUSIVE_LISTING_PROPOSAL.md",
            here / "06_REP_AGREEMENT.md",
        ]
    elif args.markdown:
        targets = [here / args.markdown]
    else:
        print("usage: build_pdf.py <markdown-file>  or  --all", file=sys.stderr)
        return 2

    for md_path in targets:
        if not md_path.exists():
            print(f"  SKIP (not found): {md_path.name}")
            continue
        pdf_path = md_path.with_suffix(".pdf")
        print(f"building: {md_path.name} -> {pdf_path.name}")
        build_pdf(md_path, pdf_path)

    return 0


if __name__ == "__main__":
    sys.exit(main())
