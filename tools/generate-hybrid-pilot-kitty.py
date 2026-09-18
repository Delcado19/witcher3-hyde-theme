#!/usr/bin/env python3
"""Generate the deterministic Kitty raster artwork for the Hero crossover pilot.

Creates a 1024x1024 detailed raster master plus size-specific pilot derivatives
for 32, 48, 64, 96, 128, 256, and 512 px.

Requires Pillow.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import math
import random

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

SIZES = (32, 48, 64, 96, 128, 256, 512)


def build_master() -> Image.Image:
    side = 2048
    random.seed(883)
    img = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img, "RGBA")

    def polygon(points, fill, outline=None, width=1):
        draw.polygon(points, fill=fill)
        if outline:
            draw.line(points + [points[0]], fill=outline, width=width, joint="curve")

    def rounded(box, radius, fill, outline=None, width=1):
        draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

    def line(points, fill, width):
        draw.line(points, fill=fill, width=width, joint="curve")

    shadow = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow, "RGBA")
    shadow_draw.ellipse((290, 250, 1760, 1760), fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(65))
    img.alpha_composite(shadow)
    draw = ImageDraw.Draw(img, "RGBA")

    polygon([(370,500),(455,180),(690,355),(512,560)], (51,50,49,255), (167,171,174,255), 24)
    polygon([(1650,500),(1565,180),(1330,355),(1508,560)], (51,50,49,255), (167,171,174,255), 24)
    polygon([(430,430),(490,255),(620,355),(520,500)], (50,33,23,255), (114,76,43,255), 14)
    polygon([(1590,430),(1530,255),(1400,355),(1500,500)], (50,33,23,255), (114,76,43,255), 14)

    for box, fill, outline, width in (
        ((300,300,1720,1720),(58,58,58,255),(190,195,199,255),28),
        ((365,365,1655,1655),(178,184,188,255),(46,47,48,255),18),
        ((440,440,1580,1580),(27,29,31,255),(93,98,101,255),22),
    ):
        draw.ellipse(box, fill=fill, outline=outline, width=width)

    cx = cy = 1010
    for angle in range(0, 360, 15):
        rad = math.radians(angle)
        r1, r2 = 584, 628
        line(
            [
                (cx + math.cos(rad)*r1, cy + math.sin(rad)*r1),
                (cx + math.cos(rad)*r2, cy + math.sin(rad)*r2),
            ],
            (215,220,224,80),
            7,
        )

    face = [(600,820),(710,610),(860,685),(1010,610),(1160,685),(1310,610),(1420,820),(1360,1250),(1010,1470),(660,1250)]
    polygon(face, (39,41,43,255), (112,118,121,255), 22)
    inner = [(660,845),(735,675),(865,742),(1010,678),(1155,742),(1285,675),(1360,845),(1300,1205),(1010,1395),(720,1205)]
    polygon(inner, (12,20,25,255), (42,49,53,255), 14)

    polygon([(710,865),(870,820),(970,890),(850,1000)], (79,83,85,255), (167,174,178,170), 10)
    polygon([(1310,865),(1150,820),(1050,890),(1170,1000)], (79,83,85,255), (167,174,178,170), 10)
    polygon([(760,1105),(910,1180),(820,1270),(700,1180)], (49,52,54,255), (105,110,113,180), 9)
    polygon([(1260,1105),(1110,1180),(1200,1270),(1320,1180)], (49,52,54,255), (105,110,113,180), 9)

    for eye_x in (830, 1190):
        glow = Image.new("RGBA", (side, side), (0,0,0,0))
        glow_draw = ImageDraw.Draw(glow, "RGBA")
        glow_draw.ellipse((eye_x-95,845,eye_x+95,955), fill=(213,142,77,90))
        glow = glow.filter(ImageFilter.GaussianBlur(28))
        img.alpha_composite(glow)
        draw = ImageDraw.Draw(img, "RGBA")
        polygon([(eye_x-86,900),(eye_x,855),(eye_x+86,900),(eye_x,945)], (165,101,45,255), (231,185,101,255), 9)
        draw.ellipse((eye_x-15,875,eye_x+15,925), fill=(10,12,13,255))
        draw.ellipse((eye_x-6,880,eye_x+3,890), fill=(245,235,198,180))

    polygon([(1010,980),(1080,1035),(1010,1095),(940,1035)], (215,221,224,255), (80,84,87,255), 8)
    line([(875,1090),(1010,1145),(1145,1090)], (166,171,175,255), 18)
    polygon([(900,1120),(955,1140),(928,1205)], (225,229,231,255), (90,94,96,255), 5)
    polygon([(1120,1120),(1065,1140),(1092,1205)], (225,229,231,255), (90,94,96,255), 5)
    polygon([(960,1170),(1010,1195),(1060,1170),(1010,1260)], (146,38,25,255), (203,74,53,255), 6)

    polygon([(1010,720),(1080,785),(1055,865),(1010,905),(965,865),(940,785)], (96,25,18,255), (189,49,31,255), 14)
    polygon([(980,788),(1010,758),(1040,788),(1010,850)], (222,230,234,255))

    rounded((420,1570,1600,1835), 56, (45,46,47,255), (149,154,158,255), 22)
    rounded((478,1625,1542,1780), 30, (11,22,28,255), (30,34,37,255), 10)
    line([(595,1670),(690,1710),(595,1750)], (49,136,166,255), 28)
    line([(760,1744),(1135,1744)], (222,230,240,255), 24)
    draw.ellipse((1430,1680,1480,1730), fill=(98,22,12,255), outline=(190,44,27,255), width=8)
    draw.ellipse((1445,1695,1465,1715), fill=(244,119,83,220))

    texture = Image.new("RGBA", (side, side), (0,0,0,0))
    texture_draw = ImageDraw.Draw(texture, "RGBA")
    for _ in range(18000):
        x = random.randint(330,1690)
        y = random.randint(320,1810)
        color = random.choice(((230,232,228,9),(0,0,0,14),(104,73,42,10),(49,136,166,6)))
        texture_draw.point((x,y), fill=color)
    for _ in range(420):
        x = random.randint(390,1610)
        y = random.randint(410,1760)
        length = random.randint(12,110)
        angle = random.uniform(-0.6,0.6)
        x2 = x + math.cos(angle)*length
        y2 = y + math.sin(angle)*length
        color = random.choice(((228,230,232,22),(8,8,8,40),(131,87,44,18)))
        texture_draw.line((x,y,x2,y2), fill=color, width=random.choice((1,2,3)))
    texture = texture.filter(ImageFilter.GaussianBlur(0.3))
    img.alpha_composite(texture)

    mask = Image.new("L", (side, side), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((500,500,1520,1520), fill=50)
    glow = Image.new("RGBA", (side, side), (49,136,166,0))
    glow.putalpha(mask.filter(ImageFilter.GaussianBlur(85)))
    img = Image.alpha_composite(glow, img)

    vignette = Image.new("RGBA", (side, side), (0,0,0,0))
    vignette_draw = ImageDraw.Draw(vignette, "RGBA")
    for i in range(160):
        alpha = int(65 * (i / 160) ** 1.6)
        vignette_draw.rectangle((i,i,side-i-1,side-i-1), outline=(0,0,0,alpha), width=1)
    img = Image.alpha_composite(img, vignette)

    master = img.resize((1024,1024), Image.Resampling.LANCZOS)
    master = ImageEnhance.Contrast(master).enhance(1.06)
    return master.filter(ImageFilter.UnsharpMask(radius=1.2, percent=115, threshold=3))


def export_derivatives(master: Image.Image, output_dir: Path) -> None:
    optimized_dir = output_dir / "optimized"
    optimized_dir.mkdir(parents=True, exist_ok=True)
    for size in SIZES:
        image = master.resize((size,size), Image.Resampling.LANCZOS)
        if size <= 48:
            image = ImageEnhance.Contrast(image).enhance(1.18)
            image = image.filter(ImageFilter.UnsharpMask(0.65, 175, 2))
        elif size <= 96:
            image = ImageEnhance.Contrast(image).enhance(1.12)
            image = image.filter(ImageFilter.UnsharpMask(0.85, 150, 2))
        elif size <= 128:
            image = ImageEnhance.Contrast(image).enhance(1.08)
            image = image.filter(ImageFilter.UnsharpMask(1.0, 130, 2))
        else:
            image = image.filter(ImageFilter.UnsharpMask(1.1, 105, 3))
        image.save(optimized_dir / f"{size}.png", optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("build/icons/hybrid-pilot/kitty"))
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    master = build_master()
    master.save(args.output_dir / "kitty-master.png", optimize=True)
    export_derivatives(master, args.output_dir)
    print(f"Wrote Kitty master and derivatives to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
