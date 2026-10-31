"""Lote 2: reparte los 150 pines en 30 días (5 al día, del 1-11 al 30-11-2026) y crea los CSV de Pinterest.
Uso: python3 hacer_csv.py https://raw.githubusercontent.com/vitrex99/pines-alimentanatura/main  (junta lote 1 y lote 2 en un solo CSV)
Horas en UTC. España en invierno es UTC+1: 08:00, 11:30, 14:30, 18:00 y 21:00."""
import json, csv, sys, os, datetime as dt
base = sys.argv[1].rstrip('/')
here = os.path.dirname(os.path.abspath(__file__))
pins = json.load(open(os.path.join(here, 'pins.json'), encoding='utf-8'))
for p in pins:
    p['lote'] = '02'
# El lote 1 (10 pines) entra en el mismo calendario: un sexto pin cada 3 días.
indice = {}
for l in open(os.path.join(os.path.dirname(here), 'fotos-index.txt')):
    n, ruta = l.split(maxsplit=1); indice[ruta.strip()] = int(n)
for p in json.load(open(os.path.join(os.path.dirname(here), 'lote-01', 'pins.json'), encoding='utf-8')):
    p['lote'] = '01'; p['foto'] = indice.get('fotos/' + p['foto'], p['foto'])
    pins.append(p)

HORAS = ['07:00', '10:30', '13:30', '17:00', '20:00']
DIA0 = dt.date(2026, 11, 1)
NAVIDAD_DESDE = dt.date(2026, 11, 15)

KW_TABLERO = {
    'Recetas bajas en FODMAP': 'recetas bajas en fodmap, recetas sibo, dieta fodmap',
    'Dieta baja en FODMAP: qué comer': 'dieta baja en fodmap, alimentos fodmap, sibo',
    'SIBO: guías y dudas': 'sibo, sobrecrecimiento bacteriano, dieta sibo',
    'Postres bajos en FODMAP': 'postres bajos en fodmap, postres sin lactosa, sibo',
    'Desayunos bajos en FODMAP': 'desayunos bajos en fodmap, desayuno sibo, dieta fodmap',
    'Navidad baja en FODMAP': 'navidad fodmap, menu navidad sibo, recetas navidad sin ajo',
    'Colon irritable: qué comer': 'colon irritable, que comer con colon irritable, dieta fodmap',
    'Raciones: Universidad de Monash': 'monash fodmap, raciones fodmap, dieta fodmap',
}

def es_navidad(p):
    return 'navidad' in p['url']

# Reparto voraz: nunca dos pines del mismo artículo el mismo día, Navidad desde el 15-11,
# y se alejan lo posible las repeticiones de foto y de artículo.
pendientes = list(pins)
plan, ult_foto, ult_art = [], {}, {}
for d in range(30):
    dia = DIA0 + dt.timedelta(days=d)
    hoy = set()
    dias_restantes = 30 - d
    for h in (HORAS[:3] + ['15:30'] + HORAS[3:] if d % 3 == 0 else HORAS):
        def nota(p):
            if p['url'] in hoy or (es_navidad(p) and dia < NAVIDAD_DESDE):
                return None
            s = min(d - ult_foto.get(p['foto'], -99), 6) * 3 + min(d - ult_art.get(p['url'], -99), 6)
            # prioridad a los artículos con muchos pines por repartir, para que no se acumulen al final
            quedan = sum(q['url'] == p['url'] for q in pendientes)
            hueco = (dia_fin - (max(dia, NAVIDAD_DESDE) if es_navidad(p) else dia)).days + 1
            s += 40 * quedan / max(1, hueco)
            return s
        dia_fin = DIA0 + dt.timedelta(days=29)
        cand = [(nota(p), i) for i, p in enumerate(pendientes)]
        cand = [c for c in cand if c[0] is not None]
        _, i = max(cand)
        p = pendientes.pop(i)
        hoy.add(p['url']); ult_foto[p['foto']] = d; ult_art[p['url']] = d
        plan.append((p, f"{dia.isoformat()}T{h}:00"))
assert not pendientes and len(plan) == 160

def fila(p, when):
    link = (f"https://alimentanatura.com/blogs/sibo/{p['url']}?utm_source=pinterest&utm_medium=social"
            f"&utm_campaign=pines-lote-{p['lote']}&utm_content=pin-{p['id']}")
    img = f"{base}/lote-02/pin-{p['id']}.jpg" if p['lote'] == '02' else f"{base}/lote-01/pin-{p['id']}.png"
    assert len(p['pin_title']) <= 100 and len(p['desc']) <= 500, p['id']
    return [p['pin_title'], img, p['board'], '', p['desc'], link, when, KW_TABLERO[p['board']]]

CAB = ['Title', 'Media URL', 'Pinterest board', 'Thumbnail', 'Description', 'Link', 'Publish date', 'Keywords']
for nombre, filas in [('pinterest-subida-noviembre.csv', plan)]:
    with open(os.path.join(here, nombre), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(CAB)
        for p, when in filas:
            w.writerow(fila(p, when))
json.dump([{'lote': p['lote'], 'id': p['id'], 'fecha_utc': when} for p, when in plan],
          open(os.path.join(here, 'calendario.json'), 'w'), indent=1)
print('CSV creados. Primer pin:', plan[0][1], ' Último:', plan[-1][1])
