"""Bausteine für die selbst gezeichneten Platzhalterbilder (nur SVG, keine fremden Bilder).

Alles hier ist eigene Grafik. Die Bilder haben feste Seitenverhältnisse, damit später ein echtes Foto
mit denselben width/height-Werten 1:1 an die Stelle passt.
"""
import math
import random


def n(x):
    s = f"{x:.1f}"
    return s[:-2] if s.endswith(".0") else s


def A(**k):
    return " ".join(f'{a.replace("_", "-")}="{v}"' for a, v in k.items() if v is not None)


# ---------- Rahmen, Verläufe, Körnung ----------
def lin(i, c1, c2, x1=0, y1=0, x2=0, y2=1, o1=1, o2=1):
    return (f'<linearGradient id="{i}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">'
            f'<stop offset="0" stop-color="{c1}" stop-opacity="{o1}"/>'
            f'<stop offset="1" stop-color="{c2}" stop-opacity="{o2}"/></linearGradient>')


def rad(i, c, o=0.9, stops=None):
    return (f'<radialGradient id="{i}"><stop offset="0" stop-color="{c}" stop-opacity="{o}"/>'
            f'<stop offset=".45" stop-color="{c}" stop-opacity="{o * .35:.2f}"/>'
            f'<stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>')


GRAIN = ('<filter id="kn" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" '
         'baseFrequency=".85" numOctaves="2" seed="7" result="t"/><feColorMatrix in="t" type="matrix" '
         'values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .55 -.18"/></filter>')


def svg(w, h, defs, body, grain=0.10, grain_color="#000"):
    g = ""
    if grain:
        g = (f'<rect width="{w}" height="{h}" fill="{grain_color}" filter="url(#kn)" opacity="{grain}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'preserveAspectRatio="xMidYMid slice"><defs>{GRAIN}{defs}</defs>{body}{g}</svg>')


# ---------- Formen ----------
def petal_d(L, W):
    return (f"M0 0C{n(W)} {n(-L * .35)} {n(W * .72)} {n(-L * .86)} 0 {n(-L)}"
            f"C{n(-W * .72)} {n(-L * .86)} {n(-W)} {n(-L * .35)} 0 0Z")


def petal(x, y, L, W, ang, fill, op=1, stroke=None, sw=1):
    return (f'<path transform="translate({n(x)} {n(y)}) rotate({n(ang)})" d="{petal_d(L, W)}" '
            f'fill="{fill}" fill-opacity="{op}"' + (f' stroke="{stroke}" stroke-width="{sw}"' if stroke else "") + "/>")


def lotus(x, y, s, ca, cb, cc, core="#e6c48f"):
    """Lotusblüte von der Seite. s = Höhe der mittleren Blütenblätter in Pixeln."""
    o = ""
    for a in (-80, 80):
        o += petal(x, y, s * .72, s * .30, a, ca)
    for a in (-60, 60):
        o += petal(x, y, s * .86, s * .32, a, ca)
    for a in (-38, 38):
        o += petal(x, y, s * .95, s * .33, a, cb)
    for a in (-17, 17):
        o += petal(x, y, s * 1.0, s * .33, a, cb)
    o += petal(x, y, s * 1.04, s * .34, 0, cc)
    o += f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(s * .22)}" ry="{n(s * .045)}" fill="{core}" fill-opacity=".9"/>'
    return o


def rosette(x, y, r, cnt, fill, fill2=None, W=.5, rot=0, ring=None):
    """Blüte von oben."""
    o = ""
    for i in range(cnt):
        a = rot + 360 / cnt * i
        o += petal(x, y, r, r * W, a, fill, 1, ring, 1.2 if ring else 1)
    if fill2:
        o += f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r * .16)}" fill="{fill2}"/>'
    return o


def bez(p0, p1, p2, t):
    u = 1 - t
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    dx = 2 * u * (p1[0] - p0[0]) + 2 * t * (p2[0] - p1[0])
    dy = 2 * u * (p1[1] - p0[1]) + 2 * t * (p2[1] - p1[1])
    return x, y, math.degrees(math.atan2(dy, dx)) + 90  # 0 = nach oben


