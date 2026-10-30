"""Genera el CSV de subida masiva de Pinterest a partir de pins.json.
Uso: python3 hacer_csv.py <url_base_imagenes>
Ejemplo de url base: https://raw.githubusercontent.com/USUARIO/pines-alimentanatura/main/lote-01
Horas en UTC (España en invierno = UTC+1)."""
import json, csv, sys, os
base = sys.argv[1].rstrip('/')
here = os.path.dirname(os.path.abspath(__file__))
pins = {p['id']: p for p in json.load(open(os.path.join(here, 'pins.json'), encoding='utf-8'))}
KW = {'01':'verduras bajas en fodmap, dieta fodmap, lista fodmap, sibo, colon irritable',
      '02':'frutas bajas en fodmap, frutas permitidas sibo, dieta fodmap, colon irritable',
      '03':'platano fodmap, platano sibo, frutas bajas en fodmap, dieta fodmap',
      '04':'pan sibo, pan bajo en fodmap, masa madre fodmap, colon irritable',
      '05':'pan sin gluten fodmap, dieta baja en fodmap, inulina, sibo',
      '06':'pan sin gluten casero, receta baja en fodmap, pan sin amasar, sibo',
      '07':'tortilla de patatas sin cebolla, receta baja en fodmap, sibo, colon irritable',
      '08':'calabaza sibo, sopa de calabaza, receta baja en fodmap, dieta fodmap',
      '09':'mousse de chocolate, postre bajo en fodmap, postre sin lactosa, sibo',
      '10':'desayuno bajo en fodmap, desayuno sibo, dieta fodmap, colon irritable'}
# (id, fecha y hora UTC). 3 pines al día a 08:30, 13:30 y 20:30 hora de España.
PLAN = [('01','2026-11-02T07:30:00'),('04','2026-11-02T12:30:00'),('07','2026-11-02T19:30:00'),
        ('02','2026-11-03T07:30:00'),('08','2026-11-03T12:30:00'),('09','2026-11-03T19:30:00'),
        ('05','2026-11-04T07:30:00'),('10','2026-11-04T12:30:00'),('03','2026-11-04T19:30:00'),
        ('06','2026-11-05T12:30:00')]
out = os.path.join(here, 'pinterest-subida-lote-01.csv')
with open(out, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['Title','Media URL','Pinterest board','Thumbnail','Description','Link','Publish date','Keywords'])
    for pid, when in PLAN:
        p = pins[pid]
        link = f"https://alimentanatura.com/blogs/sibo/{p['url']}?utm_source=pinterest&utm_medium=social&utm_campaign=pines-lote-01&utm_content=pin-{pid}"
        assert len(p['pin_title']) <= 100 and len(p['desc']) <= 500
        w.writerow([p['pin_title'], f"{base}/pin-{pid}.png", p['board'], '', p['desc'], link, when, KW[pid]])
print('CSV creado:', out)
