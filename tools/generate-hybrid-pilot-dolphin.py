#!/usr/bin/env python3
"""Generate the deterministic Dolphin raster artwork for the Hero crossover pilot.

This is pilot artwork tooling, not the final release raster pipeline. It creates:
- a 1024x1024 detailed raster master;
- size-specific pilot derivatives at 32, 48, 64, 96, 128, 256, and 512 px.

The derivatives receive modest size-specific contrast/sharpening so the pilot
compares intentional raster exports rather than a completely blind resize.

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
    scale = 2
    side = 1024 * scale
    random.seed(703)

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
    shadow_draw.rounded_rectangle((245, 190, 1805, 1790), radius=170, fill=(0, 0, 0, 170))
    shadow = shadow.filter(ImageFilter.GaussianBlur(55))
    img.alpha_composite(shadow)
    draw = ImageDraw.Draw(img, "RGBA")

    outer = [(245,285),(365,165),(1665,165),(1800,300),(1800,1625),(1680,1760),(365,1760),(245,1640)]
    polygon(outer, (44,44,45,255), (150,155,160,255), 26)
    inner = [(330,335),(405,260),(1602,260),(1715,365),(1715,1562),(1608,1662),(410,1662),(330,1588)]
    polygon(inner, (25,27,29,255), (82,85,89,255), 18)

    line([(275,315),(390,205),(1635,205),(1760,330)], (222,226,230,100), 14)
    line([(290,1610),(405,1715),(1632,1715),(1760,1590)], (0,0,0,150), 18)

    rounded((405,360,1625,930), 56, (17,24,28,255), (66,72,75,255), 16)
    rounded((450,408,1580,885), 38, (26,29,31,255), (12,14,16,255), 8)
    for y in range(420, 880, 10):
        alpha = max(0, 38 - int((y - 420) / 15))
        draw.rectangle((458, y, 1572, y + 10), fill=(80,90,96,alpha))

    rounded((405,1010,1625,1550), 42, (31,25,19,255), (89,63,38,255), 18)
    rounded((455,1065,1575,1488), 28, (40,34,29,255), (18,16,13,255), 10)
    line([(480,1240),(1550,1240)], (112,93,74,90), 8)
    rounded((650,1112,1370,1182), 30, (170,177,184,255), (40,43,46,255), 9)
    rounded((740,1368,1280,1422), 24, (149,154,159,220), (35,37,39,255), 8)

    for radius, color in ((44,(90,20,10,200)), (31,(184,42,24,255)), (14,(235,100,70,120))):
        draw.ellipse((1512-radius,1445-radius,1512+radius,1445+radius), fill=color)

    for x, y in ((360,320),(1660,340),(360,1580),(1665,1570),(530,230),(1480,230),(530,1690),(1480,1690)):
        draw.ellipse((x-18,y-18,x+18,y+18), fill=(120,126,131,255), outline=(220,225,230,100), width=4)
        draw.ellipse((x-8,y-8,x+2,y+2), fill=(230,235,240,120))

    body = [(560,790),(630,685),(760,600),(920,550),(1110,552),(1280,610),(1408,710),(1515,727),(1420,785),(1360,868),(1240,945),(1090,980),(900,960),(735,900),(620,825)]
    polygon(body, (35,126,161,255), (115,210,232,190), 12)
    polygon([(1380,705),(1595,720),(1432,790)], (34,119,153,255), (110,204,228,180), 8)
    polygon([(610,770),(470,650),(392,545),(540,590),(680,690)], (33,118,153,255), (110,204,228,150), 9)
    polygon([(628,815),(472,915),(388,1028),(548,968),(704,862)], (33,118,153,255), (110,204,228,150), 9)
    polygon([(1065,565),(1140,420),(1295,355),(1250,585)], (31,111,145,255), (104,195,220,160), 9)
    polygon([(915,870),(845,1018),(1040,908)], (192,214,222,220), (236,245,248,150), 7)

    draw.ellipse((1333,668,1377,712), fill=(6,11,14,255))
    draw.ellipse((1347,682,1363,698), fill=(230,240,244,255))
    line([(650,720),(780,635),(945,600),(1120,606),(1268,660)], (178,231,244,120), 18)
    line([(690,846),(850,910),(1050,928),(1210,890)], (6,52,70,140), 12)

    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        cx, cy = 1010, 765
        r1, r2 = 520, 575
        x1, y1 = cx + math.cos(rad)*r1, cy + math.sin(rad)*r1*0.56
        x2, y2 = cx + math.cos(rad)*r2, cy + math.sin(rad)*r2*0.56
        line([(x1,y1),(x2,y2)], (150,170,178,75), 6)

    texture = Image.new("RGBA", (side, side), (0,0,0,0))
    texture_draw = ImageDraw.Draw(texture, "RGBA")
    for _ in range(26000):
        x = random.randrange(245, 1800)
        y = random.randrange(165, 1760)
        color = random.choice(((220,220,210,10),(0,0,0,13),(93,72,49,11),(70,105,110,8)))
        texture_draw.point((x,y), fill=color)
    for _ in range(380):
        x = random.randint(300,1700)
        y = random.randint(220,1700)
        length = random.randint(12,90)
        angle = random.uniform(-0.45,0.45)
        x2 = x + math.cos(angle)*length
        y2 = y + math.sin(angle)*length
        color = random.choice(((215,220,222,25),(10,10,10,35),(120,90,55,24)))
        texture_draw.line((x,y,x2,y2), fill=color, width=random.choice((1,2,3)))
    texture = texture.filter(ImageFilter.GaussianBlur(0.35))
    img.alpha_composite(texture)

    mask = Image.new("L", (side, side), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((470,400,1580,1120), fill=70)
    glow = Image.new("RGBA", (side, side), (49,136,166,0))
    glow.putalpha(mask.filter(ImageFilter.GaussianBlur(70)))
    img = Image.alpha_composite(glow, img)

    vignette = Image.new("RGBA", (side, side), (0,0,0,0))
    vignette_draw = ImageDraw.Draw(vignette, "RGBA")
    for i in range(180):
        alpha = int(70 * (i / 180) ** 1.7)
        vignette_draw.rectangle((i,i,side-i-1,side-i-1), outline=(0,0,0,alpha), width=1)
    img = Image.alpha_composite(img, vignette)

    master = img.resize((1024,1024), Image.Resampling.LANCZOS)
    master = ImageEnhance.Contrast(master).enhance(1.05)
    return master.filter(ImageFilter.UnsharpMask(radius=1.25, percent=110, threshold=3))


def export_derivatives(master: Image.Image, output_dir: Path) -> None:
    optimized_dir = output_dir / "optimized"
    optimized_dir.mkdir(parents=True, exist_ok=True)

    for size in SIZES:
        image = master.resize((size,size), Image.Resampling.LANCZOS)
        if size <= 48:
            image = ImageEnhance.Contrast(image).enhance(1.17)
            image = image.filter(ImageFilter.UnsharpMask(0.65, 170, 2))
        elif size <= 96:
            image = ImageEnhance.Contrast(image).enhance(1.11)
            image = image.filter(ImageFilter.UnsharpMask(0.85, 145, 2))
        elif size <= 128:
            image = ImageEnhance.Contrast(image).enhance(1.08)
            image = image.filter(ImageFilter.UnsharpMask(1.0, 130, 2))
        else:
            image = image.filter(ImageFilter.UnsharpMask(1.1, 105, 3))
        image.save(optimized_dir / f"{size}.png", optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("build/icons/hybrid-pilot/dolphin"))
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    master = build_master()
    master.save(args.output_dir / "dolphin-master.png", optimize=True)
    export_derivatives(master, args.output_dir)

    print(f"Wrote Dolphin master and derivatives to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