def frond(x, y, L, ang, curve, fill, stem, cnt=15, wid=.30, op=1):
    """Farnwedel: gebogener Stiel mit gefiederten Blättchen."""
    p0, p1, p2 = (0, 0), (curve * L * .35, -L * .55), (curve * L * .7, -L)
    o = f'<g transform="translate({n(x)} {n(y)}) rotate({n(ang)})">'
    o += f'<path d="M0 0Q{n(p1[0])} {n(p1[1])} {n(p2[0])} {n(p2[1])}" fill="none" stroke="{stem}" stroke-width="{n(max(2, L * .012))}" stroke-linecap="round"/>'
    for i in range(1, cnt + 1):
        t = i / (cnt + 1)
        px, py, a = bez(p0, p1, p2, t)
        ll = L * .30 * (1 - t * .78)
        for side in (-1, 1):
            o += petal(px, py, ll, ll * wid, a + side * 68, fill, op)
    px, py, a = bez(p0, p1, p2, 1)
    o += petal(px, py, L * .08, L * .03, a, fill, op)
    return o + "</g>"


def leaf(x, y, L, W, ang, fill, vein=None, op=1):
    o = petal(x, y, L, W, ang, fill, op)
    if vein:
        o += (f'<path transform="translate({n(x)} {n(y)}) rotate({n(ang)})" d="M0 0V{n(-L * .96)}" '
              f'stroke="{vein}" stroke-width="{n(max(1.5, L * .01))}" fill="none" stroke-linecap="round" stroke-opacity=".6"/>')
    return o


def smooth(points, close_to=None):
    """Weicher Pfad durch Punkte (quadratisch über Mittelpunkte)."""
    d = f"M{n(points[0][0])} {n(points[0][1])}"
    for i in range(1, len(points) - 1):
        mx = (points[i][0] + points[i + 1][0]) / 2
        my = (points[i][1] + points[i + 1][1]) / 2
        d += f"Q{n(points[i][0])} {n(points[i][1])} {n(mx)} {n(my)}"
    d += f"L{n(points[-1][0])} {n(points[-1][1])}"
    if close_to is not None:
        d += f"V{n(close_to)}H{n(points[0][0])}Z"
    return d


def hills(w, y, amp, fill, seed, step=90, base=None, op=1, f1=1.0, f2=2.3):
    r = random.Random(seed)
    ph1, ph2 = r.random() * 6, r.random() * 6
    pts = []
    x = -step
    while x <= w + step:
        yy = y + amp * (math.sin(x / w * math.pi * 2 * f1 + ph1) * .6 + math.sin(x / w * math.pi * 2 * f2 + ph2) * .4)
        pts.append((x, yy))
        x += step
    return f'<path d="{smooth(pts, close_to=base if base else y + 4000)}" fill="{fill}" fill-opacity="{op}"/>'


def stones(x, y, s, cols, rot=(-3, 4, -2, 3, 0)):
    """Gestapelte Steine; s = Breite des untersten Steins."""
    o = f'<ellipse cx="{n(x)}" cy="{n(y + s * .02)}" rx="{n(s * .62)}" ry="{n(s * .07)}" fill="#000" fill-opacity=".28"/>'
    ws = [1, .74, .54, .38, .24]
    hs = [.30, .24, .19, .15, .12]
    yy = y
    for i in range(min(len(cols), len(ws))):
        w, h = s * ws[i] / 2, s * hs[i] / 2
        yy -= h
        o += f'<g transform="rotate({rot[i]} {n(x)} {n(yy)})"><ellipse cx="{n(x)}" cy="{n(yy)}" rx="{n(w)}" ry="{n(h)}" fill="{cols[i]}"/>'
        o += f'<ellipse cx="{n(x - w * .22)}" cy="{n(yy - h * .35)}" rx="{n(w * .55)}" ry="{n(h * .35)}" fill="#fff" fill-opacity=".10"/></g>'
        yy -= h * .86
    return o


def ripples(x, y, w, cnt, color, op=.5, ratio=.16, sw=2):
    o = ""
    for i in range(cnt):
        k = 1 + i * .55
        o += (f'<ellipse cx="{n(x)}" cy="{n(y)}" rx="{n(w * k / 2)}" ry="{n(w * k / 2 * ratio)}" fill="none" '
              f'stroke="{color}" stroke-opacity="{n(op / (1 + i * .55))}" stroke-width="{sw}"/>')
    return o


