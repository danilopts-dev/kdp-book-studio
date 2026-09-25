"""Junta PNGs de preview numa folha só (1 imagem = bem menos tokens para inspeção visual)."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw

files = sorted(Path(sys.argv[1]).glob("p*.png"))
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
ims = [Image.open(f).convert("RGB") for f in files]
w, h = max(i.width for i in ims), max(i.height for i in ims)
rows = (len(ims) + cols - 1) // cols
sheet = Image.new("RGB", (cols * (w + 10) + 10, rows * (h + 30) + 10), "#888")
d = ImageDraw.Draw(sheet)
for k, (f, im) in enumerate(zip(files, ims)):
    x, y = 10 + (k % cols) * (w + 10), 10 + (k // cols) * (h + 30)
    sheet.paste(im, (x, y + 20))
    d.text((x, y + 4), f.stem, fill="white")
sheet.save(sys.argv[2])
print(sys.argv[2], sheet.size)
