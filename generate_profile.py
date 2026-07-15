#!/usr/bin/env python3
"""
Generates a neofetch-style GitHub profile SVG (dark + light variants)
combining an ASCII-art rendering of a portrait photo with an info panel.
"""

from PIL import Image, ImageOps
import html

# ---------- CONFIG ----------
PHOTO_PATH = "photo.png"
COLS = 64                 # ascii art character columns
CELL_W = 6.0               # svg px per character column
CELL_H = 12.6              # svg px per character row (matches CELL_W's terminal aspect)
CHAR_ASPECT = CELL_W / CELL_H   # monospace char height/width correction for resampling

RAMP = " .'`^,:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

FONT = "'SFMono-Regular','Consolas','Liberation Mono','Menlo',monospace"

# duotone stops (ink 0 -> 1)  RGB
DARK_STOPS = [
    (0.00, (13, 12, 26)),      # near invisible / bg blend
    (0.12, (43, 26, 82)),
    (0.30, (91, 51, 156)),
    (0.50, (139, 92, 246)),
    (0.72, (176, 132, 247)),
    (1.00, (233, 213, 255)),
]
LIGHT_STOPS = [
    (0.00, (255, 255, 255)),
    (0.12, (233, 220, 255)),
    (0.30, (196, 165, 240)),
    (0.50, (139, 92, 246)),
    (0.72, (91, 51, 156)),
    (1.00, (30, 16, 60)),
]


def lerp(a, b, t):
    return a + (b - a) * t


def color_at(ink, stops):
    for i in range(len(stops) - 1):
        p0, c0 = stops[i]
        p1, c1 = stops[i + 1]
        if p0 <= ink <= p1:
            t = 0 if p1 == p0 else (ink - p0) / (p1 - p0)
            r = int(lerp(c0[0], c1[0], t))
            g = int(lerp(c0[1], c1[1], t))
            b = int(lerp(c0[2], c1[2], t))
            return f"#{r:02x}{g:02x}{b:02x}"
    return f"#{stops[-1][1][0]:02x}{stops[-1][1][1]:02x}{stops[-1][1][2]:02x}"


def build_ascii_grid():
    im = Image.open(PHOTO_PATH).convert("L")
    im = ImageOps.autocontrast(im, cutoff=1)
    w, h = im.size
    rows = max(1, int(COLS * (h / w) * CHAR_ASPECT))
    small = im.resize((COLS, rows))
    px = small.load()

    grid_chars = []
    grid_ink = []
    for y in range(rows):
        crow, irow = [], []
        for x in range(COLS):
            lum = px[x, y] / 255.0
            ink = max(0.0, min(1.0, 1.0 - lum))
            # soften pure-background noise so the silhouette stays clean
            if ink < 0.055:
                ink = 0.0
            idx = int(ink * (len(RAMP) - 1))
            ch = RAMP[idx]
            if ink == 0.0:
                ch = " "
            crow.append(ch)
            irow.append(ink)
        grid_chars.append(crow)
        grid_ink.append(irow)
    return grid_chars, grid_ink, rows


def ascii_svg_group(grid_chars, grid_ink, rows, stops, cell_w, cell_h, x0, y0, font_size):
    lines = []
    for ry in range(rows):
        y = y0 + ry * cell_h + font_size
        run_color = None
        run_start = None
        run_text = ""
        spans = []

        def flush(end_x):
            nonlocal run_color, run_start, run_text
            if run_text.strip("") != "" and run_color is not None:
                spans.append(
                    f'<tspan x="{x0 + run_start * cell_w:.1f}" '
                    f'fill="{run_color}">{html.escape(run_text)}</tspan>'
                )
            run_color, run_start, run_text = None, None, ""

        for rx in range(COLS):
            ch = grid_chars[ry][rx]
            ink = grid_ink[ry][rx]
            if ch == " ":
                flush(rx)
                continue
            col = color_at(ink, stops)
            if col != run_color:
                flush(rx)
                run_color = col
                run_start = rx
                run_text = ch
            else:
                run_text += ch
        flush(COLS)

        if spans:
            lines.append(f'<text y="{y:.1f}" font-size="{font_size}">' + "".join(spans) + "</text>")
    return "\n    ".join(lines)


# ---------- INFO PANEL CONTENT ----------
INFO_FIELDS = [
    ("section", "umesh --profile"),
    ("gap", None),
    ("name", "Umesh Sai Hanuma Prasad Syamala"),
    ("kv", ("Degree", "B.Tech, CSE (AI & ML) \u00b7 CGPA 9.59/10")),
    ("kv", ("College", "Vishnu Institute of Technology, Bhimavaram")),
    ("kv", ("Intern", "VLED Lab, IIT Ropar \u00b7 May\u2013Jul 2026")),
    ("kv", ("Focus", "Agentic AI \u00b7 GenAI Systems \u00b7 Full-Stack")),
    ("gap", None),
    ("section", "~/stack"),
    ("kv", ("Lang", "Python \u00b7 Java \u00b7 JavaScript \u00b7 TypeScript \u00b7 SQL")),
    ("kv", ("AI/ML", "LangChain \u00b7 Gemini API \u00b7 FAISS \u00b7 Ollama \u00b7 OpenCV")),
    ("kv", ("Web", "React \u00b7 Node.js \u00b7 Flask \u00b7 FastAPI \u00b7 Electron")),
    ("kv", ("Data", "MongoDB \u00b7 Firebase \u00b7 Pandas \u00b7 NumPy")),
    ("gap", None),
    ("section", "~/projects"),
    ("kv", ("WayBig", "Electron desktop AI agent \u00b7 Gemini function-calling")),
    ("kv", ("NeuroNotes", "RAG notebook platform \u00b7 LangGraph + FAISS")),
    ("kv", ("InterviewAI", "Local interview simulator \u00b7 Llama 3.2 (3B)")),
    ("gap", None),
    ("section", "~/highlights"),
    ("kv", ("Award", "NPTEL Elite Gold, Java (IIT Kharagpur) \u2014 Top 5%")),
    ("kv", ("Cert", "Microsoft & LinkedIn \u2014 Career Essentials in GenAI")),
    ("gap", None),
    ("section", "~/reach"),
    ("kv", ("GitHub", "github.com/Umesh-369")),
    ("kv", ("LinkedIn", "linkedin.com/in/umeshsaihanumaprasad")),
    ("kv", ("Mail", "s.umeshsaihanumaprasad@gmail.com")),
]


