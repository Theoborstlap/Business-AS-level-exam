"""Reusable business diagrams drawn as vector graphics on a PDF page.

Each function reserves vertical space, draws within the content width, and
advances the cursor. They gracefully page-break before drawing.
"""
from pdfgen import (PDF, F_REG, F_BOLD, F_OBL, BLACK, DARK, GREY, LIGHT,
                    LIGHTER, NAVY, BLUE, RED, GREEN, MAROON, Color,
                    text_width, PAGE_W)

AXIS = Color(0.2, 0.2, 0.2)
GRID = Color(0.85, 0.85, 0.85)


def _caption(pdf, text):
    pdf.spacer(2)
    pdf.paragraph(text, size=8.8, font=F_OBL, color=GREY, align='center',
                  gap_after=6)


def _frame_start(pdf, height):
    pdf.spacer(6)
    pdf.ensure(height + 8)


def breakeven(pdf, caption="Fig: Break-even chart", h=210,
              tc_label="Total costs", tr_label="Total revenue",
              fc_label="Fixed costs", be_label="Break-even point"):
    _frame_start(pdf, h)
    left = pdf.ml + 42
    right = PAGE_W - pdf.mr - 60
    top = pdf.y - 10
    bottom = pdf.y - h + 26
    # axes
    pdf.line(left, top, left, bottom, 1.1, AXIS)
    pdf.line(left, bottom, right, bottom, 1.1, AXIS)
    # fixed cost line
    fc_y = bottom + (top - bottom) * 0.22
    pdf.line(left, fc_y, right, fc_y, 1.3, GREEN)
    # total cost line (from fc_y intercept up)
    tc_end = bottom + (top - bottom) * 0.78
    pdf.polyline([(left, fc_y), (right, tc_end)], 1.5, RED)
    # total revenue line from origin
    tr_end = bottom + (top - bottom) * 0.95
    pdf.polyline([(left, bottom), (right, tr_end)], 1.5, BLUE)
    # break-even where TR meets TC: solve intersection
    # TR: y=bottom + t*(tr_end-bottom); TC: y=fc_y + t*(tc_end-fc_y)
    import_slope_tr = (tr_end - bottom)
    import_slope_tc = (tc_end - fc_y)
    denom = (import_slope_tr - import_slope_tc)
    t = (fc_y - bottom) / denom if denom else 0.5
    bex = left + t * (right - left)
    bey = bottom + t * import_slope_tr
    pdf.line(bex, bottom, bex, bey, 0.7, GREY, dash="2 2")
    pdf.line(left, bey, bex, bey, 0.7, GREY, dash="2 2")
    # marker
    pdf.fill_rect(bex - 2.2, bey - 2.2, 4.4, 4.4, MAROON)
    # labels
    pdf.raw_text(right - 4 - text_width(tr_label, 8.5), tr_end + 3, tr_label, 8.5, F_BOLD, BLUE)
    pdf.raw_text(right - 4 - text_width(tc_label, 8.5), tc_end - 10, tc_label, 8.5, F_BOLD, RED)
    pdf.raw_text(left + 4, fc_y + 3, fc_label, 8.5, F_BOLD, GREEN)
    pdf.raw_text(bex + 4, bey + 6, be_label, 8.2, F_BOLD, MAROON)
    # axis titles
    pdf.raw_text(right - 70, bottom - 12, "Output (units)", 8.5, F_OBL, DARK)
    pdf.raw_text(left - 34, top - 4, "Costs /", 8.0, F_OBL, DARK)
    pdf.raw_text(left - 34, top - 13, "Revenue", 8.0, F_OBL, DARK)
    pdf.raw_text(left - 34, top - 22, "(\u00a3)", 8.0, F_OBL, DARK)
    pdf.y = bottom - 16
    _caption(pdf, caption)


def product_life_cycle(pdf, caption="Fig: Product life cycle", h=200):
    _frame_start(pdf, h)
    left = pdf.ml + 34
    right = PAGE_W - pdf.mr - 20
    top = pdf.y - 10
    bottom = pdf.y - h + 30
    pdf.line(left, top, left, bottom, 1.1, AXIS)
    pdf.line(left, bottom, right, bottom, 1.1, AXIS)
    span = right - left
    # sales curve points
    pts = [
        (left, bottom + 3),
        (left + span * 0.14, bottom + (top - bottom) * 0.10),
        (left + span * 0.34, bottom + (top - bottom) * 0.55),
        (left + span * 0.55, bottom + (top - bottom) * 0.86),
        (left + span * 0.74, bottom + (top - bottom) * 0.88),
        (left + span * 0.90, bottom + (top - bottom) * 0.58),
        (right - 4, bottom + (top - bottom) * 0.34),
    ]
    pdf.polyline(pts, 1.7, BLUE)
    stages = [("Devel.", 0.02, 0.14), ("Introduction", 0.14, 0.30),
              ("Growth", 0.30, 0.52), ("Maturity", 0.52, 0.80),
              ("Decline", 0.80, 0.99)]
    for name, a, b in stages:
        xx = left + span * a
        pdf.line(xx, bottom, xx, top, 0.5, GRID, dash="2 2")
        mid = left + span * ((a + b) / 2)
        pdf.raw_text(mid - text_width(name, 7.8) / 2, bottom - 12, name, 7.8, F_BOLD, DARK)
    pdf.raw_text(left - 26, top - 4, "Sales", 8.0, F_OBL, DARK)
    pdf.raw_text(right - 44, bottom - 22, "Time", 8.5, F_OBL, DARK)
    pdf.y = bottom - 26
    _caption(pdf, caption)


