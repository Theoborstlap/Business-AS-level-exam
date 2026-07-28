"""
A tiny, dependency-free PDF generation engine.

Supports: multiple A4 pages, automatic page breaks, word-wrapped paragraphs,
headings, bullet lists, tables, horizontal rules, and vector primitives
(lines, rectangles, filled rectangles, text) used to draw business diagrams.

Fonts used are the PDF standard-14 (no embedding needed). WinAnsiEncoding is
declared so currency symbols (GBP, EUR) and typographic dashes/quotes render.
"""

# ---------------------------------------------------------------------------
# Helvetica character widths (units per 1000 em) for WinAnsi/ASCII range.
# Used for accurate word wrapping. Bold/oblique reuse these with a safety factor.
# ---------------------------------------------------------------------------
_HELV_W = {
    ' ': 278, '!': 278, '"': 355, '#': 556, '$': 556, '%': 889, '&': 667,
    "'": 191, '(': 333, ')': 333, '*': 389, '+': 584, ',': 278, '-': 333,
    '.': 278, '/': 278, '0': 556, '1': 556, '2': 556, '3': 556, '4': 556,
    '5': 556, '6': 556, '7': 556, '8': 556, '9': 556, ':': 278, ';': 278,
    '<': 584, '=': 584, '>': 584, '?': 556, '@': 1015, 'A': 667, 'B': 667,
    'C': 722, 'D': 722, 'E': 667, 'F': 611, 'G': 778, 'H': 722, 'I': 278,
    'J': 500, 'K': 667, 'L': 556, 'M': 833, 'N': 722, 'O': 778, 'P': 667,
    'Q': 778, 'R': 722, 'S': 667, 'T': 611, 'U': 722, 'V': 667, 'W': 944,
    'X': 667, 'Y': 667, 'Z': 611, '[': 278, '\\': 278, ']': 278, '^': 469,
    '_': 556, '`': 333, 'a': 556, 'b': 556, 'c': 500, 'd': 556, 'e': 556,
    'f': 278, 'g': 556, 'h': 556, 'i': 222, 'j': 222, 'k': 500, 'l': 222,
    'm': 833, 'n': 556, 'o': 556, 'p': 556, 'q': 556, 'r': 333, 's': 500,
    't': 278, 'u': 556, 'v': 500, 'w': 722, 'x': 500, 'y': 500, 'z': 500,
    '{': 334, '|': 260, '}': 334, '~': 584,
}
_DEFAULT_W = 556

# Common non-ASCII characters we care about (currency, dashes, quotes)
_EXTRA_W = {
    '\u00a3': 556,  # GBP
    '\u20ac': 556,  # EUR
    '\u2013': 556,  # en dash
    '\u2014': 1000,  # em dash
    '\u2018': 222, '\u2019': 222,  # single quotes
    '\u201c': 333, '\u201d': 333,  # double quotes
    '\u2022': 350,  # bullet
    '\u00b0': 400,  # degree
    '\u00d7': 584,  # multiply
    '\u2248': 549,
}


def char_width(ch, size, bold=False):
    w = _HELV_W.get(ch)
    if w is None:
        w = _EXTRA_W.get(ch, _DEFAULT_W)
    if bold:
        w = int(w * 1.04)
    return w * size / 1000.0


def text_width(s, size, bold=False):
    return sum(char_width(c, size, bold) for c in s)


# Map characters PDF standard fonts can't show to safe equivalents,
# then encode as cp1252 (WinAnsi).
_SANITIZE = {
    '\u2192': '->', '\u2190': '<-', '\u21d2': '=>',
    '\u2264': '<=', '\u2265': '>=', '\u2260': '!=',
    '\u2212': '-',        # minus sign -> hyphen (not in WinAnsi)
    '\u2248': '~',        # approximately equal (not in WinAnsi)
    '\u00bd': '1/2', '\u00bc': '1/4', '\u00be': '3/4',
    '\ufb01': 'fi', '\ufb02': 'fl',
    '\u00a0': ' ',
}


def _enc(s):
    # map characters the standard fonts can't show to safe ASCII equivalents
    s = ''.join(_SANITIZE.get(ch, ch) for ch in s)
    # encode to WinAnsi (cp1252) bytes so the declared /WinAnsiEncoding renders
    # currency symbols, en/em dashes and typographic quotes correctly, then hold
    # them as a latin-1 string so the final latin-1 stream encode is byte-exact.
    s = s.encode('cp1252', 'replace').decode('latin-1')
    # escape PDF string special chars
    s = s.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')
    return s