def tealight(x, y, s, cup="#c8c5ba", flame="#f3d9a4", glow_id="gl"):
    """s = Breite des Becherchens."""
    o = f'<circle cx="{n(x)}" cy="{n(y - s * .7)}" r="{n(s * 2.1)}" fill="url(#{glow_id})"/>'
    o += (f'<path d="M{n(x - s / 2)} {n(y - s * .42)}L{n(x - s * .4)} {n(y)}H{n(x + s * .4)}L{n(x + s / 2)} {n(y - s * .42)}Z" fill="{cup}"/>')
    o += f'<ellipse cx="{n(x)}" cy="{n(y - s * .42)}" rx="{n(s / 2)}" ry="{n(s * .09)}" fill="#fff" fill-opacity=".35"/>'
    o += (f'<path d="M{n(x)} {n(y - s * 1.25)}C{n(x + s * .24)} {n(y - s * .9)} {n(x + s * .16)} {n(y - s * .52)} {n(x)} {n(y - s * .46)}'
          f'C{n(x - s * .16)} {n(y - s * .52)} {n(x - s * .24)} {n(y - s * .9)} {n(x)} {n(y - s * 1.25)}Z" fill="{flame}"/>')
    return o


def herbball(x, y, r, cloth, cloth2, cord, herb, steam=None):
    """Kräuterstempel: Stoffball mit Knoten und Bändchen."""
    o = f'<ellipse cx="{n(x)}" cy="{n(y + r * .92)}" rx="{n(r * .9)}" ry="{n(r * .14)}" fill="#000" fill-opacity=".25"/>'
    o += f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" fill="{cloth}"/>'
    o += f'<path d="M{n(x - r * .95)} {n(y - r * .2)}Q{n(x)} {n(y + r * .35)} {n(x + r * .95)} {n(y - r * .2)}" fill="none" stroke="{cloth2}" stroke-width="{n(r * .04)}" stroke-opacity=".6"/>'
    o += f'<path d="M{n(x - r * .7)} {n(y + r * .45)}Q{n(x)} {n(y + r * .95)} {n(x + r * .7)} {n(y + r * .45)}" fill="none" stroke="{cloth2}" stroke-width="{n(r * .04)}" stroke-opacity=".5"/>'
    o += f'<ellipse cx="{n(x - r * .3)}" cy="{n(y - r * .35)}" rx="{n(r * .5)}" ry="{n(r * .3)}" fill="#fff" fill-opacity=".10" transform="rotate(-25 {n(x - r * .3)} {n(y - r * .35)})"/>'
    # Knoten oben
    o += f'<path d="M{n(x - r * .22)} {n(y - r * .93)}L{n(x - r * .34)} {n(y - r * 1.42)}Q{n(x)} {n(y - r * 1.62)} {n(x + r * .34)} {n(y - r * 1.42)}L{n(x + r * .22)} {n(y - r * .93)}Z" fill="{cloth}"/>'
    o += f'<rect x="{n(x - r * .27)}" y="{n(y - r * 1.12)}" width="{n(r * .54)}" height="{n(r * .13)}" rx="{n(r * .06)}" fill="{cord}"/>'
    for a, l in ((-35, .5), (0, .62), (35, .5)):
        o += petal(x, y - r * 1.5, r * l, r * .17, a, herb)
    if steam:
        for dx in (-.3, 0, .3):
            o += (f'<path d="M{n(x + r * dx)} {n(y - r * 2.1)}c{n(r * .2)} {n(-r * .3)} {n(-r * .2)} {n(-r * .5)} 0 {n(-r * .85)}" '
                  f'fill="none" stroke="{steam}" stroke-opacity=".35" stroke-width="{n(max(2, r * .05))}" stroke-linecap="round"/>')
    return o


def chedi(cx, by, h, fill, fill2=None, ring=None):
    w = h * .56
    fill2 = fill2 or fill
    o = ""
    for i, (ww, hh) in enumerate(((1, .09), (.8, .08), (.64, .07))):
        y0 = by - sum((.09, .08, .07)[:i]) * h
        o += f'<rect x="{n(cx - w * ww / 2)}" y="{n(y0 - hh * h)}" width="{n(w * ww)}" height="{n(hh * h)}" fill="{fill if i % 2 == 0 else fill2}"/>'
    yb = by - .24 * h
    o += (f'<path d="M{n(cx - w * .27)} {n(yb)}C{n(cx - w * .36)} {n(yb - h * .17)} {n(cx - w * .19)} {n(yb - h * .30)} {n(cx - w * .1)} {n(yb - h * .34)}'
          f'H{n(cx + w * .1)}C{n(cx + w * .19)} {n(yb - h * .30)} {n(cx + w * .36)} {n(yb - h * .17)} {n(cx + w * .27)} {n(yb)}Z" fill="{fill}"/>')
    yr = yb - h * .34
    for i in range(6):
        ww = w * (.24 - i * .03)
        o += f'<rect x="{n(cx - ww / 2)}" y="{n(yr - (i + 1) * h * .033)}" width="{n(ww)}" height="{n(h * .022)}" rx="{n(h * .01)}" fill="{fill2}"/>'
    ys = yr - 6 * h * .033
    o += f'<path d="M{n(cx - w * .045)} {n(ys)}L{n(cx)} {n(by - h)}L{n(cx + w * .045)} {n(ys)}Z" fill="{fill}"/>'
    o += f'<circle cx="{n(cx)}" cy="{n(ys + h * .01)}" r="{n(w * .05)}" fill="{fill2}"/>'
    return o


