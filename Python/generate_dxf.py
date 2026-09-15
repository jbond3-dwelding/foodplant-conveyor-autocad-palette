#!/usr/bin/env python3
"""Generate AutoCAD R12 DXF symbols for food-plant sanitary conveyors.
No third-party packages required. Units: inches. Insertion: infeed CL at 0,0.
Usage: python generate_dxf.py [outdir]
"""
from pathlib import Path
import sys

LAYERS = [
    ("0", 7, "CONTINUOUS"),
    ("Q-CONV-BELT", 4, "CONTINUOUS"),
    ("Q-CONV-FRAM", 7, "CONTINUOUS"),
    ("Q-CONV-SUPP", 8, "CONTINUOUS"),
    ("Q-CONV-DRIV", 1, "CONTINUOUS"),
    ("Q-CONV-XFER", 6, "CONTINUOUS"),
    ("Q-CONV-SANI", 3, "HIDDEN"),
    ("Q-CONV-GUID", 2, "CONTINUOUS"),
    ("Q-CONV-CNTR", 2, "CENTER"),
    ("Q-CONV-FLOW", 1, "CONTINUOUS"),
    ("Q-CONV-ANNO", 7, "CONTINUOUS"),
    ("Q-CONV-HIDD", 8, "HIDDEN"),
    ("Q-CONV-CLR", 8, "PHANTOM"),
    ("Q-EQPM-INSP", 5, "CONTINUOUS"),
]


def header():
    s = (
        "  0\nSECTION\n  2\nHEADER\n  9\n$ACADVER\n  1\nAC1009\n"
        "  9\n$INSUNITS\n 70\n1\n  9\n$INSBASE\n 10\n0.0\n 20\n0.0\n 30\n0.0\n"
        "  0\nENDSEC\n  0\nSECTION\n  2\nTABLES\n  0\nTABLE\n  2\nLTYPE\n 70\n4\n"
        "  0\nLTYPE\n  2\nCONTINUOUS\n 70\n0\n  3\nSolid line\n 72\n65\n 73\n0\n 40\n0.0\n"
        "  0\nLTYPE\n  2\nCENTER\n 70\n0\n  3\nCenter\n 72\n65\n 73\n4\n 40\n2.0\n"
        " 49\n1.25\n 74\n0\n 49\n-0.25\n 74\n0\n 49\n0.25\n 74\n0\n 49\n-0.25\n 74\n0\n"
        "  0\nLTYPE\n  2\nHIDDEN\n 70\n0\n  3\nHidden\n 72\n65\n 73\n2\n 40\n0.375\n"
        " 49\n0.25\n 74\n0\n 49\n-0.125\n 74\n0\n"
        "  0\nLTYPE\n  2\nPHANTOM\n 70\n0\n  3\nPhantom\n 72\n65\n 73\n6\n 40\n2.5\n"
        " 49\n1.25\n 74\n0\n 49\n-0.25\n 74\n0\n 49\n0.25\n 74\n0\n"
        " 49\n-0.25\n 74\n0\n 49\n0.25\n 74\n0\n 49\n-0.25\n 74\n0\n"
        "  0\nENDTAB\n  0\nTABLE\n  2\nLAYER\n 70\n20\n"
    )
    for n, c, lt in LAYERS:
        s += f"  0\nLAYER\n  2\n{n}\n 70\n0\n 62\n{c}\n  6\n{lt}\n"
    s += "  0\nENDTAB\n  0\nENDSEC\n  0\nSECTION\n  2\nENTITIES\n"
    return s


def footer():
    return "  0\nENDSEC\n  0\nEOF\n"


def line(x1, y1, x2, y2, layer="0"):
    return (
        f"  0\nLINE\n  8\n{layer}\n 10\n{x1:.4f}\n 20\n{y1:.4f}\n 30\n0.0\n"
        f" 11\n{x2:.4f}\n 21\n{y2:.4f}\n 31\n0.0\n"
    )


def circ(cx, cy, r, layer="0"):
    return (
        f"  0\nCIRCLE\n  8\n{layer}\n 10\n{cx:.4f}\n 20\n{cy:.4f}\n 30\n0.0\n"
        f" 40\n{r:.4f}\n"
    )


def text(x, y, h, s, layer="0"):
    return (
        f"  0\nTEXT\n  8\n{layer}\n 10\n{x:.4f}\n 20\n{y:.4f}\n 30\n0.0\n"
        f" 40\n{h:.4f}\n  1\n{s}\n"
    )