# Font resource names
F_REG = 'F1'   # Helvetica
F_BOLD = 'F2'  # Helvetica-Bold
F_OBL = 'F3'   # Helvetica-Oblique
F_BI = 'F4'    # Helvetica-BoldOblique

PAGE_W = 595.28   # A4 width in points
PAGE_H = 841.89   # A4 height in points


class Color:
    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def s(self):
        return f"{self.r:.3f} {self.g:.3f} {self.b:.3f}"


BLACK = Color(0, 0, 0)
DARK = Color(0.12, 0.12, 0.12)
GREY = Color(0.45, 0.45, 0.45)
LIGHT = Color(0.90, 0.90, 0.90)
LIGHTER = Color(0.955, 0.955, 0.955)
NAVY = Color(0.10, 0.20, 0.42)
MAROON = Color(0.45, 0.10, 0.12)
BLUE = Color(0.15, 0.35, 0.70)
RED = Color(0.75, 0.15, 0.15)
GREEN = Color(0.10, 0.45, 0.20)
BOXBG = Color(0.96, 0.97, 0.99)
BOXBORDER = Color(0.60, 0.66, 0.78)


class PDF:
    def __init__(self, margin_l=56, margin_r=56, margin_t=56, margin_b=54):
        self.pages = []          # list of content-op string lists
        self.ml = margin_l
        self.mr = margin_r
        self.mt = margin_t
        self.mb = margin_b
        self.x = margin_l
        self.y = PAGE_H - margin_t
        self._ops = None
        self.page_no = 0
        self.on_new_page = None   # callback(pdf) run after each page starts
        self.footer = None        # callback(pdf) run before page finalised
        self._pending_footers = []

    # -- page management ----------------------------------------------------
    @property
    def content_w(self):
        return PAGE_W - self.ml - self.mr

    def add_page(self):
        self._ops = []
        self.pages.append(self._ops)
        self.page_no += 1
        self.y = PAGE_H - self.mt
        self.x = self.ml
        if self.on_new_page:
            self.on_new_page(self)

    def ensure(self, need):
        """Ensure `need` vertical points remain; else new page."""
        if self.y - need < self.mb:
            self.add_page()
            return True
        return False

    # -- low level ops ------------------------------------------------------
    def _op(self, s):
        self._ops.append(s)

    def raw_text(self, x, y, s, size, font=F_REG, color=BLACK):
        self._op("BT")
        self._op(f"{color.s()} rg")
        self._op(f"/{font} {size:.2f} Tf")
        self._op(f"1 0 0 1 {x:.2f} {y:.2f} Tm")
        self._op(f"({_enc(s)}) Tj")
        self._op("ET")

    def line(self, x1, y1, x2, y2, width=0.8, color=GREY, dash=None):
        self._op(f"{width:.2f} w")
        self._op(f"{color.s()} RG")
        if dash:
            self._op(f"[{dash}] 0 d")
        else:
            self._op("[] 0 d")
        self._op(f"{x1:.2f} {y1:.2f} m {x2:.2f} {y2:.2f} l S")
        self._op("[] 0 d")

    def rect(self, x, y, w, h, width=0.8, color=GREY):
        self._op(f"{width:.2f} w")
        self._op(f"{color.s()} RG")
        self._op(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re S")

    def fill_rect(self, x, y, w, h, color=LIGHT, border=None, bw=0.8):
        self._op(f"{color.s()} rg")
        if border:
            self._op(f"{border.s()} RG")
            self._op(f"{bw:.2f} w")
            self._op(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re B")
        else:
            self._op(f"{x:.2f} {y:.2f} {w:.2f} {h:.2f} re f")

    def polyline(self, pts, width=1.4, color=BLUE, dash=None):
        if len(pts) < 2:
            return
        self._op(f"{width:.2f} w")
        self._op(f"{color.s()} RG")
        if dash:
            self._op(f"[{dash}] 0 d")
        self._op(f"{pts[0][0]:.2f} {pts[0][1]:.2f} m")
        for px, py in pts[1:]:
            self._op(f"{px:.2f} {py:.2f} l")
        self._op("S")
        self._op("[] 0 d")

    # -- high level text ----------------------------------------------------
    def _wrap(self, text, size, bold, max_w):
        words = text.split(' ')
        lines = []
        cur = ''
        for w in words:
            trial = w if not cur else cur + ' ' + w
            if text_width(trial, size, bold) <= max_w or not cur:
                # handle a single word longer than the line
                if not cur and text_width(w, size, bold) > max_w:
                    lines.extend(self._hard_break(w, size, bold, max_w))
                    cur = ''
                else:
                    cur = trial
            else:
                lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def _hard_break(self, word, size, bold, max_w):
        out = []
        cur = ''
        for ch in word:
            if text_width(cur + ch, size, bold) <= max_w or not cur:
                cur += ch
            else:
                out.append(cur)
                cur = ch
        if cur:
            out.append(cur)
        return out

    def paragraph(self, text, size=10.5, font=F_REG, color=DARK,
                  leading=None, indent=0, gap_after=5, align='left',
                  x=None, max_w=None):
        bold = font in (F_BOLD, F_BI)
        if leading is None:
            leading = size * 1.34
        left = (x if x is not None else self.ml) + indent
        width = (max_w if max_w is not None else (self.content_w - indent))
        for para in text.split('\n'):
            lines = self._wrap(para, size, bold, width) if para else ['']
            for ln in lines:
                self.ensure(leading)
                if align == 'center':
                    lw = text_width(ln, size, bold)
                    tx = left + (width - lw) / 2
                elif align == 'right':
                    lw = text_width(ln, size, bold)
                    tx = left + (width - lw)
                else:
                    tx = left
                self.raw_text(tx, self.y - size, ln, size, font, color)
                self.y -= leading
        self.y -= gap_after

    def bullet(self, text, size=10.5, font=F_REG, color=DARK, indent=14,
               marker='\u2022', gap_after=3, label_font=None):
        bold = font in (F_BOLD, F_BI)
        leading = size * 1.34
        left = self.ml + indent
        width = self.content_w - indent
        lines = self._wrap(text, size, bold, width)
        for i, ln in enumerate(lines):
            self.ensure(leading)
            if i == 0:
                self.raw_text(self.ml + indent - 12, self.y - size, marker,
                              size, label_font or font, color)
            self.raw_text(left, self.y - size, ln, size, font, color)
            self.y -= leading
        self.y -= gap_after

    def heading(self, text, size=15, color=NAVY, gap_before=6, gap_after=6,
                font=F_BOLD, rule=False):
        self.y -= gap_before
        self.ensure(size * 1.4 + (6 if rule else 0))
        self.raw_text(self.ml, self.y - size, text, size, font, color)
        self.y -= size * 1.28
        if rule:
            self.y -= 2
            self.line(self.ml, self.y, PAGE_W - self.mr, self.y, 1.0, color)
            self.y -= 4
        self.y -= gap_after

    def hrule(self, color=LIGHT, width=0.8, gap=6):
        self.y -= gap
        self.ensure(2)
        self.line(self.ml, self.y, PAGE_W - self.mr, self.y, width, color)
        self.y -= gap

    def spacer(self, h=8):
        self.ensure(h)
        self.y -= h

    def move_to(self, y):
        self.y = y

    # -- a bordered callout box (draws text then frames it) -----------------
    def box(self, render_fn, pad=10, bg=BOXBG, border=BOXBORDER, gap_after=8):
        """render_fn(pdf) draws content; we frame it. Handles page breaks by
        simply drawing a left accent bar per page region isn't trivial, so we
        pre-measure by rendering into a scratch to know height is hard; instead
        we reserve using a simple approach: draw background after content only
        if it fits one page. For long content we fall back to an accent line."""
        start_y = self.y
        start_page = len(self.pages)
        self.y -= pad
        self.x = self.ml + pad
        render_fn(self)
        end_page = len(self.pages)
        end_y = self.y
        if start_page == end_page:
            top = start_y
            bottom = end_y - pad + 4
            # draw box behind: since content already drawn, draw border only
            self.rect(self.ml + 2, bottom, self.content_w - 4, top - bottom,
                      1.0, border)
        self.x = self.ml
        self.y = end_y - pad
        self.y -= gap_after

    # -- table --------------------------------------------------------------
    def table(self, headers, rows, col_w=None, size=9.5, header_bg=NAVY,
              header_fg=Color(1, 1, 1), align=None, gap_after=10,
              row_h=None, zebra=True):
        n = len(headers)
        total = self.content_w
        if col_w is None:
            col_w = [total / n] * n
        else:
            s = sum(col_w)
            col_w = [w * total / s for w in col_w]
        if align is None:
            align = ['left'] * n
        pad = 4
        line_h = size * 1.28

        def cell_lines(txt, w, bold):
            return self._wrap(str(txt), size, bold, w - 2 * pad)

        def draw_row(cells, bold, fg, bg=None):
            wrapped = [cell_lines(c, col_w[i], bold) for i, c in enumerate(cells)]
            h = max(len(wl) for wl in wrapped) * line_h + 2 * pad * 0.6
            if row_h:
                h = max(h, row_h)
            self.ensure(h)
            top = self.y
            if bg:
                self.fill_rect(self.ml, top - h, total, h, bg)
            # vertical/horizontal border
            x = self.ml
            for i in range(n):
                cy = top - pad * 0.6 - size
                for ln in wrapped[i]:
                    if align[i] == 'center':
                        tx = x + (col_w[i] - text_width(ln, size, bold)) / 2
                    elif align[i] == 'right':
                        tx = x + col_w[i] - pad - text_width(ln, size, bold)
                    else:
                        tx = x + pad
                    self.raw_text(tx, cy, ln, size, F_BOLD if bold else F_REG, fg)
                    cy -= line_h
                x += col_w[i]
            # grid
            self.line(self.ml, top - h, self.ml + total, top - h, 0.5, LIGHT)
            self.y = top - h
            return h

        # header
        self.ensure(line_h + 8)
        draw_row(headers, True, header_fg, header_bg)
        for ri, r in enumerate(rows):
            bg = LIGHTER if (zebra and ri % 2 == 1) else None
            draw_row(r, False, DARK, bg)
        # outer frame
        self.y -= gap_after

    # -- output -------------------------------------------------------------
    def save(self, path):
        objs = []

        def add(obj):
            objs.append(obj)
            return len(objs)  # 1-based id

        # Fonts
        font_defs = [
            ('F1', 'Helvetica'), ('F2', 'Helvetica-Bold'),
            ('F3', 'Helvetica-Oblique'), ('F4', 'Helvetica-BoldOblique'),
        ]
        font_ids = {}
        for name, base in font_defs:
            fid = add(f"<< /Type /Font /Subtype /Type1 /BaseFont /{base} "
                      f"/Encoding /WinAnsiEncoding >>")
            font_ids[name] = fid

        res_fonts = ' '.join(f"/{n} {font_ids[n]} 0 R" for n, _ in font_defs)
        resources = f"<< /Font << {res_fonts} >> >>"

        # Reserve pages parent id
        pages_id = len(objs) + 1 + 2 * len(self.pages) + 1  # placeholder recalc
        # We'll build content + page objects, then pages tree, then catalog.
        content_ids = []
        for ops in self.pages:
            stream = "\n".join(ops).encode('latin-1', 'replace')
            cid = add((stream, True))  # mark as stream
            content_ids.append(cid)

        page_ids = []
        # we need pages_id known; compute after we know count
        pages_obj_index = None
        # placeholder for pages tree object id
        pages_tree_id = len(objs) + len(self.pages) + 1
        for cid in content_ids:
            pid = add(f"<< /Type /Page /Parent {pages_tree_id} 0 R "
                      f"/MediaBox [0 0 {PAGE_W:.2f} {PAGE_H:.2f}] "
                      f"/Resources {resources} /Contents {cid} 0 R >>")
            page_ids.append(pid)

        kids = ' '.join(f"{pid} 0 R" for pid in page_ids)
        pages_tree_actual = add(f"<< /Type /Pages /Kids [{kids}] "
                                f"/Count {len(page_ids)} >>")
        assert pages_tree_actual == pages_tree_id, (pages_tree_actual, pages_tree_id)
        catalog_id = add(f"<< /Type /Catalog /Pages {pages_tree_id} 0 R >>")

        # Serialize
        out = bytearray()
        out += b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
        offsets = [0] * (len(objs) + 1)
        for i, obj in enumerate(objs, start=1):
            offsets[i] = len(out)
            out += f"{i} 0 obj\n".encode('latin-1')
            if isinstance(obj, tuple) and obj[1] is True:
                stream = obj[0]
                out += f"<< /Length {len(stream)} >>\nstream\n".encode('latin-1')
                out += stream
                out += b"\nendstream\n"
            else:
                out += obj.encode('latin-1')
                out += b"\n"
            out += b"endobj\n"

        xref_pos = len(out)
        n = len(objs) + 1
        out += f"xref\n0 {n}\n".encode('latin-1')
        out += b"0000000000 65535 f \n"
        for i in range(1, n):
            out += f"{offsets[i]:010d} 00000 n \n".encode('latin-1')
        out += b"trailer\n"
        out += f"<< /Size {n} /Root {catalog_id} 0 R >>\n".encode('latin-1')
        out += b"startxref\n"
        out += f"{xref_pos}\n".encode('latin-1')
        out += b"%%EOF\n"

        with open(path, 'wb') as f:
            f.write(out)
        return len(self.pages)
