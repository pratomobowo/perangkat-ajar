#!/usr/bin/env python3
"""
Pipeline MD → HTML → PDF untuk dokumen perangkat ajar (portable).
Pemakaian:
    python3 gen_pdf_from_md.py input.md output.pdf "Header dokumen" [landscape]
Dependensi:
    pip install markdown-it-py weasyprint
Catatan:
    - MD = data saja; styling dari CSS bawaan script ini (gaya dokumen perangkat ajar).
    - Arg ke-4 "landscape" untuk tabel lebar (matriks Prosem).
"""
import sys

try:
    from markdown_it import MarkdownIt
    from weasyprint import HTML
except ImportError as e:
    sys.exit(f"Dependensi kurang: {e}\nInstall dulu: pip install markdown-it-py weasyprint")


def build_css(header_text="", landscape=False):
    page = "A4 landscape" if landscape else "A4 portrait"
    margin = "8mm 8mm 12mm 8mm" if landscape else "12mm 11mm 14mm 11mm"
    return f"""
@page {{ size: {page}; margin: {margin};
        @top-center {{ content: "{header_text}"; font-size: 7.5pt; color: #555; font-family: 'DejaVu Sans', sans-serif; }}
        @bottom-center {{ content: "Hal. " counter(page) " / " counter(pages); font-size: 7.5pt; color: #888; font-family: 'DejaVu Sans', sans-serif; }} }}
body {{ font-family: 'DejaVu Sans', sans-serif; font-size: 8.8pt; color: #222; line-height: 1.45; text-align: justify; }}
h1 {{ font-size: 15pt; color: #1a5276; text-align: center; margin: 0 0 2pt 0; page-break-after: avoid; }}
h2 {{ font-size: 12.5pt; color: #1a5276; border-bottom: 1.2pt solid #2980b9; padding-bottom: 2pt; margin: 12pt 0 6pt 0; page-break-after: avoid; }}
h3 {{ font-size: 11pt; color: #1a5276; margin: 10pt 0 4pt 0; page-break-after: avoid; }}
h4 {{ text-align: left; color: #1a5276; background: #eaf2f8; border-left: 3pt solid #2980b9; padding: 4pt 6pt; margin: 8pt 0 4pt 0; border-radius: 0 3pt 3pt 0; page-break-after: avoid; }}
h5 {{ text-align: left; color: #1a5276; margin: 6pt 0 3pt 0; }}
p {{ margin: 3pt 0; }}
.sub {{ text-align: center; color: #555; font-size: 9pt; margin-bottom: 10pt; }}
table {{ width: 100%; border-collapse: collapse; margin: 5pt 0; }}
th, td {{ border: 0.6pt solid #5d6d7e; padding: 3.5pt 4.5pt; vertical-align: top; }}
th {{ background: #2980b9; color: #fff; font-weight: bold; text-align: center; font-size: 8.2pt; }}
td {{ font-size: 8.5pt; }}
.c {{ text-align: center; }}
.keg {{ text-align: center; font-size: 7pt; color: #8b4513; background: #fdf6e3; }}
tr:nth-child(even) td {{ background: #f4f9fd; }}
tr {{ page-break-inside: avoid; }}
.lbl {{ background: #eaf2f8; font-weight: bold; width: 26%; }}
.pertemuan {{ border: 1pt solid #2980b9; border-radius: 5pt; padding: 7pt 9pt; margin: 8pt 0; }}
.pertemuan h4 {{ color: #1a5276; margin: 0 0 4pt 0; font-size: 10.5pt; page-break-after: avoid; }}
.tahap {{ font-weight: bold; color: #1a5276; margin-top: 6pt; page-break-after: avoid; }}
.prinsip {{ font-style: italic; color: #666; font-size: 8pt; }}
.kotak-ttd {{ width: 100%; page-break-inside: avoid; margin-top: 8pt; }}
.kotak-ttd td {{ border: none; text-align: center; font-size: 9pt; }}
.note {{ font-size: 8pt; color: #666; font-style: italic; margin-top: 4pt; }}
.small {{ font-size: 8pt; }}
code {{ font-family: 'DejaVu Sans Mono', monospace; font-size: 7.8pt; background: #f0f0f0; padding: 0 2pt; }}
pre {{ background: #f6f8fa; border: 0.5pt solid #ccc; border-radius: 3pt; padding: 4pt 6pt; font-family: 'DejaVu Sans Mono', monospace; font-size: 7.8pt; white-space: pre-wrap; margin: 3pt 0; }}
ul, ol {{ margin: 3pt 0 6pt 0; padding-left: 18pt; }}
li {{ margin-bottom: 1.5pt; }}
blockquote {{ border-left: 3pt solid #95a5a6; margin: 4pt 0; padding: 2pt 8pt; color: #555; }}
hr {{ border: none; border-top: 1pt solid #bdc3c7; margin: 8pt 0; }}
.pagebreak {{ page-break-before: always; }}
"""


def md_to_pdf(md_path, pdf_out, header_text="", extra_css="", landscape=False):
    """Konversi MD → PDF (MD → HTML via markdown-it → PDF via WeasyPrint)."""
    with open(md_path, encoding='utf-8') as f:
        md_text = f.read()
    html_body = MarkdownIt("commonmark").enable("table").render(md_text)
    css = build_css(header_text, landscape)
    html = f"""<!DOCTYPE html><html lang="id"><head><meta charset="utf-8"><style>{css}{extra_css}</style></head><body>{html_body}</body></html>"""
    tmp = '/tmp/md_pipeline.html'
    with open(tmp, 'w', encoding='utf-8') as f:
        f.write(html)
    HTML(filename=tmp).write_pdf(pdf_out)
    return len(html_body)


if __name__ == '__main__':
    # input MD arg1, output PDF arg2, header arg3 (opsional), orientasi arg4 "landscape" (opsional)
    if len(sys.argv) < 3:
        sys.exit("Pemakaian: gen_pdf_from_md.py input.md output.pdf [\"header\"] [landscape]")
    src = sys.argv[1]
    dst = sys.argv[2]
    header = sys.argv[3] if len(sys.argv) > 3 else ""
    landscape = len(sys.argv) > 4 and sys.argv[4] == "landscape"
    n = md_to_pdf(src, dst, header, "", landscape)
    print(f"OK: {src} → {dst} ({n} chars HTML)")
