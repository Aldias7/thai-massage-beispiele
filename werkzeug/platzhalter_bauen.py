"""Zeichnet alle Platzhalterbilder der drei Entwürfe als SVG (eigene Grafik, ohne Personen).

Aufruf (im Projektordner thai-massage):  ..\\.venv\\Scripts\\python.exe werkzeug\\platzhalter_bauen.py
Die Dateien landen in beispiel-N/bilder/. Die Seitenverhältnisse stehen im Namen der Funktionen
und in den width/height-Werten der <img>-Tags, damit ein echtes Foto 1:1 passt.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from platzhalter_lib import *  # noqa

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def save(sub, name, content):
    d = os.path.join(ROOT, sub, "bilder")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def orchid(x, y, r, c1, c2, c3, core, stroke=None, rot=0):
    o = ""
    for a in (0, 130, -130):
        o += petal(x, y, r * .82, r * .34, a + rot, c1, 1, stroke, 2)
    for a in (-78, 78):
        o += petal(x, y, r * .95, r * .55, a + rot, c2, 1, stroke, 2)
    o += petal(x, y, r * .5, r * .26, 180 + rot, c3, 1, stroke, 2)
    o += f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r * .1)}" fill="{core}"/>'
    return o


def stem(d, color, w):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round"/>'


# =====================================================================
# Entwurf 1: dunkel, Salbei, Nacht am Wasser
# =====================================================================
BG, BG2, MID, DEEP = "#1a1c1a", "#222622", "#2f342e", "#3d4a3e"
S3, S1, S2, PALE, GLOW = "#5f7660", "#8fa68e", "#a6bca5", "#c8c5ba", "#e6c48f"


def e1_hero():  # 3:2
    w, h = 1500, 1000
    defs = (lin("sky", "#0e110e", "#27322b", y2=.62) + lin("wat", "#1d261f", "#0d100d") + rad("mg", "#cfe0cb", .55)
            + rad("gl", GLOW, .8))
    b = f'<rect width="{w}" height="{h}" fill="url(#sky)"/>'
    b += sparkles(w, h, 70, "#dfe9db", 11, 1, 2.6, .8, ymax=520)
    b += f'<circle cx="750" cy="330" r="470" fill="url(#mg)"/>'
    b += f'<circle cx="750" cy="330" r="172" fill="#dce4d4" fill-opacity=".93"/>'
    b += hills(w, 585, 34, "#1c2620", 3, base=700) + hills(w, 612, 24, "#141a16", 5, base=700, f1=1.4)
    b += f'<rect y="628" width="{w}" height="{h - 628}" fill="url(#wat)"/>'
    for i, (wd, op) in enumerate(((280, .34), (230, .30), (180, .26), (130, .22), (84, .2), (40, .18))):
        b += f'<rect x="{n(750 - wd)}" y="{n(646 + i * 21)}" width="{n(wd * 2)}" height="6" rx="3" fill="#dce4d4" fill-opacity="{op}"/>'
    b += ripples(750, 760, 520, 4, S2, .5)
    for x, y, rx, a in ((300, 800, 150, 8), (1190, 760, 130, -6), (1060, 900, 200, 4), (470, 905, 170, -10), (150, 700, 90, 3), (1380, 840, 120, 0)):
        b += padlily(x, y, rx, "#25362b", a)
    b += lotus(750, 735, 320, "#4f6c57", "#86a58b", "#d3e4cc", GLOW)
    b += tealight(330, 868, 34, PALE) + tealight(1160, 830, 28, PALE) + tealight(1330, 900, 24, PALE)
    return svg(w, h, defs, b, .12, "#fff")


def e1_farn():  # 4:5
    w, h = 1000, 1250
    defs = lin("bg", "#2b332d", BG) + rad("mg", "#cfe0cb", .45)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += sparkles(w, h, 40, "#dfe9db", 4, 1, 2.2, .7, ymax=650)
    b += f'<circle cx="500" cy="450" r="400" fill="url(#mg)"/><circle cx="500" cy="450" r="215" fill="#cdd8c5" fill-opacity=".24"/>'
    b += frond(930, 1290, 980, -4, -.5, "#334439", "#4c6150", 17)
    b += frond(80, 1290, 1020, 5, .48, "#3e5244", S3, 17)
    b += frond(250, 1290, 760, 20, .5, "#566e5a", S1, 15)
    b += frond(780, 1290, 700, -22, -.5, "#4b6350", S1, 14)
    b += stem("M500 1250C470 1010 545 830 500 690", S3, 9)
    b += petal(500, 700, 210, 66, -17, S3) + petal(500, 700, 210, 66, 17, S3) + petal(500, 700, 232, 70, 0, "#b9cdb4")
    b += leaf(500, 1230, 300, 90, -62, "#2c3b31", S3) + leaf(500, 1230, 300, 90, 62, "#2c3b31", S3)
    return svg(w, h, defs, b, .12, "#fff")


def e1_steine():  # 4:5
    w, h = 1000, 1250
    defs = lin("bg", "#222a24", "#121512") + lin("wat", "#26322a", "#0f120f") + rad("mg", "#cfe0cb", .4)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += sparkles(w, h, 50, "#dfe9db", 8, 1, 2.2, .7, ymax=700)
    b += f'<circle cx="500" cy="470" r="360" fill="url(#mg)"/><circle cx="500" cy="470" r="150" fill="#d6e0cf" fill-opacity=".85"/>'
    b += hills(w, 780, 30, "#18201b", 9, base=900)
    b += f'<rect y="800" width="{w}" height="{h - 800}" fill="url(#wat)"/>'
    b += ripples(500, 960, 560, 5, S2, .5)
    b += stones(500, 960, 470, ["#5d6b5f", "#7d8d7d", "#98a897", "#b3c0b0", "#cdd6c8"])
    b += lotus(820, 1040, 120, "#4f6c57", "#86a58b", "#d3e4cc", GLOW)
    b += padlily(190, 1060, 120, "#25362b", 4) + padlily(840, 1160, 150, "#25362b", -5)
    return svg(w, h, defs, b, .12, "#fff")


def e1_muster():  # 2:1
    w, h = 2000, 1000
    t = 200
    pat = (f'<pattern id="mu" width="{t}" height="{t}" patternUnits="userSpaceOnUse">'
           f'<rect width="{t}" height="{t}" fill="#1f2621"/>'
           f'<path d="M100 8L192 100L100 192L8 100Z" fill="none" stroke="{S3}" stroke-width="2.4" stroke-opacity=".7"/>'
           f'<path d="M100 38L162 100L100 162L38 100Z" fill="#2a362d"/>'
           + rosette(100, 100, 40, 8, "#4c6150", GLOW, .42, 0) +
           f'<circle cx="0" cy="0" r="9" fill="{S1}" fill-opacity=".6"/><circle cx="{t}" cy="0" r="9" fill="{S1}" fill-opacity=".6"/>'
           f'<circle cx="0" cy="{t}" r="9" fill="{S1}" fill-opacity=".6"/><circle cx="{t}" cy="{t}" r="9" fill="{S1}" fill-opacity=".6"/></pattern>')
    defs = pat + rad("gl", "#e6f0df", .5) + ('<radialGradient id="vg"><stop offset=".25" stop-color="#101310" stop-opacity="0"/>'
                                             '<stop offset="1" stop-color="#101310" stop-opacity=".9"/></radialGradient>')
    b = f'<rect width="{w}" height="{h}" fill="url(#mu)"/><rect width="{w}" height="{h}" fill="url(#vg)"/>'
    b += f'<circle cx="1000" cy="500" r="380" fill="url(#gl)"/>'
    b += lotus(1000, 640, 400, "#4f6c57", "#86a58b", "#d3e4cc", GLOW)
    b += ripples(1000, 660, 700, 3, S2, .4)
    return svg(w, h, defs, b, .10, "#fff")


def e1_oel():  # 3:2
    w, h = 1500, 1000
    defs = lin("bg", "#29312b", "#171a17") + rad("oel", "#e9cf92", 1) + rad("gl", GLOW, .8)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += frond(60, 1050, 560, 55, .5, "#3e5244", S3, 13) + frond(1440, 1050, 600, -55, -.5, "#3e5244", S3, 13)
    b += f'<ellipse cx="750" cy="560" rx="400" ry="395" fill="#000" fill-opacity=".35"/>'
    b += f'<circle cx="750" cy="500" r="380" fill="#47554a"/><circle cx="750" cy="500" r="352" fill="#222a24"/>'
    b += f'<circle cx="750" cy="500" r="318" fill="#b99a55"/><circle cx="750" cy="500" r="318" fill="url(#oel)" fill-opacity=".85"/>'
    b += f'<ellipse cx="640" cy="360" rx="150" ry="70" fill="#fff" fill-opacity=".14" transform="rotate(-28 640 360)"/>'
    b += rosette(750, 500, 160, 12, "#f0ead8", "#e0b660", .42, 0, "#bfae85")
    b += rosette(750, 500, 100, 8, "#e6d9b4", "#c28f2c", .42, 22, "#bfae85")
    for x, y, a in ((520, 650, 30), (980, 360, -40), (940, 690, 70), (570, 330, 110), (1030, 520, 20)):
        b += petal(x, y, 90, 34, a, "#d8e2cf", .95)
    b += tealight(310, 880, 40, PALE) + tealight(1230, 850, 34, PALE)
    return svg(w, h, defs, b, .12, "#fff")


def e1_kraeuter():  # 4:5
    w, h = 1000, 1250
    defs = lin("bg", "#2a312b", "#161916") + rad("gl", "#d7e2cd", .22)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    for i in range(8):  # Leinentuch mit Streifen
        b += f'<rect y="{n(760 + i * 62)}" width="{w}" height="{n(40 + i * 3)}" fill="#fff" fill-opacity="{n(.025 + i * .006)}"/>'
    b += f'<rect y="760" width="{w}" height="490" fill="#2c332e" fill-opacity=".55"/>'
    b += f'<circle cx="480" cy="560" r="480" fill="url(#gl)"/>'
    for x, y, L, a in ((150, 1010, 190, -64), (830, 1060, 200, 70), (320, 1180, 160, -100), (700, 1150, 170, 110)):
        b += leaf(x, y, L, L * .3, a, S3, S2)
    b += herbball(410, 780, 240, "#c8c5ba", "#8fa68e", S3, S1, "#dfe9db")
    b += herbball(720, 960, 165, "#b9b7ab", "#8fa68e", S3, S1, "#dfe9db")
    return svg(w, h, defs, b, .12, "#fff")


def e1_kerzen():  # 4:5
    w, h = 1000, 1250
    defs = lin("bg", "#232824", "#101210") + rad("gl", GLOW, .75)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += f'<circle cx="500" cy="760" r="520" fill="url(#gl)" fill-opacity=".30"/>'
    # Handtücher
    for i, (y, c, c2, wd) in enumerate(((1020, "#a8b5a5", "#8fa68e", 780), (905, "#c8c5ba", "#a6bca5", 700), (800, "#dcd9ce", "#8fa68e", 620))):
        x0 = 500 - wd / 2
        b += f'<rect x="{n(x0)}" y="{n(y)}" width="{wd}" height="118" rx="26" fill="{c}"/>'
        b += f'<rect x="{n(x0 + 30)}" y="{n(y + 82)}" width="{n(wd - 60)}" height="10" rx="5" fill="{c2}"/>'
        b += f'<path d="M{n(x0 + wd * .12)} {n(y + 20)}Q{n(x0 + wd * .2)} {n(y + 60)} {n(x0 + wd * .12)} {n(y + 98)}" fill="none" stroke="#000" stroke-opacity=".12" stroke-width="5"/>'
    b += f'<rect x="60" y="1135" width="880" height="14" rx="7" fill="#000" fill-opacity=".35"/>'
    for x, y, s in ((300, 790, 76), (500, 770, 92), (700, 790, 76), (410, 715, 52), (600, 718, 52)):
        b += tealight(x, y, s, "#c8c5ba")
    b += sparkles(w, h, 26, "#f3d9a4", 21, 1, 3, .7, ymax=520)
    return svg(w, h, defs, b, .12, "#fff")


def e1_raum():  # 3:2
    w, h = 1500, 1000
    defs = (lin("wall", "#2a302b", "#1b1e1b") + lin("fl", "#1c201c", "#0f110f") + lin("sk", "#10151a", "#2a3b3a")
            + rad("gl", GLOW, .8) + rad("fg", GLOW, .35))
    b = f'<rect width="{w}" height="{h}" fill="url(#wall)"/>'
    b += f'<path d="M1010 640V330A190 190 0 0 1 1390 330V640Z" fill="#161a17"/>'
    b += f'<path d="M1040 640V330A160 160 0 0 1 1360 330V640Z" fill="url(#sk)"/>'
    for sx, sy in ((1100, 250), (1150, 400), (1330, 230), (1310, 400), (1090, 330)):
        b += f'<circle cx="{sx}" cy="{sy}" r="3" fill="#dfe9db" fill-opacity=".8"/>'
    b += f'<circle cx="1260" cy="330" r="64" fill="#dce4d4" fill-opacity=".92"/>'
    b += f'<rect x="1040" y="470" width="320" height="170" fill="#16201b" fill-opacity=".7"/>'
    b += f'<path d="M1040 470H1360" stroke="{S3}" stroke-width="6"/><path d="M1200 190V640" stroke="{S3}" stroke-width="6"/>'
    b += f'<path d="M1010 640H1390" stroke="{S3}" stroke-width="12"/>'
    b += f'<rect y="690" width="{w}" height="310" fill="url(#fl)"/>'
    b += f'<circle cx="440" cy="820" r="520" fill="url(#fg)"/>'
    b += f'<path d="M420 0V250" stroke="{S3}" stroke-width="4"/>'
    b += f'<circle cx="420" cy="360" r="190" fill="url(#gl)"/>'
    b += (f'<path d="M420 250L470 280V420L420 450L370 420V280Z" fill="#f0d9a8" fill-opacity=".92"/>'
          f'<path d="M420 250V450M370 280L470 280M370 420L470 420" stroke="#8a7440" stroke-width="3" fill="none"/>')
    b += f'<path d="M330 800H1180L1300 960H190Z" fill="#000" fill-opacity=".35"/>'
    b += f'<path d="M330 760H1170L1290 940H210Z" fill="#7d9a80"/><path d="M370 782H1130L1228 920H272Z" fill="#8fa68e"/>'
    b += f'<path d="M370 782H1130L1228 920H272Z" fill="none" stroke="#5f7660" stroke-width="6"/>'
    b += f'<ellipse cx="256" cy="840" rx="40" ry="62" fill="#c8c5ba"/><rect x="256" y="778" width="190" height="124" fill="#c8c5ba"/><ellipse cx="446" cy="840" rx="40" ry="62" fill="#dcd9ce"/>'
    b += f'<ellipse cx="446" cy="840" rx="40" ry="62" fill="none" stroke="#8fa68e" stroke-width="5"/>'
    b += tealight(1330, 900, 44, PALE)
    return svg(w, h, defs, b, .12, "#fff")


def e1_ornament():  # Trennband, wiederholbar (CSS-Hintergrund)
    w, h = 240, 56
    b = ""
    for i in (0, 1):
        x = 60 + i * 120
        b += lotus(x, 44, 30, S3, S1, S2, GLOW)
    b += f'<circle cx="0" cy="40" r="3.5" fill="{S1}"/><circle cx="120" cy="40" r="3.5" fill="{S1}"/>'
    b += f'<path d="M12 40H48M72 40H108M132 40H168M192 40H228" stroke="{S3}" stroke-width="2" stroke-linecap="round"/>'
    return svg(w, h, "", b, 0).replace('preserveAspectRatio="xMidYMid slice"', "")


# =====================================================================
# Entwurf 2: warm, Nussbraun, Webmuster, Gold
# =====================================================================
B2, M2, D2 = "#2b2216", "#382d1e", "#1f170c"
T1, T2, T3, GO, GO2, OX, CR = "#bda38b", "#d2bba4", "#8f7759", "#c8963e", "#e0b660", "#6b3029", "#ebe9e3"


def e2_buehne():  # 2:3
    w, h = 1000, 1500
    defs = lin("bg", "#34291a", D2) + lin("ar", "#5a4630", "#2b2216") + rad("gl", GO2, .75)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += sparkles(w, h, 40, GO2, 14, 1, 2.4, .6, ymax=300)
    b += f'<path d="M130 1220V560A370 370 0 0 1 870 560V1220Z" fill="{GO}" fill-opacity=".9"/>'
    b += f'<path d="M156 1220V560A344 344 0 0 1 844 560V1220Z" fill="url(#ar)"/>'
    b += f'<circle cx="500" cy="760" r="330" fill="url(#gl)"/><circle cx="500" cy="560" r="130" fill="{GO2}" fill-opacity=".85"/>'
    b += chedi(500, 930, 420, "#3a2e1c", "#4a3a26")
    b += f'<rect x="156" y="960" width="688" height="260" fill="#1f170c" fill-opacity=".55"/>'
    b += ripples(500, 1100, 560, 4, GO2, .5)
    b += lotus(500, 1120, 320, "#7c6444", T1, "#f0e2cb", GO2)
    b += f'<rect y="1262" width="{w}" height="238" fill="{D2}"/>'
    b += textile_band(0, 1290, w, 62, GO, OX, T2, 2)
    return svg(w, h, defs, b, .12, "#fff")


def e2_orchidee():  # 2:3
    w, h = 1000, 1500
    defs = lin("bg", "#3a2d1c", D2) + rad("gl", GO2, .35)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="520" cy="620" r="560" fill="url(#gl)"/>'
    b += sparkles(w, h, 36, GO2, 17, 1, 2.2, .5)
    b += leaf(420, 1520, 760, 120, -22, "#4a3d22", "#6e5a35") + leaf(560, 1520, 700, 110, 24, "#3e3320", "#6e5a35") + leaf(500, 1520, 560, 100, 2, "#56472a", "#7d6840")
    d = "M600 1480C640 1100 330 900 410 480C430 360 500 250 640 190"
    b += stem(d, "#8f7759", 10)
    for (x, y, r, rot) in ((590, 1110, 150, 8), (470, 905, 142, -14), (420, 700, 130, 6), (430, 520, 112, -8), (510, 340, 92, 10), (620, 222, 70, 0)):
        b += orchid(x, y, r, T2, "#f0e2cb", GO, OX if False else GO2, None, rot)
    for x, y, r in ((690, 160, 24), (735, 130, 16)):
        b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{T1}"/>'
    return svg(w, h, defs, b, .12, "#fff")


def e2_phan():  # 2:3, Opfer-Schale auf Fuß
    w, h = 1000, 1500
    defs = lin("bg", "#34291a", D2) + lin("bw", "#d7a64a", "#8a5f1c") + rad("gl", GO2, .5)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="500" cy="720" r="520" fill="url(#gl)"/>'
    b += sparkles(w, h, 30, GO2, 19, 1, 2.2, .5, ymax=420)
    # Tuch
    b += f'<rect y="1180" width="{w}" height="320" fill="{OX}"/>'
    b += textile_band(0, 1200, w, 64, GO, "#4a1f1a", T2, 1)
    b += f'<rect y="1290" width="{w}" height="14" fill="{GO}" fill-opacity=".8"/>'
    b += f'<rect y="1380" width="{w}" height="90" fill="#000" fill-opacity=".18"/>'
    b += f'<ellipse cx="500" cy="1190" rx="270" ry="26" fill="#000" fill-opacity=".35"/>'
    # Fuß, Schaft, Schale
    b += f'<path d="M270 1185C270 1140 380 1110 500 1110S730 1140 730 1185Z" fill="url(#bw)"/>'
    b += f'<path d="M455 1112L470 900H530L545 1112Z" fill="url(#bw)"/>'
    for y, wd in ((1050, 110), (980, 92), (915, 100)):
        b += f'<rect x="{n(500 - wd / 2)}" y="{y}" width="{wd}" height="22" rx="11" fill="{GO2}"/>'
    b += f'<path d="M190 700H810C810 830 690 910 500 910S190 830 190 700Z" fill="url(#bw)"/>'
    b += f'<ellipse cx="500" cy="700" rx="310" ry="34" fill="#f1cf86"/>'
    b += f'<path d="M230 760Q500 800 770 760" fill="none" stroke="{OX}" stroke-width="10" stroke-opacity=".7"/>'
    # Blüten: Ringelblumen und Knospen
    r_ = __import__("random").Random(5)
    for i, (x, y, r, c1, c2) in enumerate(((330, 640, 120, GO, GO2), (500, 590, 140, "#d7a64a", "#f1cf86"), (670, 640, 120, GO, GO2),
                                           (415, 520, 100, "#e0b660", "#f6dca0"), (590, 515, 100, "#e0b660", "#f6dca0"), (500, 430, 84, GO, GO2))):
        b += rosette(x, y, r, 16, c1, None, .27, 0) + rosette(x, y, r * .7, 12, c2, None, .3, 15) + f'<circle cx="{x}" cy="{y}" r="{r * .12}" fill="{OX}"/>'
    for x, y, a in ((230, 640, -60), (770, 640, 60), (345, 740, -30), (655, 740, 30)):
        b += petal(x, y, 150, 40, a, "#f0e2cb", .96)
    # Girlande
    b += f'<path d="M190 745C250 880 400 900 500 905C600 900 750 880 810 745" fill="none" stroke="{OX}" stroke-width="3" stroke-opacity=".9"/>'
    for i in range(1, 10):
        t = i / 10
        x = 190 + 620 * t
        y = 745 + 160 * (1 - (2 * t - 1) ** 2) * .95
        b += f'<circle cx="{n(x)}" cy="{n(y)}" r="14" fill="{GO2 if i % 2 else T1}"/>'
    return svg(w, h, defs, b, .12, "#fff")


def e2_chedi():  # 2:3
    w, h = 1000, 1500
    defs = lin("bg", "#14100a", "#3b2e1b", y2=.8) + rad("gl", GO2, .7) + lin("ch", "#e6c27a", "#9a6f24")
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    b += sparkles(w, h, 90, "#f1e2bd", 23, 1, 2.6, .8, ymax=900)
    b += f'<circle cx="760" cy="300" r="300" fill="url(#gl)" fill-opacity=".5"/><circle cx="760" cy="300" r="90" fill="#f4e4bb" fill-opacity=".9"/>'
    b += hills(w, 1040, 40, "#23190d", 31, base=1400) + hills(w, 1100, 26, "#1a120a", 33, base=1400, f1=1.5)
    b += chedi(180, 1130, 360, "#4a3a22", "#5a4630") + chedi(830, 1130, 300, "#4a3a22", "#5a4630")
    b += f'<circle cx="500" cy="780" r="400" fill="url(#gl)" fill-opacity=".35"/>'
    b += chedi(500, 1170, 960, "url(#ch)", "#f1cf86")
    b += f'<rect y="1262" width="{w}" height="238" fill="{D2}"/>'
    b += textile_band(0, 1292, w, 62, GO, OX, T2, 2)
    return svg(w, h, defs, b, .12, "#fff")


def e2_stempel():  # 3:2
    w, h = 1500, 1000
    defs = lin("bg", "#3a2d1c", D2) + rad("gl", GO2, .35)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    for i in range(12):
        b += f'<rect x="{i * 130}" width="62" height="{h}" fill="#fff" fill-opacity="{.03 + (i % 3) * .012}"/>'
    b += f'<rect y="700" width="{w}" height="300" fill="{OX}"/>' + textile_band(0, 722, w, 74, GO, "#4a1f1a", T2, 1)
    b += f'<rect y="840" width="{w}" height="160" fill="#000" fill-opacity=".2"/>'
    b += f'<circle cx="650" cy="470" r="520" fill="url(#gl)"/>'
    for x, y, L, a in ((250, 800, 190, -70), (1260, 830, 200, 75), (900, 930, 150, 110)):
        b += leaf(x, y, L, L * .3, a, "#6e5a35", T1)
    b += herbball(560, 560, 230, T2, GO, OX, "#8f9a55", T1)
    b += herbball(960, 680, 170, "#c4ad92", GO, OX, "#8f9a55", T1)
    return svg(w, h, defs, b, .12, "#fff")


def e2_frangipani():  # 2:3
    w, h = 1000, 1500
    defs = lin("bg", "#34291a", D2) + rad("gl", GO2, .3)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="500" cy="700" r="560" fill="url(#gl)"/>'
    b += leaf(300, 1560, 900, 130, -28, "#3e3320", "#6e5a35") + leaf(700, 1560, 940, 130, 30, "#4a3d22", "#6e5a35") + leaf(500, 1560, 700, 110, 4, "#56472a", "#7d6840")
    for (x, y, r, rot) in ((520, 560, 280, 8), (300, 1050, 220, -20), (720, 1100, 190, 24), (700, 250, 130, 40)):
        for i in range(5):
            b += petal(x, y, r, r * .62, rot + i * 72, "#f0e2cb", 1, "#c8b394", 2)
        for i in range(5):
            b += petal(x, y, r * .55, r * .26, rot + i * 72 + 8, GO2, .95)
        b += f'<circle cx="{x}" cy="{y}" r="{r * .06}" fill="{GO}"/>'
    return svg(w, h, defs, b, .12, "#fff")


def e2_tuecher():  # 3:2
    w, h = 1500, 1000
    defs = lin("bg", "#3a2d1c", D2) + rad("gl", GO2, .6)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="1010" cy="520" r="470" fill="url(#gl)" fill-opacity=".5"/>'
    for i, (y, c, wd, st) in enumerate(((730, T3, 960, OX), (610, T1, 880, GO), (490, T2, 800, OX), (370, "#e3d3bd", 720, GO))):
        x0 = 500 - wd / 2 + 80
        b += f'<rect x="{n(x0)}" y="{y}" width="{wd}" height="136" rx="32" fill="{c}"/>'
        b += f'<rect x="{n(x0 + 36)}" y="{y + 92}" width="{wd - 72}" height="12" rx="6" fill="{st}"/><rect x="{n(x0 + 36)}" y="{y + 110}" width="{wd - 72}" height="6" rx="3" fill="{st}" fill-opacity=".6"/>'
        b += f'<path d="M{n(x0 + 70)} {y + 22}Q{n(x0 + 100)} {y + 66} {n(x0 + 70)} {y + 108}" fill="none" stroke="#000" stroke-opacity=".12" stroke-width="6"/>'
    b += f'<rect x="60" y="866" width="1100" height="16" rx="8" fill="#000" fill-opacity=".35"/>'
    b += tealight(1180, 800, 74, T2, "#f6dca0") + tealight(1320, 830, 52, T2, "#f6dca0")
    b += leaf(1150, 880, 190, 50, 70, "#6e5a35", T1)
    b += sparkles(w, h, 20, GO2, 39, 1, 3, .7, ymax=330)
    return svg(w, h, defs.replace('rad("gl"', ""), b.replace('url(#gl)', 'url(#gl)'), .12, "#fff")


def e2_ornament():
    w, h = 248, 62
    b = textile_band(0, 0, w, 62, GO, OX, T2, 1)
    return svg(w, h, "", b, 0).replace('preserveAspectRatio="xMidYMid slice"', "")


# =====================================================================
# Entwurf 3: hell, Papier, Ocker, Botanik
# =====================================================================
P3, M3, M32, PAP = "#e4e1da", "#d6d2c9", "#cac5b9", "#f1eee7"
OC, OC2, OC3, INK = "#9c6b0f", "#c28f2c", "#e0b968", "#26241d"
OL, OL2, CL, CL2, SD = "#7b8460", "#a2aa84", "#b88a64", "#d3b494", "#e8d9bc"


def e3_hero():  # 8:5
    w, h = 1600, 1000
    defs = lin("sk", "#f4efe3", "#e7d8b6", y2=.75) + rad("gl", OC3, .7)
    b = f'<rect width="{w}" height="{h}" fill="url(#sk)"/>'
    b += f'<circle cx="1060" cy="400" r="520" fill="url(#gl)"/><circle cx="1060" cy="400" r="215" fill="{OC2}" fill-opacity=".92"/>'
    b += f'<circle cx="1060" cy="400" r="215" fill="none" stroke="{OC}" stroke-width="3" stroke-opacity=".5"/>'
    b += hills(w, 600, 36, "#d9c9a4", 41, base=1100) + chedi(1330, 650, 330, "#cdbb91", "#c6b284")
    b += hills(w, 680, 40, "#b9b78d", 43, base=1100, f1=1.2) + chedi(240, 715, 400, "#a4a77c", "#9ea275") + chedi(470, 722, 250, "#a4a77c", "#9ea275")
    b += hills(w, 780, 36, "#8d9470", 47, base=1100, f1=.8) + chedi(900, 822, 210, "#7f8864", "#79825e")
    b += hills(w, 880, 30, "#6a7355", 49, base=1100, f1=1.1)
    for i, x in enumerate(range(120, 1600, 210)):
        b += lotus(x + (i % 2) * 40, 985, 70, "#7c6a35", "#a9863c", OC3, SD)
    return svg(w, h, defs, b, .10, "#000")


def e3_tor():  # 3:4
    w, h = 900, 1200
    defs = lin("sk", "#f4efe3", "#e7d8b6") + rad("gl", OC3, .6)
    b = f'<rect width="{w}" height="{h}" fill="url(#sk)"/><circle cx="450" cy="470" r="400" fill="url(#gl)"/>'
    b += f'<rect y="1080" width="{w}" height="120" fill="{CL2}"/>'
    # Blick durchs Tor: ferner Chedi
    b += f'<rect x="318" y="600" width="264" height="480" fill="{SD}"/>' + chedi(450, 1080, 360, OL2, "#9ea275")
    b += f'<rect x="230" y="560" width="88" height="520" fill="{CL}"/><rect x="582" y="560" width="88" height="520" fill="{CL}"/>'
    b += f'<rect x="230" y="560" width="22" height="520" fill="#fff" fill-opacity=".14"/><rect x="582" y="560" width="22" height="520" fill="#fff" fill-opacity=".14"/>'
    b += f'<rect x="200" y="520" width="500" height="54" fill="{OC}"/>' + textile_band(200, 524, 500, 46, OC3, "#7a5209", SD, 1).replace("<path", "<path")
    b += roof(450, 520, 640, 300, OC2, OC)
    b += f'<rect x="150" y="1040" width="600" height="40" fill="{CL2}"/><rect x="110" y="1080" width="680" height="40" fill="#c7a883"/>'
    b += lotus(120, 1160, 60, "#7c6a35", "#a9863c", OC3, SD) + lotus(780, 1160, 60, "#7c6a35", "#a9863c", OC3, SD)
    return svg(w, h, defs, b, .10, "#000")


def e3_orchidee_weiss():  # 1:1
    w, h = 1000, 1000
    defs = lin("bg", CL2, "#e6d3b4") + rad("gl", "#fff", .55)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="560" cy="430" r="420" fill="url(#gl)"/>'
    b += leaf(240, 1040, 640, 110, -26, "#5d6544", "#8d9470") + leaf(330, 1040, 520, 100, 12, "#6f7852", "#9aa27c")
    b += stem("M300 1020C330 800 560 780 600 520C620 380 600 300 560 220", "#7a6a45", 9)
    for (x, y, r, rot) in ((470, 780, 150, -10), (610, 560, 140, 8), (580, 360, 118, -6), (545, 215, 86, 6)):
        b += orchid(x, y, r, "#fbf9f4", "#fffdf8", "#f3e7c9", OC, "#d9ceb5", rot)
    return svg(w, h, defs, b, .10, "#000")


def e3_steine():  # 3:2
    w, h = 1500, 1000
    defs = lin("bg", "#f4efe3", "#e3d3ae") + rad("gl", OC3, .6)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="750" cy="470" r="420" fill="url(#gl)"/><circle cx="750" cy="450" r="250" fill="{OC2}" fill-opacity=".55"/>'
    b += hills(w, 800, 22, "#d6c49e", 51, base=1100) + f'<rect y="840" width="{w}" height="160" fill="#c9b78f"/>'
    b += ripples(750, 905, 640, 4, OC, .45)
    b += stones(750, 900, 520, [CL, "#a89a6e", "#c9b383", "#d9c8a2", OL])
    b += leaf(260, 940, 300, 60, -55, OL, "#5d6544") + leaf(1240, 950, 320, 60, 60, "#6a7355", "#5d6544")
    return svg(w, h, defs, b, .10, "#000")


def e3_sen():  # 3:2, Energielinien
    w, h = 1500, 1000
    defs = lin("bg", "#f1eee7", "#e3dac4") + rad("gl", OC3, .55)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="750" cy="500" r="420" fill="url(#gl)"/>'
    cols = [OC, OL, CL, OC2, OL, CL, OC, OL, CL, OC2]
    for i in range(10):
        y0 = 120 + i * 84
        y1 = y0
        ym = 500 + (i - 4.5) * 22
        wd = 2.5 + (3 if i in (2, 7) else 0)
        b += (f'<path d="M-20 {y0}C420 {y0} 520 {ym} 750 {ym}C980 {ym} 1080 {y1} 1520 {y1}" fill="none" stroke="{cols[i]}" stroke-width="{wd}" '
              f'stroke-opacity="{.85 if i in (2, 7) else .6}" stroke-linecap="round"/>')
    for i in range(10):
        ym = 500 + (i - 4.5) * 22
        b += f'<circle cx="750" cy="{n(ym)}" r="6" fill="{PAP}" stroke="{OC}" stroke-width="2"/>'
    b += f'<circle cx="750" cy="500" r="64" fill="{OC2}" fill-opacity=".9"/>' + rosette(750, 500, 40, 8, PAP, OC, .45)
    return svg(w, h, defs, b, .10, "#000")


def e3_fussbad():  # 3:2
    w, h = 1500, 1000
    defs = lin("bg", "#f4efe3", "#e3d3ae") + lin("sc", "#c99b6e", "#9d7048") + rad("gl", OC3, .5)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="750" cy="420" r="400" fill="url(#gl)"/>'
    b += f'<rect y="780" width="{w}" height="220" fill="#d6c49e"/>'
    b += leaf(180, 900, 380, 70, -50, OL, "#5d6544") + leaf(1330, 900, 400, 70, 52, "#6a7355", "#5d6544")
    b += f'<ellipse cx="750" cy="830" rx="470" ry="50" fill="#000" fill-opacity=".18"/>'
    b += f'<path d="M270 560H1230C1230 760 1060 850 750 850S270 760 270 560Z" fill="url(#sc)"/>'
    b += f'<path d="M290 640Q750 700 1210 640" fill="none" stroke="{SD}" stroke-width="10" stroke-opacity=".7"/>'
    b += f'<ellipse cx="750" cy="560" rx="480" ry="62" fill="#e9dcc2"/><ellipse cx="750" cy="566" rx="440" ry="48" fill="#cbd6c3"/>'
    b += lotus(750, 560, 190, "#c8a96a", "#e6cf9a", "#fffaf0", OC2)
    for x, y, a in ((480, 575, 60), (1020, 580, -70), (600, 590, 100), (900, 588, 70)):
        b += petal(x, y, 70, 26, a, "#fdf7ea", .95)
    for dx in (-120, 0, 120):
        b += f'<path d="M{750 + dx} 330c60 -60 -60 -100 0 -170" fill="none" stroke="{OC}" stroke-opacity=".35" stroke-width="7" stroke-linecap="round"/>'
    return svg(w, h, defs, b, .10, "#000")


def e3_paar():  # 3:2
    w, h = 1500, 1000
    defs = lin("bg", "#f1eee7", "#e3d8bd") + lin("wt", "#d9d4bd", "#b7b695") + rad("gl", OC3, .5)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="750" cy="400" r="460" fill="url(#gl)"/>'
    b += f'<circle cx="750" cy="380" r="170" fill="{OC2}" fill-opacity=".5"/>'
    b += f'<rect y="640" width="{w}" height="360" fill="url(#wt)"/>'
    b += ripples(520, 800, 560, 4, OL, .5) + ripples(1010, 860, 430, 3, OL, .5)
    for x, y, rx, a in ((200, 740, 150, 4), (1340, 720, 120, -4), (1230, 920, 200, 6), (260, 930, 170, -6), (780, 950, 140, 0)):
        b += padlily(x, y, rx, "#6a7355", a)
    b += lotus(520, 805, 360, "#d7b36e", "#ecd29a", "#fffaf0", OC2)
    b += lotus(1010, 862, 260, "#d7b36e", "#ecd29a", "#fffaf0", OC2)
    return svg(w, h, defs, b, .10, "#000")


def e3_chedis():  # 3:4
    w, h = 900, 1200
    defs = lin("sk", "#f4efe3", "#e7d8b6", y2=.8) + rad("gl", OC3, .6)
    b = f'<rect width="{w}" height="{h}" fill="url(#sk)"/><circle cx="640" cy="330" r="360" fill="url(#gl)"/><circle cx="640" cy="330" r="130" fill="{OC2}" fill-opacity=".9"/>'
    b += hills(w, 820, 28, "#d9c9a4", 61, base=1300) + chedi(160, 830, 300, "#cdbb91", "#c6b284") + chedi(750, 830, 260, "#cdbb91", "#c6b284")
    b += hills(w, 900, 26, "#a4a77c", 63, base=1300, f1=1.3)
    b += chedi(450, 960, 760, OC, OC2)
    b += chedi(210, 980, 440, "#8d9470", "#7f8864") + chedi(700, 985, 380, "#8d9470", "#7f8864")
    b += f'<rect y="1000" width="{w}" height="200" fill="#6a7355"/>'
    b += textile_band(0, 1040, w, 60, OC3, "#5d6544", SD, 1)
    return svg(w, h, defs, b, .10, "#000")


def e3_toksen():  # 8:5
    w, h = 1600, 1000
    defs = (lin("bg", "#ece6d8", "#ddd3bd") + lin("wd", "#c9985f", "#8e6334", x2=0, y2=1) + lin("wd2", "#b88a52", "#7a522c") + rad("gl", "#fff", .5))
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/>'
    for i in range(50):  # Leinenstruktur
        b += f'<rect y="{i * 20}" width="{w}" height="2" fill="#000" fill-opacity=".03"/>'
    b += f'<circle cx="800" cy="440" r="560" fill="url(#gl)"/>'
    b += f'<rect y="840" width="{w}" height="160" fill="{OL}"/>' + textile_band(0, 862, w, 62, OC3, "#5d6544", SD, 1)
    b += f'<ellipse cx="760" cy="820" rx="640" ry="26" fill="#000" fill-opacity=".18"/>'
    # Keil
    b += (f'<g transform="translate(560 730) rotate(-9)"><path d="M0 -34L700 -10V10L0 34Q-40 0 0 -34Z" fill="url(#wd2)"/>'
          f'<path d="M30 -18L690 -4M30 8L690 2" stroke="#5a381a" stroke-opacity=".35" stroke-width="3"/></g>')
    # Hammer
    b += (f'<g transform="translate(790 500) rotate(-24)"><rect x="-60" y="-24" width="640" height="48" rx="24" fill="url(#wd)"/>'
          f'<path d="M-40 -8L560 -8M-30 10L540 10" stroke="#5a381a" stroke-opacity=".3" stroke-width="3"/>'
          f'<rect x="-390" y="-92" width="360" height="184" rx="70" fill="url(#wd2)"/><ellipse cx="-390" cy="0" rx="40" ry="92" fill="#8e6334"/>'
          f'<ellipse cx="-390" cy="0" rx="26" ry="64" fill="none" stroke="#5a381a" stroke-opacity=".4" stroke-width="3"/>'
          f'<path d="M-330 -52H-70M-330 0H-70M-330 52H-70" stroke="#5a381a" stroke-opacity=".3" stroke-width="3"/>'
          f'<rect x="-120" y="-98" width="34" height="196" rx="12" fill="{OC}"/></g>')
    return svg(w, h, defs, b, .10, "#000")


def e3_zweig():  # 1:1
    w, h = 1000, 1000
    defs = lin("bg", M3, "#e8dfc8") + rad("gl", "#fff", .5)
    b = f'<rect width="{w}" height="{h}" fill="url(#bg)"/><circle cx="520" cy="440" r="440" fill="url(#gl)"/>'
    b += leaf(150, 1040, 520, 80, -40, "#8d9470", "#5d6544") + leaf(250, 1040, 420, 70, 8, "#a2aa84", "#6a7355")
    b += stem("M120 960C300 900 520 880 640 640C720 480 820 420 900 300", OC, 7)
    for (x, y, r, rot) in ((320, 905, 120, -22), (480, 840, 116, 10), (620, 700, 110, -6), (730, 520, 100, 12), (840, 360, 84, -4)):
        b += orchid(x, y, r, PAP, "#faf6ec", "#f0dcae", OC2, OC, rot)
    for x, y, r in ((905, 260, 22), (935, 215, 15)):
        b += f'<circle cx="{x}" cy="{y}" r="{r}" fill="{CL2}" stroke="{OC}" stroke-width="2"/>'
    return svg(w, h, defs, b, .10, "#000")


def e3_ornament():  # Rankenband, hell
    w, h = 320, 56
    b = ""
    for i in range(2):
        x0 = i * 160
        b += f'<path d="M{x0} 28C{x0 + 40} 4 {x0 + 70} 52 {x0 + 80} 28S{x0 + 120} 4 {x0 + 160} 28" fill="none" stroke="{OC}" stroke-width="2.4" stroke-linecap="round"/>'
        b += petal(x0 + 40, 14, 22, 8, -30, OC2) + petal(x0 + 120, 42, 22, 8, 150, OC2)
        b += f'<circle cx="{x0 + 80}" cy="28" r="5" fill="{OC}"/>'
    return svg(w, h, "", b, 0).replace('preserveAspectRatio="xMidYMid slice"', "")


JOBS = {
    "beispiel-1": {"nacht-lotus.svg": e1_hero, "farn-knospe.svg": e1_farn, "steine.svg": e1_steine, "muster-band.svg": e1_muster,
                   "oelschale.svg": e1_oel, "kraeuterstempel.svg": e1_kraeuter, "teelichter.svg": e1_kerzen, "raum.svg": e1_raum,
                   "ornament.svg": e1_ornament},
    "beispiel-2": {"buehne-lotus.svg": e2_buehne, "orchidee.svg": e2_orchidee, "opferschale.svg": e2_phan, "chedi.svg": e2_chedi,
                   "kraeuterstempel.svg": e2_stempel, "frangipani.svg": e2_frangipani, "tuecher.svg": e2_tuecher, "ornament.svg": e2_ornament},
    "beispiel-3": {"huegel.svg": e3_hero, "tor.svg": e3_tor, "orchidee-weiss.svg": e3_orchidee_weiss, "steine.svg": e3_steine,
                   "sen-linien.svg": e3_sen, "fussbad.svg": e3_fussbad, "lotus-paar.svg": e3_paar, "chedis.svg": e3_chedis,
                   "tok-sen.svg": e3_toksen, "orchidee-zweig.svg": e3_zweig, "ornament.svg": e3_ornament},
}

if __name__ == "__main__":
    for sub, jobs in JOBS.items():
        for name, fn in jobs.items():
            save(sub, name, fn())
            print("ok", sub, name)