def boston_matrix(pdf, caption="Fig: Boston Matrix", h=210):
    _frame_start(pdf, h)
    size = min(h - 30, pdf.content_w - 120)
    left = pdf.ml + 60
    top = pdf.y - 6
    bottom = top - size
    right = left + size
    midx = (left + right) / 2
    midy = (top + bottom) / 2
    pdf.rect(left, bottom, size, size, 1.0, AXIS)
    pdf.line(midx, bottom, midx, top, 0.8, GREY)
    pdf.line(left, midy, right, midy, 0.8, GREY)
    quad = [("Star", left, top, midx, midy, GREEN),
            ("Question Mark", midx, top, right, midy, Color(0.8, 0.6, 0.1)),
            ("Cash Cow", left, midy, midx, bottom, BLUE),
            ("Dog", midx, midy, right, bottom, RED)]
    for name, x1, y1, x2, y2, col in quad:
        cx = (x1 + x2) / 2
        cy = (y1 + y2) / 2
        pdf.raw_text(cx - text_width(name, 9.5, True) / 2, cy - 3, name, 9.5, F_BOLD, col)
    # axis labels
    pdf.raw_text(left - 44, top - 2, "High", 8, F_OBL, DARK)
    pdf.raw_text(left - 44, bottom + 6, "Low", 8, F_OBL, DARK)
    pdf.raw_text(left - 52, midy + 30, "Market", 8, F_OBL, DARK)
    pdf.raw_text(left - 52, midy + 21, "growth", 8, F_OBL, DARK)
    pdf.raw_text(left + 2, bottom - 12, "High", 8, F_OBL, DARK)
    pdf.raw_text(right - text_width("Low", 8), bottom - 12, "Low", 8, F_OBL, DARK)
    lbl = "Relative market share"
    pdf.raw_text(midx - text_width(lbl, 8) / 2, bottom - 22, lbl, 8, F_OBL, DARK)
    pdf.y = bottom - 28
    _caption(pdf, caption)


def inventory_chart(pdf, caption="Fig: Inventory control chart", h=200):
    _frame_start(pdf, h)
    left = pdf.ml + 40
    right = PAGE_W - pdf.mr - 20
    top = pdf.y - 10
    bottom = pdf.y - h + 30
    pdf.line(left, top, left, bottom, 1.1, AXIS)
    pdf.line(left, bottom, right, bottom, 1.1, AXIS)
    span = right - left
    height = top - bottom
    maxlvl = bottom + height * 0.9
    reorder = bottom + height * 0.5
    buffer = bottom + height * 0.2
    # sawtooth
    pts = [(left, maxlvl)]
    cycles = 3
    for c in range(cycles):
        x0 = left + span * (c / cycles)
        x1 = left + span * ((c + 0.75) / cycles)
        x2 = left + span * ((c + 1) / cycles)
        pts.append((x1, buffer))
        pts.append((x2, maxlvl))
    pdf.polyline(pts, 1.5, BLUE)
    # reference lines
    pdf.line(left, maxlvl, right, maxlvl, 0.7, GREEN, dash="3 2")
    pdf.line(left, reorder, right, reorder, 0.7, Color(0.8, 0.6, 0.1), dash="3 2")
    pdf.line(left, buffer, right, buffer, 0.7, RED, dash="3 2")
    pdf.raw_text(right - text_width("Maximum inventory", 7.8) - 2, maxlvl + 3, "Maximum inventory", 7.8, F_BOLD, GREEN)
    pdf.raw_text(right - text_width("Re-order level", 7.8) - 2, reorder + 3, "Re-order level", 7.8, F_BOLD, Color(0.8, 0.6, 0.1))
    pdf.raw_text(right - text_width("Buffer inventory", 7.8) - 2, buffer + 3, "Buffer inventory", 7.8, F_BOLD, RED)
    pdf.raw_text(left - 30, top - 4, "Inventory", 7.6, F_OBL, DARK)
    pdf.raw_text(left - 30, top - 13, "level", 7.6, F_OBL, DARK)
    pdf.raw_text(right - 34, bottom - 12, "Time", 8.5, F_OBL, DARK)
    pdf.y = bottom - 16
    _caption(pdf, caption)


