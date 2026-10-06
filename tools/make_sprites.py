"""Erzeugt die Platzhalter-Sprites (Feuer + Charaktere/Outfits). Aufruf: python tools/make_sprites.py

Ersetze die PNGs spaeter durch eigene Pixel-Art (z. B. aus Aseprite): gleiche Frame-Groesse,
Frames nebeneinander in einer Datei. Die Charakter-Texte/Zuordnung stehen in Characters/*/character.json.
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def rect(im, x0, y0, x1, y1, c):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if 0 <= x < im.width and 0 <= y < im.height:
                im.putpixel((x, y), c)


def sheet(frames):
    w, h = frames[0].size
    s = Image.new("RGBA", (w * len(frames), h))
    for i, fr in enumerate(frames):
        s.paste(fr, (i * w, 0))
    return s


# ---------- Feuer: 4 Frames a 16x16 ----------
RED, ORANGE, YELLOW = (200, 50, 30, 255), (240, 130, 30, 255), (255, 225, 90, 255)
LOG, LOG2 = (110, 70, 40, 255), (80, 50, 30, 255)


def fire_frame(f):
    im = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    h = [9, 10, 8, 10][f]
    sway = [0, 1, 0, -1][f]
    for i in range(h):
        y = 13 - i
        half = max(1, int(4 * (1 - i / h)) + 1)
        cx = 8 + sway * (i // 3)
        rect(im, cx - half, y, cx + half - 1, y, RED)
        if half >= 2:
            rect(im, cx - half + 1, y, cx + half - 2, y, ORANGE)
        if half >= 3 and i < h * 0.6:
            rect(im, cx - half + 2, y, cx + half - 3, y, YELLOW)
    rect(im, 2, 14, 13, 15, LOG)
    rect(im, 4, 14, 5, 15, LOG2)
    rect(im, 10, 14, 11, 15, LOG2)
    return im


os.makedirs(os.path.join(ROOT, "Assets"), exist_ok=True)
sheet([fire_frame(f) for f in range(4)]).save(os.path.join(ROOT, "Assets", "fire.png"))


# ---------- Charaktere: 16x24, je 4 Frames pro Animation ----------
def rgb(r, g, b):
    return (r, g, b, 255)


def char_frame(p, bob=0, arms_up=False, jump=0, blink=False):
    im = Image.new("RGBA", (16, 24), (0, 0, 0, 0))
    oy = -jump
    # Kopf mit Kapuze
    rect(im, 5, 6 + oy + bob, 10, 11 + oy + bob, p["hood"])
    rect(im, 8, 8 + oy + bob, 10, 10 + oy + bob, p["skin"])
    rect(im, 9, 9 + oy + bob, 9, 9 + oy + bob, p["skin"] if blink else p["dark"])
    # optional: Hut mit Feder
    if "hat" in p:
        rect(im, 4, 6 + oy + bob, 11, 6 + oy + bob, p["hat"])
        rect(im, 6, 3 + oy + bob, 9, 5 + oy + bob, p["hat"])
        rect(im, 10, 2 + oy + bob, 10, 4 + oy + bob, p["feather"])
    # Koerper (+ optional Schal)
    rect(im, 4, 12 + oy, 11, 20 + oy, p["coat"])
    if "scarf" in p:
        rect(im, 4, 12 + oy, 11, 13 + oy, p["scarf"])
    # Arme
    if arms_up:
        rect(im, 2, 7 + oy, 3, 12 + oy, p["coat"])
        rect(im, 12, 7 + oy, 13, 12 + oy, p["coat"])
        rect(im, 2, 6 + oy, 2, 6 + oy, p["skin"])
        rect(im, 13, 6 + oy, 13, 6 + oy, p["skin"])
    else:
        rect(im, 3, 13 + oy, 4, 18 + oy, p["coat"])
        rect(im, 11, 13 + oy, 12, 18 + oy, p["coat"])
    # Beine (sitzend, nach rechts zum Feuer)
    rect(im, 5, 21 + oy, 12, 22 + oy, p["pants"])
    rect(im, 12, 21 + oy, 14, 23 + oy, p["boot"])
    return im


def save_outfit(char_id, outfit, palette):
    d = os.path.join(ROOT, "Characters", char_id, "outfits", outfit)
    os.makedirs(d, exist_ok=True)
    idle = [char_frame(palette, 0), char_frame(palette, 0), char_frame(palette, 1), char_frame(palette, 1, blink=True)]
    react = [char_frame(palette, 0, True, 0), char_frame(palette, 0, True, 2),
             char_frame(palette, 0, True, 3), char_frame(palette, 0, True, 1)]
    sheet(idle).save(os.path.join(d, "idle.png"))
    sheet(react).save(os.path.join(d, "react.png"))


BASE = dict(skin=rgb(240, 200, 160), pants=rgb(70, 60, 50), boot=rgb(40, 30, 25), dark=rgb(20, 20, 30))

save_outfit("wanderer", "default", {**BASE, "hood": rgb(60, 90, 140), "coat": rgb(50, 70, 110)})
save_outfit("wanderer", "winter", {**BASE, "hood": rgb(225, 230, 240), "coat": rgb(110, 140, 185), "scarf": rgb(190, 50, 50)})
save_outfit("pip", "default", {**BASE, "hood": rgb(80, 130, 80), "coat": rgb(170, 120, 50), "pants": rgb(90, 60, 50),
                               "hat": rgb(50, 90, 50), "feather": rgb(220, 60, 60)})
print("ok")
