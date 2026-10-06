from PIL import Image

def rect(im, x0, y0, x1, y1, c):
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if 0 <= x < im.width and 0 <= y < im.height:
                im.putpixel((x, y), c)

# ---------- Feuer: 4 Frames à 16x16 ----------
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

sheet = Image.new("RGBA", (16 * 4, 16))
for f in range(4):
    sheet.paste(fire_frame(f), (f * 16, 0))
sheet.save("Assets/fire.png")

# ---------- Charakter: 16x24, je 4 Frames ----------
HOOD, SKIN, COAT, PANTS, BOOT, DARK = (60, 90, 140, 255), (240, 200, 160, 255), (50, 70, 110, 255), (70, 60, 50, 255), (40, 30, 25, 255), (20, 20, 30, 255)

def char_frame(bob=0, arms_up=False, jump=0, blink=False):
    im = Image.new("RGBA", (16, 24), (0, 0, 0, 0))
    oy = -jump
    # Kopf mit Kapuze
    rect(im, 5, 6 + oy + bob, 10, 11 + oy + bob, HOOD)
    rect(im, 8, 8 + oy + bob, 10, 10 + oy + bob, SKIN)
    im.putpixel((9, 9 + oy + bob), DARK if not blink else SKIN)
    # Koerper
    rect(im, 4, 12 + oy, 11, 20 + oy, COAT)
    # Arme
    if arms_up:
        rect(im, 2, 7 + oy, 3, 12 + oy, COAT)
        rect(im, 12, 7 + oy, 13, 12 + oy, COAT)
        im.putpixel((2, 6 + oy), SKIN)
        im.putpixel((13, 6 + oy), SKIN)
    else:
        rect(im, 3, 13 + oy, 4, 18 + oy, COAT)
        rect(im, 11, 13 + oy, 12, 18 + oy, COAT)
    # Beine (sitzend, nach rechts zum Feuer)
    rect(im, 5, 21 + oy, 12, 22 + oy, PANTS)
    rect(im, 12, 21 + oy, 14, 23 + oy, BOOT)
    return im

idle = [char_frame(0), char_frame(0), char_frame(1), char_frame(1, blink=True)]
react = [char_frame(0, True, 0), char_frame(0, True, 2), char_frame(0, True, 3), char_frame(0, True, 1)]
for name, frames in (("char_idle", idle), ("char_react", react)):
    s = Image.new("RGBA", (16 * len(frames), 24))
    for i, fr in enumerate(frames):
        s.paste(fr, (i * 16, 0))
    s.save(f"Assets/{name}.png")
print("ok")