def demand_supply(pdf, caption="Fig: Demand and supply", h=200):
    _frame_start(pdf, h)
    left = pdf.ml + 40
    right = PAGE_W - pdf.mr - 30
    top = pdf.y - 10
    bottom = pdf.y - h + 26
    pdf.line(left, top, left, bottom, 1.1, AXIS)
    pdf.line(left, bottom, right, bottom, 1.1, AXIS)
    # demand (down slope), supply (up slope)
    pdf.polyline([(left, top - 6), (right, bottom + 12)], 1.5, RED)
    pdf.polyline([(left, bottom + 6), (right, top - 12)], 1.5, BLUE)
    # equilibrium approx centre
    ex = (left + right) / 2
    ey = (top + bottom) / 2
    pdf.line(left, ey, ex, ey, 0.6, GREY, dash="2 2")
    pdf.line(ex, bottom, ex, ey, 0.6, GREY, dash="2 2")
    pdf.fill_rect(ex - 2, ey - 2, 4, 4, MAROON)
    pdf.raw_text(right - text_width("Demand", 8.5) - 2, bottom + 10, "Demand", 8.5, F_BOLD, RED)
    pdf.raw_text(right - text_width("Supply", 8.5) - 2, top - 14, "Supply", 8.5, F_BOLD, BLUE)
    pdf.raw_text(left - 28, top - 4, "Price", 8, F_OBL, DARK)
    pdf.raw_text(left + 2, ey + 3, "P", 8.5, F_BOLD, MAROON)
    pdf.raw_text(right - 60, bottom - 12, "Quantity", 8.5, F_OBL, DARK)
    pdf.y = bottom - 16
    _caption(pdf, caption)


def org_chart(pdf, caption="Fig: Organisation structure", h=190):
    _frame_start(pdf, h)
    cx = (pdf.ml + PAGE_W - pdf.mr) / 2
    top = pdf.y - 6
    bw, bh = 120, 26
    gap = 20

    def cell(x, y, label, col=NAVY):
        pdf.fill_rect(x - bw / 2, y - bh, bw, bh, Color(0.93, 0.95, 0.99), border=col, bw=1.0)
        pdf.raw_text(x - text_width(label, 8.6, True) / 2, y - bh + 8, label, 8.6, F_BOLD, col)

    # tier 1
    cell(cx, top, "Managing Director")
    y2 = top - bh - gap
    xs = [cx - 150, cx, cx + 150]
    labels2 = ["Marketing Dir.", "Operations Dir.", "Finance Dir."]
    # connectors
    pdf.line(cx, top - bh, cx, y2 + 6, 0.8, GREY)
    pdf.line(xs[0], y2 + 6, xs[2], y2 + 6, 0.8, GREY)
    for x, lb in zip(xs, labels2):
        pdf.line(x, y2 + 6, x, y2, 0.8, GREY)
        cell(x, y2, lb, MAROON)
    y3 = y2 - bh - gap
    for x in xs:
        pdf.line(x, y2 - bh, x, y3 + 6, 0.8, GREY)
        pdf.line(x - 40, y3 + 6, x + 40, y3 + 6, 0.8, GREY)
        for dx in (-40, 40):
            pdf.line(x + dx, y3 + 6, x + dx, y3, 0.8, GREY)
            pdf.fill_rect(x + dx - 34, y3 - bh, 68, bh, Color(0.97, 0.97, 0.97), border=GREY, bw=0.7)
    pdf.raw_text(cx - text_width("Supervisors & operational staff", 8) / 2, y3 - bh + 9,
                 "Supervisors & operational staff", 8, F_OBL, DARK)
    pdf.y = y3 - bh - 6
    _caption(pdf, caption)


def capacity_bar(pdf, caption="Fig: Capacity utilisation", h=170,
                 series=None):
    _frame_start(pdf, h)
    if series is None:
        series = [("2023", 62), ("2024", 78), ("2025", 91)]
    left = pdf.ml + 40
    right = PAGE_W - pdf.mr - 30
    top = pdf.y - 10
    bottom = pdf.y - h + 30
    pdf.line(left, top, left, bottom, 1.1, AXIS)
    pdf.line(left, bottom, right, bottom, 1.1, AXIS)
    n = len(series)
    slot = (right - left) / n
    bw = slot * 0.5
    for i, (lab, val) in enumerate(series):
        bx = left + slot * i + (slot - bw) / 2
        bh = (top - bottom) * (val / 100.0)
        pdf.fill_rect(bx, bottom, bw, bh, BLUE)
        pdf.raw_text(bx + bw / 2 - text_width(f"{val}%", 8) / 2, bottom + bh + 3, f"{val}%", 8, F_BOLD, NAVY)
        pdf.raw_text(bx + bw / 2 - text_width(lab, 8) / 2, bottom - 12, lab, 8, F_REG, DARK)
    pdf.raw_text(left - 30, top - 4, "% used", 7.6, F_OBL, DARK)
    pdf.y = bottom - 16
    _caption(pdf, caption)


DIAGRAM_FUNCS = {
    'breakeven': breakeven,
    'plc': product_life_cycle,
    'boston': boston_matrix,
    'inventory': inventory_chart,
    'demand_supply': demand_supply,
    'org_chart': org_chart,
    'capacity': capacity_bar,
}


def draw(pdf, name, **kwargs):
    fn = DIAGRAM_FUNCS.get(name)
    if fn:
        fn(pdf, **kwargs)
