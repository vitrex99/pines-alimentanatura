"""Crea pins.json (ids 001-150 y foto de cada pin) y fotos reducidas para render.js.
Uso: python3 preparar.py <carpeta_fotos_reducidas>"""
import json, os, sys
from PIL import Image
import pines
here = os.path.dirname(os.path.abspath(__file__))
raiz = os.path.dirname(here)
dest = sys.argv[1]
os.makedirs(dest, exist_ok=True)
idx = {}
for l in open(os.path.join(raiz, 'fotos-index.txt')):
    n, f = l.split(maxsplit=1)
    idx[int(n)] = f.strip()
for i, p in enumerate(pines.PINS):
    p['id'] = f'{i+1:03d}'
    p['foto_src'] = idx[p['foto']]
    p['foto_file'] = f"{p['foto']}.jpg"
    out = os.path.join(dest, p['foto_file'])
    if not os.path.exists(out):
        im = Image.open(os.path.join(raiz, idx[p['foto']])).convert('RGB')
        im.thumbnail((1400, 1400))
        im.save(out, quality=88)
json.dump(pines.PINS, open(os.path.join(here, 'pins.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(pines.PINS), 'pines')