def solid(p1, p2, p3, layer="0"):
    return (
        f"  0\nSOLID\n  8\n{layer}\n"
        f" 10\n{p1[0]:.4f}\n 20\n{p1[1]:.4f}\n 30\n0.0\n"
        f" 11\n{p2[0]:.4f}\n 21\n{p2[1]:.4f}\n 31\n0.0\n"
        f" 12\n{p3[0]:.4f}\n 22\n{p3[1]:.4f}\n 32\n0.0\n"
        f" 13\n{p3[0]:.4f}\n 23\n{p3[1]:.4f}\n 33\n0.0\n"
    )


def rect(x, y, w, h, layer="0"):
    return (
        line(x, y, x + w, y, layer)
        + line(x + w, y, x + w, y + h, layer)
        + line(x + w, y + h, x, y + h, layer)
        + line(x, y + h, x, y, layer)
    )


def belt_plan(W=24, L=96):
    ow, y0 = W + 4.0, -(W + 4.0) / 2
    e = [
        rect(0, y0, L, ow, "Q-CONV-FRAM"),
        rect(0, -W / 2, L, W, "Q-CONV-BELT"),
        line(-6, 0, L + 6, 0, "Q-CONV-CNTR"),
        rect(-1, y0 - 1, L + 2, ow + 2, "Q-CONV-SANI"),
        line(0, -W / 2 - 0.75, L, -W / 2 - 0.75, "Q-CONV-GUID"),
        line(0, W / 2 + 0.75, L, W / 2 + 0.75, "Q-CONV-GUID"),
        rect(L - 4, y0, 4, ow, "Q-CONV-DRIV"),
        solid((L, 0), (L - 6, 1.5), (L - 6, -1.5), "Q-CONV-FLOW"),
        solid((L / 2, 0), (L / 2 - 6, 1.5), (L / 2 - 6, -1.5), "Q-CONV-FLOW"),
        text(L - 3.6, -1.2, 1.25, "DR", "Q-CONV-ANNO"),
        text(0.3, y0 - 2.2, 1.0, "TU", "Q-CONV-ANNO"),
        text(L / 2 - 8, ow / 2 + 3.5, 1.5, f"{W:.0f} BELT x {L:.0f}", "Q-CONV-ANNO"),
        text(L / 2 - 8, ow / 2 + 5.5, 1.1, "SANITARY 304 SS", "Q-CONV-ANNO"),
    ]
    x = 12.0
    while x <= L - 12:
        e.append(rect(x - 1, y0 - 1, 2, 2, "Q-CONV-SUPP"))
        e.append(rect(x - 1, y0 + ow - 1, 2, 2, "Q-CONV-SUPP"))
        x += 60.0
    return "".join(e)