def roof(cx, by, w, h, fill, fill2, tiers=3):
    """Thai-Dach mit aufgeschwungenen Enden (Chofa-Form), von unten nach oben gestapelt."""
    o = ""
    for i in range(tiers):
        tw = w * (1 - .22 * i)
        ty = by - i * h * .27
        c = fill if i % 2 == 0 else fill2
        o += (f'<path d="M{n(cx - tw / 2 - tw * .05)} {n(ty - h * .15)}Q{n(cx - tw * .47)} {n(ty - h * .01)} {n(cx - tw * .38)} {n(ty)}'
              f'H{n(cx + tw * .38)}Q{n(cx + tw * .47)} {n(ty - h * .01)} {n(cx + tw / 2 + tw * .05)} {n(ty - h * .15)}'
              f'C{n(cx + tw * .32)} {n(ty - h * .17)} {n(cx + tw * .1)} {n(ty - h * .28)} {n(cx)} {n(ty - h * .33)}'
              f'C{n(cx - tw * .1)} {n(ty - h * .28)} {n(cx - tw * .32)} {n(ty - h * .17)} {n(cx - tw / 2 - tw * .05)} {n(ty - h * .15)}Z" fill="{c}"/>')
    ty = by - (tiers - 1) * h * .27 - h * .33
    o += f'<path d="M{n(cx - w * .012)} {n(ty)}L{n(cx)} {n(ty - h * .22)}L{n(cx + w * .012)} {n(ty)}Z" fill="{fill2}"/>'
    return o


def diamond(x, y, r, fill):
    return f'<path d="M{n(x)} {n(y - r)}L{n(x + r)} {n(y)}L{n(x)} {n(y + r)}L{n(x - r)} {n(y)}Z" fill="{fill}"/>'


def textile_band(x, y, w, cell, c1, c2, c3, rows=1):
    """Thai-Webborte: Rauten mit Innenraute und Punkt, dazwischen Zähne."""
    o = ""
    k = int(w // cell) + 2
    for r_ in range(rows):
        yy = y + r_ * cell
        for i in range(k):
            cx = x + i * cell + cell / 2
            cy = yy + cell / 2
            o += diamond(cx, cy, cell * .46, c1)
            o += diamond(cx, cy, cell * .28, c2)
            o += f'<circle cx="{n(cx)}" cy="{n(cy)}" r="{n(cell * .07)}" fill="{c3}"/>'
            o += f'<path d="M{n(cx + cell * .5)} {n(yy)}l{n(cell * .12)} {n(cell * .5)}l{n(-cell * .12)} {n(cell * .5)}l{n(-cell * .12)} {n(-cell * .5)}z" fill="{c2}" fill-opacity=".55"/>'
    return o


def sparkles(w, h, cnt, color, seed, rmin=1.5, rmax=4, op=.7, ymax=None):
    r = random.Random(seed)
    o = ""
    for _ in range(cnt):
        o += (f'<circle cx="{n(r.random() * w)}" cy="{n(r.random() * (ymax or h))}" r="{n(rmin + r.random() * (rmax - rmin))}" '
              f'fill="{color}" fill-opacity="{n(op * (.4 + r.random() * .6))}"/>')
    return o


def padlily(x, y, rx, fill, ang=0):
    ry = rx * .24
    return (f'<g transform="rotate({ang} {n(x)} {n(y)})"><path d="M{n(x)} {n(y)}L{n(x + rx)} {n(y - ry * .4)}A{n(rx)} {n(ry)} 0 1 1 {n(x + rx * .96)} {n(y + ry * .4)}Z" fill="{fill}"/></g>')