def build_info_panel(x0, y0, dark: bool):
    label_color = "#a78bfa" if dark else "#7c3aed"
    section_color = "#f0abfc" if dark else "#a21caf"
    name_color = "#ffffff" if dark else "#1e1030"
    value_color = "#cbd5e1" if dark else "#3f3355"
    sep_color = "#3b3555" if dark else "#d8cdf0"

    line_h = 21
    font_size = 13.4
    lines = []
    y = y0
    label_w = 92

    for kind, content in INFO_FIELDS:
        if kind == "gap":
            y += line_h * 0.55
            continue
        if kind == "section":
            y += line_h * 0.15
            lines.append(
                f'<text x="{x0}" y="{y:.1f}" font-size="{font_size}" '
                f'font-weight="700" fill="{section_color}">{html.escape(content)}</text>'
            )
            y += line_h * 0.55
            lines.append(
                f'<line x1="{x0}" y1="{y:.1f}" x2="{x0 + 360}" y2="{y:.1f}" '
                f'stroke="{sep_color}" stroke-width="1"/>'
            )
            y += line_h * 0.85
            continue
        if kind == "name":
            lines.append(
                f'<text x="{x0}" y="{y:.1f}" font-size="16" '
                f'font-weight="700" fill="{name_color}">{html.escape(content)}</text>'
            )
            y += line_h * 1.3
            continue
        if kind == "kv":
            k, v = content
            lines.append(
                f'<text x="{x0}" y="{y:.1f}" font-size="{font_size}" '
                f'font-weight="600" fill="{label_color}">{html.escape(k)}</text>'
                f'<text x="{x0 + label_w}" y="{y:.1f}" font-size="{font_size}" '
                f'fill="{value_color}">{html.escape(v)}</text>'
            )
            y += line_h
            continue
    return "\n    ".join(lines), y


def render_svg(dark: bool, out_path: str):
    grid_chars, grid_ink, rows = build_ascii_grid()
    stops = DARK_STOPS if dark else LIGHT_STOPS

    bg = "#0b0c14" if dark else "#ffffff"
    panel_bg = "#11121c" if dark else "#faf8ff"
    border = "#2b2a3d" if dark else "#e3d9fb"
    title_color = "#9694b0" if dark else "#8b7fa8"
    accent_green = "#4ade80" if dark else "#16a34a"
    muted = "#6b7280" if dark else "#8b7fa8"

    width = 900
    ascii_font_size = 9.6
    cell_w = CELL_W
    cell_h = CELL_H
    ascii_x0 = 34
    ascii_y0 = 60
    ascii_block_h = rows * cell_h

    info_x0 = ascii_x0 + COLS * cell_w + 46
    info_y0 = 74

    ascii_svg = ascii_svg_group(grid_chars, grid_ink, rows, stops, cell_w, cell_h, ascii_x0, ascii_y0, ascii_font_size)
    info_svg, info_end_y = build_info_panel(info_x0, info_y0, dark)

    body_bottom = max(ascii_y0 + ascii_block_h, info_end_y) + 36
    height = int(body_bottom + 40)

    status_y = height - 34

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" font-family="{FONT}">
  <defs>
    <clipPath id="rounded"><rect x="0" y="0" width="{width}" height="{height}" rx="14" ry="14"/></clipPath>
  </defs>
  <g clip-path="url(#rounded)">
    <rect x="0" y="0" width="{width}" height="{height}" fill="{bg}"/>
    <rect x="0" y="0" width="{width}" height="34" fill="{panel_bg}"/>
    <rect x="0" y="0" width="{width}" height="{height}" fill="none" stroke="{border}" stroke-width="1"/>
    <line x1="0" y1="34" x2="{width}" y2="34" stroke="{border}" stroke-width="1"/>

    <circle cx="20" cy="17" r="6" fill="#ff5f57"/>
    <circle cx="40" cy="17" r="6" fill="#febc2e"/>
    <circle cx="60" cy="17" r="6" fill="#28c840"/>
    <text x="{width/2}" y="21" font-size="12.5" fill="{title_color}" text-anchor="middle">umesh@github &#8212; zsh &#8212; 110x{rows+18}</text>

    {ascii_svg}

    {info_svg}

    <line x1="24" y1="{status_y - 20}" x2="{width-24}" y2="{status_y - 20}" stroke="{border}" stroke-width="1"/>
    <circle cx="34" cy="{status_y}" r="4" fill="{accent_green}"/>
    <text x="46" y="{status_y+4}" font-size="12.5" fill="{muted}">open to AI/ML &amp; Agentic Engineering internships</text>
    <text x="{width-24}" y="{status_y+4}" font-size="12.5" fill="{muted}" text-anchor="end">last generated \u00b7 Jul 2026</text>
  </g>
</svg>'''

    with open(out_path, "w") as f:
        f.write(svg)
    print(f"wrote {out_path} ({width}x{height}, {rows} rows)")


if __name__ == "__main__":
    render_svg(dark=True, out_path="dark.svg")
    render_svg(dark=False, out_path="light.svg")