def belt_elev(W=24, L=96, tob=36):
    rail, e, x = 3.5, [], 12.0
    e += [
        line(0, tob, L, tob, "Q-CONV-BELT"),
        rect(0, tob - rail, L, rail, "Q-CONV-FRAM"),
        line(0, tob - rail - 5, L, tob - rail - 5, "Q-CONV-HIDD"),
        rect(L - 10, tob - rail - 8, 10, 8, "Q-CONV-DRIV"),
        circ(L - 3, tob - rail / 2, 2.5, "Q-CONV-DRIV"),
        circ(3, tob - rail / 2, 1.75, "Q-CONV-FRAM"),
        rect(-1, tob - rail - 12, L + 2, 2, "Q-CONV-SANI"),
        line(-6, 0, L + 6, 0, "Q-CONV-ANNO"),
        text(-4, 1.5, 1.25, "FFL", "Q-CONV-ANNO"),
        text(4, tob + 1.5, 1.25, f"TOB {tob:.0f}\", "Q-CONV-ANNO"),
        text(L / 2 - 6, tob + 3.5, 1.25, f"{W:.0f} SANITARY BELT", "Q-CONV-ANNO"),
    ]
    while x <= L - 12:
        e += [
            line(x, 0, x, tob - rail, "Q-CONV-SUPP"),
            line(x - 6, 0, x + 6, 0, "Q-CONV-SUPP"),
            circ(x, 0, 1.0, "Q-CONV-SUPP"),
        ]
        x += 60.0
    return "".join(e)


def screw_plan(dia=6, L=96):
    r, e, x, pitch = dia / 2 + 0.5, [], 0.0, dia
    e += [
        rect(0, -r, L, 2 * r, "Q-CONV-FRAM"),
        line(-4, 0, L + 4, 0, "Q-CONV-CNTR"),
        circ(L + 3, 0, 4, "Q-CONV-DRIV"),
        rect(8, 4, 10, 8, "Q-CONV-FRAM"),
        text(9, 12.5, 1.1, "HOPPER", "Q-CONV-ANNO"),
        circ(L - 8, 0, 1.5, "Q-CONV-XFER"),
        text(2, -r - 3, 1.2, f"SCR {dia:.0f}\" TUBULAR SANITARY", "Q-CONV-ANNO"),
    ]
    while x < L:
        e.append(line(x, -r + 0.2, min(x + pitch / 2, L), r - 0.2, "Q-CONV-BELT"))
        x += pitch / 2
    return "".join(e)


def stand(h=36):
    return "".join([
        line(-8, 0, 8, 0, "Q-CONV-SUPP"),
        circ(-6, 0, 1, "Q-CONV-SUPP"), circ(6, 0, 1, "Q-CONV-SUPP"),
        line(-6, 0, -6, 4, "Q-CONV-SUPP"), line(6, 0, 6, 4, "Q-CONV-SUPP"),
        line(-6, 4, 6, 4, "Q-CONV-SUPP"), line(0, 4, 0, h, "Q-CONV-SUPP"),
        line(-10, h, 10, h, "Q-CONV-FRAM"),
        text(-7, h + 1.5, 1.2, f"H-STAND TOB {h}\", "Q-CONV-ANNO"),
    ])


def nose(W=24):
    return "".join([
        circ(0, 0, 0.5, "Q-CONV-XFER"),
        line(-4, -W / 2 - 2, 2, -W / 2 - 2, "Q-CONV-FRAM"),
        line(-4, W / 2 + 2, 2, W / 2 + 2, "Q-CONV-FRAM"),
        line(-4, -W / 2 - 2, -4, W / 2 + 2, "Q-CONV-FRAM"),
        text(-3, W / 2 + 3.5, 1.1, f"NOSE BAR {W}\", "Q-CONV-ANNO"),
    ])


def md(W=18):
    return "".join([
        rect(0, -W / 2 - 6, 30, W + 12, "Q-EQPM-INSP"),
        rect(4, -W / 2 - 2, 22, W + 4, "Q-EQPM-INSP"),
        line(-6, 0, 36, 0, "Q-CONV-CNTR"),
        text(6, W / 2 + 8, 1.4, f"METAL DETECTOR {W}\", "Q-CONV-ANNO"),
        rect(32, -8, 10, 16, "Q-CONV-XFER"),
        text(33, 9, 1.1, "REJECT", "Q-CONV-ANNO"),
    ])


def flow():
    return "".join([
        line(0, 0, 18, 0, "Q-CONV-FLOW"),
        solid((18, 0), (12, 2.5), (12, -2.5), "Q-CONV-FLOW"),
        text(4, 3.5, 1.25, "PRODUCT FLOW", "Q-CONV-ANNO"),
    ])


def legend():
    rows = [
        (32, "L1 DRY / PACKAGED     painted or bolted 304  IP54-IP65"),
        (26, "L2 LIGHT WASH         bolted 304 #4          IP65-IP66"),
        (20, "L3 WASHDOWN           welded 304 open frame  IP66"),
        (14, "L4 SANITARY / CIP     304/316 32uin Ra       IP69K"),
        (8, "L5 3-A / USDA         continuous weld + COP  raw protein/dairy"),
    ]
    e = [
        rect(0, 0, 70, 42, "Q-CONV-ANNO"),
        text(2, 38, 2.0, "FOOD PLANT CONVEYOR HYGIENE LEGEND", "Q-CONV-ANNO"),
        text(3, 3, 1.0, "Generic sanitary classes for layout only.", "Q-CONV-ANNO"),
    ]
    for y, t in rows:
        e.append(text(3, y, 1.4, t, "Q-CONV-ANNO"))
    return "".join(e)


def main():
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "Dxf"
    out.mkdir(parents=True, exist_ok=True)
    files = {}
    for w in (6, 8, 12, 18, 24, 36, 48):
        files[f"FP-CONV-BELT-PLN-{w:02d}.dxf"] = belt_plan(w, 96)
        files[f"FP-CONV-BELT-ELV-{w:02d}.dxf"] = belt_elev(w, 96, 36)
        files[f"FP-CONV-MOD-PLN-{w:02d}.dxf"] = belt_plan(w, 96)
    for d in (4, 6, 9, 12, 16):
        files[f"FP-CONV-SCRW-PLN-{d:02d}.dxf"] = screw_plan(d, 96)
    for h in (22, 30, 36, 42, 48):
        files[f"FP-CONV-STD-H-{h}.dxf"] = stand(h)
    files["FP-CONV-XFR-NOSE-24.dxf"] = nose(24)
    files["FP-CONV-QC-MD-18.dxf"] = md(18)
    files["FP-CONV-ANNO-FLOW.dxf"] = flow()
    files["FP-CONV-LGND-HYG.dxf"] = legend()
    for name, ents in files.items():
        (out / name).write_text(header() + ents + footer(), encoding="utf-8")
        print("wrote", out / name)


if __name__ == "__main__":
    main()
