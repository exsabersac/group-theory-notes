#!/usr/bin/env python3
"""Build unofficial Chinese study PDFs of Matthew Macauley's VGT slides.

Reads zh-src/sectionN.md translation sources, writes a Typst document, and
compiles an A4 portrait PDF: original slide image on top, Chinese text below.

Usage:
  python3 build_zh_pdf.py            # all sections
  python3 build_zh_pdf.py 1 2        # selected sections
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent.parent  # group-theory-notes
BUILD = ROOT / "_build"
IMG_ROOT = BUILD / "images"
TYP_ROOT = BUILD / "typst"
SRC_ROOT = ROOT / "zh-src"
FONT_PATHS = [
    "/usr/share/fonts/opentype/noto",
    "/usr/share/fonts/truetype",
    "/usr/share/fonts/opentype",
    "/usr/share/fonts",
]

SECTIONS = [
    {
        "n": 1,
        "pages": 61,
        "stem": "Macauley-Math4120-section1-Groups-intuitively",
        "title_en": "Section 1: Groups, intuitively",
        "title_zh": "第 1 节：直观地认识群",
    },
    {
        "n": 2,
        "pages": 37,
        "stem": "Macauley-Math4120-section2-Examples-of-groups",
        "title_en": "Section 2: Examples of groups",
        "title_zh": "第 2 节：群的例子",
    },
    {
        "n": 3,
        "pages": 67,
        "stem": "Macauley-Math4120-section3-Structure-of-groups",
        "title_en": "Section 3: The structure of groups",
        "title_zh": "第 3 节：群的结构",
    },
    {
        "n": 4,
        "pages": 51,
        "stem": "Macauley-Math4120-section4-Maps-between-groups",
        "title_en": "Section 4: Maps between groups",
        "title_zh": "第 4 节：群之间的映射",
    },
    {
        "n": 5,
        "pages": 57,
        "stem": "Macauley-Math4120-section5-Groups-acting-on-sets",
        "title_en": "Section 5: Groups acting on sets",
        "title_zh": "第 5 节：群在集合上的作用",
    },
    {
        "n": 6,
        "pages": 59,
        "stem": "Macauley-Math4120-section6-Field-and-Galois-theory",
        "title_en": "Section 6: Field and Galois theory",
        "title_zh": "第 6 节：域与伽罗瓦理论",
    },
    {
        "n": 7,
        "pages": 46,
        "stem": "Macauley-Math4120-section7-Ring-theory",
        "title_en": "Section 7: Ring theory",
        "title_zh": "第 7 节：环论",
    },
]

COURSE_URL = "https://www.math.clemson.edu/~macaule/classes/m20_math4120/"
LICENSE_INDEX = "https://www.math.clemson.edu/~macaule/youtube.html"
CC_URL = "https://creativecommons.org/licenses/by-nc-sa/4.0/"
YOUTUBE = "https://www.youtube.com/playlist?list=PLwV-9DG53NDxU337smpTwm6sef4x-SCLv"

PAGE_RE = re.compile(r"^%%%\s*PAGE\s+(\d+)\s*$")


def parse_source(path: Path) -> dict[int, str]:
    text = path.read_text(encoding="utf-8")
    pages: dict[int, str] = {}
    current: int | None = None
    buf: list[str] = []
    for line in text.splitlines():
        m = PAGE_RE.match(line.strip())
        if m:
            if current is not None:
                pages[current] = "\n".join(buf).strip()
            current = int(m.group(1))
            buf = []
        else:
            if current is not None:
                buf.append(line)
    if current is not None:
        pages[current] = "\n".join(buf).strip()
    return pages


def escape_typst_outside_math(text: str) -> str:
    """Escape typst-special characters in markup, leaving $math$ intact."""
    parts = re.split(r"(\$[^$]*\$)", text)
    out = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            out.append(part)  # math
            continue
        # Don't escape inside already-written typst calls starting with #
        # Escape # except at start of a typst command we explicitly allow later.
        # For body text, escape #, and unmatched .
        # Convert our lightweight markup first in convert_body.
        out.append(part)
    return "".join(out)


# box heading keywords
BOX_HEADINGS = {
    "核心思想",
    "定义",
    "非正式定义",
    "正式定义",
    "定理",
    "命题",
    "引理",
    "推论",
    "注记",
    "注",
    "备注",
    "观察",
    "例子",
    "例",
    "习题",
    "练习",
    "事实",
    "问题",
    "问题组",
    "算法",
    "警告",
    "注意事项",
    "说明",
    "评论",
    "摘要",
    "概览",
    "提示",
    "约定",
    "验证",
    "证明",
    "检验",
}


def typst_escape_text(s: str) -> str:
    return (
        s.replace("\\", "\\\\")
        .replace("#", "\\#")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("_", "\\_")
    )


def convert_body(raw: str) -> str:
    """Convert lightweight markup into typst markup."""
    lines = raw.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # title
        if stripped.startswith("== "):
            title = typst_escape_text(stripped[3:].strip())
            out.append(
                f'#text(size: 13.5pt, weight: "bold", fill: rgb("#2c2a7a"))[{title}]'
            )
            out.append("#v(0.35em)")
            i += 1
            continue

        # box / section heading
        if stripped.startswith("### "):
            heading = stripped[4:].strip()
            key = heading.split("（")[0].split("(")[0].strip()
            color = "#1b5e20" if key in {"核心思想"} else (
                "#6a1b1b" if key in {"警告", "注意事项"} else
                "#1a237e" if key in {"定义", "非正式定义", "正式定义", "约定"} else
                "#4a148c" if key in {"定理", "命题", "引理", "推论"} else
                "#004d40"
            )
            h = typst_escape_text(heading)
            out.append(
                f'#block(above: 0.55em, below: 0.25em)[#text(weight: "bold", fill: rgb("{color}"), size: 11pt)[{h}]]'
            )
            i += 1
            continue

        # typst-native lists: "- item" and "+ item"
        m_b = re.match(r"^- (.*)$", stripped)
        m_e = re.match(r"^(\d+)\. (.*)$", stripped)
        if m_b:
            out.append("- " + style_inline(m_b.group(1)))
            i += 1
            continue
        if m_e:
            out.append("+ " + style_inline(m_e.group(2)))
            i += 1
            continue

        if stripped == "":
            out.append("#v(0.28em)")
            i += 1
            continue

        out.append(style_inline(stripped))
        i += 1

    return "\n".join(out)


def normalize_math(math_inner: str) -> str:
    """Light TeX-to-typst tweaks inside $...$."""
    s = math_inner
    s = s.replace("triangle.l.eq", " lt.tri.eq ")
    s = s.replace("^circ", " degree")
    s = s.replace("\\circ", " degree")
    s = s.replace("\\times", " times ")
    s = s.replace("\\in", " in ")
    s = s.replace("\\leq", " <=")
    s = s.replace("\\geq", " >=")
    s = s.replace("\\neq", " eq.not ")
    s = s.replace("\\cdot", " dot ")
    s = s.replace("\\circ", " compose ")  # after degree already handled
    return s


def style_inline(text: str) -> str:
    """Handle *emphasis* and $math$, escape the rest."""
    # split by math first
    parts = re.split(r"(\$[^$]*\$)", text)
    rendered = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            inner = part[1:-1]
            rendered.append("$" + normalize_math(inner) + "$")
            continue
        # emphasis *...* but not **
        chunks = re.split(r"(\*[^*]+\*)", part)
        acc = []
        for ch in chunks:
            if len(ch) >= 2 and ch.startswith("*") and ch.endswith("*"):
                inner = typst_escape_text(ch[1:-1])
                acc.append(f"#text(weight: \"semibold\")[{inner}]")
            else:
                acc.append(typst_escape_text(ch))
        rendered.append("".join(acc))
    return "".join(rendered)


def title_page_typst(sec: dict) -> str:
    title_zh = sec["title_zh"]
    title_en = sec["title_en"]
    return f'''
#page(
  margin: (x: 22mm, y: 20mm),
  footer: [
    #set text(size: 8pt, fill: rgb("#444"))
    #line(length: 100%, stroke: 0.45pt + rgb("#3d348b"))
    #v(3pt)
    #align(right)[非官方中译本・CC BY-NC-SA 4.0]
  ],
)[
  #align(center)[
    #v(8mm)
    #text(size: 12pt, fill: rgb("#444"))[Matthew Macauley 课程讲义中译]
    #v(4mm)
    #text(size: 22pt, weight: "bold", fill: rgb("#2c2a7a"))[{title_zh}]
    #v(2mm)
    #text(size: 12pt, fill: rgb("#444"))[{title_en}]
    #v(8mm)
    #text(size: 13pt, weight: "bold")[非官方中译本（仅供学习使用）]
    #v(1mm)
    #text(size: 11pt)[并非官方版本或官方中文版]
  ]

  #v(10mm)
  #set text(size: 10.5pt)
  #set par(justify: true, leading: 0.85em, spacing: 0.65em)

  *原作者：* Matthew Macauley #h(1em)
  *单位：* Department of Mathematical Sciences, Clemson University

  *课程：* Math 4120 Modern Algebra（2020 年夏季课程材料；配套 Visual Group Theory 视频课）

  *原讲义许可：* Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（#link("{CC_URL}")[CC BY-NC-SA 4.0]）

  *本译本许可：* 本文件是上述讲义的演绎作品，同样以 #link("{CC_URL}")[CC BY-NC-SA 4.0] 许可发布。转载、改编须署名原作者 Matthew Macauley 与译者说明，不得用于商业目的，并以相同许可分享。

  *原课程页：* #link("{COURSE_URL}")[{COURSE_URL}]

  *许可说明索引：* #link("{LICENSE_INDEX}")[{LICENSE_INDEX}]

  *配套视频课：* #link("{YOUTUBE}")[YouTube 播放列表（43 讲）]

  #v(4mm)
  #text(weight: "bold")[译者说明]
  #v(1mm)
  本译本将每一页原幻灯片图像置于上方，中文译文置于下方，以便对照阅读，并保留凯莱图、照片与表格等插图。页脚标明原幻灯片页码。原幻灯片页脚中的 “M. Macauley (Clemson) …” 已出现在图像中，译文不再重复。

  公式、群名与记号尽量保持原样，例如 $D_4$、$S_3$、$A_4$、$V_4$、$ZZ$、$ZZ_n$、$e$ 等。译文如有错漏，一律以原幻灯片为准。这不是官方中文版。
]
'''


def long_page_image_width(body: str) -> str:
    """Shrink the slide image slightly when the Chinese text is long."""
    # rough length without math markup
    n = len(re.sub(r"\s+", "", body))
    if n > 1600:
        return "86%"
    if n > 1200:
        return "92%"
    if n > 900:
        return "96%"
    return "100%"


def typst_font_size(body: str) -> str:
    n = len(re.sub(r"\s+", "", body))
    if n > 1600:
        return "9.2pt"
    if n > 1200:
        return "9.7pt"
    if n > 900:
        return "10.1pt"
    return "10.5pt"


def build_typst(sec: dict, pages: dict[int, str]) -> str:
    stem = sec["stem"]
    total = sec["pages"]
    missing = [i for i in range(1, total + 1) if i not in pages]
    if missing:
        raise SystemExit(f"{stem}: missing translations for pages {missing}")
    extra = sorted(set(pages) - set(range(1, total + 1)))
    if extra:
        raise SystemExit(f"{stem}: unexpected page numbers {extra}")

    img_dir = (IMG_ROOT / stem).resolve()
    parts = [
        '#set document(title: "' + sec["title_zh"] + '（非官方中译本）", author: "Unofficial Chinese translation of Matthew Macauley, Math 4120")',
        '#set text(font: ("Noto Serif CJK SC", "Libertinus Serif", "New Computer Modern"), size: 10.5pt, lang: "zh")',
        '#set par(justify: true, leading: 0.8em)',
        '#show math.equation: set text(font: "New Computer Modern Math")',
        title_page_typst(sec),
    ]

    for n in range(1, total + 1):
        body_src = pages[n]
        body = convert_body(body_src)
        img = img_dir / f"p-{n:02d}.jpg"
        if not img.exists():
            raise SystemExit(f"missing image: {img}")
        width = long_page_image_width(body_src)
        fsize = typst_font_size(body_src)
        # typst path: use POSIX string, escape backslashes
        img_s = str(img).replace("\\", "/")
        footer_left = f'{sec["title_zh"]} · 原幻灯片 {n} / {total}'
        parts.append(f'''
#page(
  paper: "a4",
  margin: (x: 13mm, top: 9mm, bottom: 15mm),
  footer: [
    #set text(size: 8pt, fill: rgb("#333333"))
    #line(length: 100%, stroke: 0.45pt + rgb("#3d348b"))
    #v(3pt)
    #grid(
      columns: (1fr, auto),
      align: (left + horizon, right + horizon),
      [{footer_left}],
      [非官方中译本・CC BY-NC-SA 4.0],
    )
  ],
)[
  #align(center)[
    #block(width: {width}, stroke: 0.4pt + rgb("#c8c8c8"), inset: 0pt, clip: true)[
      #image("{img_s}", width: 100%)
    ]
  ]
  #v(0.55em)
  #set text(size: {fsize})
  #set par(justify: true, leading: 0.78em, spacing: 0.55em)
  {body}
]
''')
    return "\n".join(parts)


def write_companion_md(sec: dict, pages: dict[int, str], dest: Path) -> None:
    lines = [
        f'# {sec["title_zh"]}',
        "",
        f'原名：*{sec["title_en"]}*',
        "",
        "原作者：Matthew Macauley（Clemson University, Department of Mathematical Sciences）",
        "",
        "课程：Math 4120 Modern Algebra（2020 年夏季课程材料；配套 Visual Group Theory 视频课）",
        "",
        f'许可：本译本为原讲义的演绎作品，与原文同以 [CC BY-NC-SA 4.0]({CC_URL}) 发布。这是*非官方中译本*，仅供学习对照，并非官方中文版。',
        "",
        f'原课程页：<{COURSE_URL}>  ',
        f'许可说明索引：<{LICENSE_INDEX}>',
        "",
        "说明：公式使用 `$...$`（Typst / 类 TeX 记号）。完整对照版（含原幻灯片图像）见同目录下的 PDF。",
        "",
    ]
    for n in range(1, sec["pages"] + 1):
        body = pages[n]
        # strip == title marker into bold
        body2 = re.sub(r"^== (.+)$", r"**\1**", body, flags=re.M)
        body2 = re.sub(r"^### (.+)$", r"**\1**", body2, flags=re.M)
        lines.append(f"## 第 {n} 页 / {sec['pages']}")
        lines.append("")
        lines.append(body2.strip())
        lines.append("")
    dest.write_text("\n".join(lines) + "\n", encoding="utf-8")


def typst_bin() -> str:
    for p in [
        Path.home() / ".local/bin/typst",
        Path("/usr/local/bin/typst"),
        Path("/usr/bin/typst"),
    ]:
        if p.exists():
            return str(p)
    return "typst"


def compile_section(sec: dict) -> Path:
    src = SRC_ROOT / f"section{sec['n']}.md"
    if not src.exists():
        raise SystemExit(f"missing translation source: {src}")
    pages = parse_source(src)
    typ_src = build_typst(sec, pages)
    TYP_ROOT.mkdir(parents=True, exist_ok=True)
    typ_path = TYP_ROOT / f"section{sec['n']}.typ"
    typ_path.write_text(typ_src, encoding="utf-8")

    out_pdf = ROOT / f"{sec['stem']}-zh.pdf"
    cmd = [typst_bin(), "compile", "--root", "/", str(typ_path), str(out_pdf)]
    for fp in FONT_PATHS:
        if Path(fp).exists():
            cmd[2:2] = ["--font-path", fp]
    print("Running:", " ".join(cmd), flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout)
        sys.stderr.write(r.stderr)
        raise SystemExit(f"typst failed for section {sec['n']} (code {r.returncode})")
    if r.stderr:
        # typst warnings
        sys.stderr.write(r.stderr)
    companion = ROOT / f"{sec['stem']}-zh.md"
    write_companion_md(sec, pages, companion)
    size = out_pdf.stat().st_size
    print(f"Wrote {out_pdf} ({size} bytes) and {companion}")
    return out_pdf


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("sections", nargs="*", type=int, help="section numbers (default: all that have sources)")
    args = p.parse_args(argv)
    wanted = args.sections or [s["n"] for s in SECTIONS if (SRC_ROOT / f"section{s['n']}.md").exists()]
    by_n = {s["n"]: s for s in SECTIONS}
    for n in wanted:
        if n not in by_n:
            raise SystemExit(f"unknown section {n}")
        compile_section(by_n[n])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
