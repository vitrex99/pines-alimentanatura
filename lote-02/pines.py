# Lote 2: 150 pines. Cada pin: articulo (slug), plantilla, foto (indice de fotos-index), tablero,
# titulo y descripcion del pin, y los campos de la plantilla. Datos sacados de los articulos del blog.
R = 'Recetas bajas en FODMAP'
D = 'Dieta baja en FODMAP: qué comer'
S = 'SIBO: guías y dudas'
P = 'Postres bajos en FODMAP'
DE = 'Desayunos bajos en FODMAP'
N = 'Navidad baja en FODMAP'
C = 'Colon irritable: qué comer'
M = 'Raciones: Universidad de Monash'

PINS = []
def pin(slug, tpl, foto, board, pt, desc, **k):
    PINS.append(dict(url=slug, tpl=tpl, foto=foto, board=board, pin_title=pt, desc=desc, **k))

V = 'verduras-bajas-en-fodmap-lista-gramos'
pin(V, 'foto', 69, D, 'Verduras bajas en FODMAP: la lista con gramos para tu compra',
    'Zanahoria, patata y chirivía casi sin límite; calabacín a 65 g y berenjena, judías verdes, espinacas o pepino a 75 g por comida, según la Universidad de Monash. Guarda la lista completa de verduras bajas en FODMAP para SIBO y colon irritable.',
    kicker='Guía con gramos', title='Verduras bajas en FODMAP', sub='Cuánto puedes comer de cada una, según Monash')
pin(V, 'lista', 67, D, 'Verduras que conviene evitar en la fase de eliminación FODMAP',
    'Cebolla, ajo, puerro (parte blanca), espárragos, alcachofa, coliflor, champiñones frescos y guisantes: las verduras con más FODMAP que conviene apartar al principio de la dieta. En la guía tienes con qué sustituir cada una.',
    kicker='Mejor evitar al principio', title='Verduras altas en FODMAP', unit='Por qué dan problemas',
    rows=[['Cebolla, ajo, puerro blanco', 'fructanos'], ['Espárragos, alcachofa', 'fructanos'], ['Coliflor, champiñones', 'manitol'], ['Guisantes', 'GOS']], source='Basado en los datos de la Universidad de Monash')
pin(V, 'pregunta', 44, D, '¿Puedo comer tomate con SIBO? Las nuevas raciones del tomate',
    'El tomate ya no se considera libre de FODMAP: los análisis recientes de Monash sitúan el tomate común en 65 g (medio tomate) y el cherry en 45 g (3 unidades). Te explicamos cómo usarlo sin pasarte en la dieta baja en FODMAP.',
    kicker='Pregunta frecuente', title='¿Puedo comer tomate con SIBO?', answer=['Sí, pero en ración medida', 'Tomate común: 65 g (medio tomate)', 'Tomate cherry: 45 g (3 unidades)'], source=M)
pin(V, 'versus', 69, D, 'Pimiento rojo o verde en la dieta FODMAP: no tienen la misma ración',
    'El pimiento verde es bajo en FODMAP hasta 75 g por comida, pero el rojo solo hasta 43 g, según la Universidad de Monash. Un detalle que cambia mucho tus sofritos y ensaladas si sigues la dieta baja en FODMAP por SIBO o colon irritable.',
    kicker='¿Sabías que…?', title='Pimiento verde y rojo: raciones distintas', a=['Pimiento verde', 'por comida', 'hasta 75 g', 'ración cómoda'], b=['Pimiento rojo', 'por comida', 'hasta 43 g', 'ración más pequeña'], note='El rojo tiene más fructosa.', source=M)
pin(V, 'curiosidad', 26, D, 'Cocinar la cebolla no elimina sus FODMAP: lo que sí funciona',
    'La cebolla pochada sigue siendo alta en fructanos y un caldo hecho con cebolla conserva FODMAP aunque la retires. Lo que sí ayuda: verduras cocinadas, que muchas personas con SIBO toleran mejor que crudas. Guía completa de verduras bajas en FODMAP.',
    kicker='Error común', title='Cocinar una verdura no le quita los FODMAP', body='Lo que conviene saber:', list=['La cebolla pochada sigue alta en fructanos', 'Un caldo con cebolla conserva FODMAP', 'Las verduras cocinadas suelen sentar mejor'])
pin(V, 'pregunta', 67, D, '¿Puedo comer brócoli con SIBO? Sí, las cabezas y con medida',
    'El brócoli es bajo en FODMAP si comes solo las cabezas, hasta 75 g por comida según la Universidad de Monash. Te contamos qué verduras puedes tomar con SIBO o colon irritable y cuánto, en nuestra lista de verduras bajas en FODMAP con gramos.',
    kicker='Pregunta frecuente', title='¿Puedo comer brócoli con SIBO?', answer=['Sí, solo las cabezas', 'Hasta 75 g por comida', 'Mejor cocinado al principio'], source=M)
pin(V, 'lista', 69, D, 'Las verduras más seguras de la dieta FODMAP (sin límite práctico)',
    'Según la Universidad de Monash, la zanahoria, la patata y la chirivía no tienen límite práctico en la dieta baja en FODMAP, y la lechuga es muy segura. Son la base perfecta para llenar el plato con SIBO o colon irritable.',
    kicker='Para llenar el plato', title='Las verduras más seguras', unit='Ración baja por comida',
    rows=[['Zanahoria', 'sin límite práctico'], ['Patata', 'sin límite práctico'], ['Chirivía', 'sin límite práctico'], ['Lechuga romana', '75 g'], ['Col lombarda', '75 g']], source=M)
pin(V, 'curiosidad', 46, D, 'Salsa de tomate comprada y FODMAP: por qué conviene hacerla en casa',
    'Casi todas las salsas de tomate comerciales llevan ajo y cebolla, y Monash las clasifica como altas en FODMAP. El tomate triturado en lata es bajo hasta 100 g. Más trucos en la guía de verduras bajas en FODMAP.',
    kicker='Ojo con la etiqueta', title='La salsa de tomate comprada suele ser alta en FODMAP', body='Por qué y qué hacer:', list=['Casi todas llevan ajo y cebolla', 'Tomate triturado en lata: hasta 100 g', 'Hazla en casa con orégano'])

F = 'frutas-bajas-en-fodmap-permitidas-guia'
pin(F, 'lista', 17, D, 'Frutas bajas en FODMAP: cuántos gramos puedes comer de cada una',
    'Fresas hasta 65 g, frambuesas hasta 60 g, arándanos hasta 40 g, 2 kiwis verdes y plátano firme hasta 100 g, según la Universidad de Monash. La guía de frutas para la dieta baja en FODMAP, SIBO y colon irritable.',
    kicker='Guarda esta lista', title='Frutas bajas en FODMAP con gramos', unit='Ración baja por comida',
    rows=[['Fresas', '65 g'], ['Frambuesas', '60 g'], ['Arándanos', '40 g'], ['Kiwi verde', '2 uds (150 g)'], ['Plátano firme', '100 g']], source=M)
pin(F, 'curiosidad', 17, D, 'Por qué la manzana hincha y otras frutas no: fructosa y glucosa',
    'Cuando una fruta tiene más fructosa que glucosa, como la manzana, la pera o el mango, el intestino no la absorbe bien y fermenta. Por eso unas frutas sientan bien y otras no. Te lo explicamos en la guía de frutas bajas en FODMAP.',
    kicker='Así funciona', title='Por qué unas frutas hinchan y otras no', body='La clave es la fructosa libre:', list=['Manzana, pera y mango: exceso de fructosa', 'La glucosa ayuda a absorberla', 'Sin glucosa suficiente, fermenta'])
pin(F, 'versus', 17, D, 'Melón y dieta FODMAP: cantaloup o piel de sapo, ¿cuánto puedes comer?',
    'No todos los melones tienen la misma ración: el cantaloup o galia es bajo en FODMAP hasta 120 g y el melón piel de sapo baja a 90 g, según Monash. Más frutas con sus gramos en nuestra guía.',
    kicker='¿Sabías que…?', title='Dos melones, dos raciones', a=['Cantaloup o galia', 'una rodaja fina', 'hasta 120 g', 'por comida'], b=['Piel de sapo', 'melón blanco', 'hasta 90 g', 'por comida'], note='Pésalo las primeras veces.', source=M)
pin(F, 'curiosidad', 18, D, 'Compotas y batidos de fruta: por qué no reducen los FODMAP',
    'Cocinar la manzana o la pera ablanda la fibra pero no destruye los FODMAP, y un batido mezcla varias frutas en una sola toma. Dos errores frecuentes en la dieta baja en FODMAP que explicamos en la guía de frutas.',
    kicker='Error común', title='La fruta cocinada sigue teniendo FODMAP', body='Dos trampas habituales:', list=['Compotas: la fructosa sigue ahí', 'Batidos: varias frutas en una toma', 'Mejor fruta entera y medida'])
pin(F, 'pregunta', 45, D, '¿Puedo comer kiwi con SIBO? Sí, y hasta dos piezas',
    'El kiwi verde es bajo en FODMAP hasta 2 unidades medianas (unos 150 g), según la Universidad de Monash. Una de las frutas más cómodas para el desayuno si sigues la dieta baja en FODMAP por SIBO o colon irritable.',
    kicker='Pregunta frecuente', title='¿Puedo comer kiwi con SIBO?', answer=['Sí, es de las más cómodas', 'Kiwi verde: hasta 2 unidades', 'Unos 150 g por comida'], source=M)
pin(F, 'curiosidad', 18, D, 'La regla de las 3 horas entre raciones de fruta en la dieta FODMAP',
    'No comas dos raciones de fruta seguidas: si tomas fresas en el desayuno, espera 3 o 4 horas antes de la siguiente fruta. Es una forma sencilla de no acumular FODMAP. Más consejos en la guía de frutas bajas en FODMAP.',
    kicker='Truco práctico', title='Deja 3 horas entre raciones de fruta', body='Así evitas acumular FODMAP:', list=['Una ración de fruta por toma', 'Espera 3 o 4 horas hasta la siguiente', 'Cuidado al juntar frutas en el postre'])
pin(F, 'lista', 18, D, 'Frutas altas en FODMAP y con qué sustituirlas',
    'Ciruelas, melocotón, higos o dátiles concentran sorbitol o fructosa. Te proponemos alternativas bajas en FODMAP para cada una: arándanos, piña, mandarina o fresas. Guía completa con gramos de la Universidad de Monash.',
    kicker='Cambia esto por esto', title='Más frutas para cambiar', unit='En la fase de eliminación',
    rows=[['Ciruelas', 'arándanos frescos'], ['Melocotón, nectarina', 'piña o mandarina'], ['Higos', 'fresas con canela'], ['Dátiles, pasas', 'fruta fresca medida']], source='Basado en los datos de la Universidad de Monash')
pin(F, 'foto', 19, D, 'Cómo elegir el plátano si sigues la dieta baja en FODMAP',
    'Cómpralo con las puntas aún verdes y cómelo cuando esté amarillo y firme: así es bajo en FODMAP hasta 100 g. Cuando salen motas marrones acumula fructanos. La prueba del plátano y más trucos en la guía de frutas.',
    kicker='La prueba del plátano', title='Elige el plátano por su piel', sub='Amarillo y firme: hasta 100 g. Con motas: unos 35 g')

QP = 'que-pan-comer-con-sibo'
pin(QP, 'curiosidad', 49, D, 'Cómo reconocer un pan de masa madre de verdad en la panadería',
    'No todo lo que se vende como masa madre lo es: muchos panes llevan levadura añadida y fermentan en pocas horas, sin tiempo para reducir los fructanos. Fíjate en la lista de ingredientes. Guía completa del pan con SIBO.',
    kicker='Antes de comprar', title='Cómo reconocer una masa madre de verdad', body='Mira la etiqueta:', list=['Solo harina, agua, sal y masa madre', 'Si pone «levadura», fermentación rápida', 'Desconfía del pan de molde «de masa madre»'])
pin(QP, 'versus', 48, D, 'Pan con SIBO: masa madre de espelta sí, espelta normal no',
    'La espelta moderna tiene tantos FODMAP como el trigo; solo la espelta de masa madre tradicional ha dado baja en FODMAP en los análisis de Monash, hasta 2 rebanadas. Guía del pan con SIBO y colon irritable.',
    kicker='¿Sabías que…?', title='Espelta: depende de cómo se haga', a=['Masa madre de espelta', 'fermentación larga', '2 rebanadas', 'baja en FODMAP'], b=['Espelta sin masa madre', 'fermentación rápida', 'Evitar', 'tantos FODMAP como el trigo'], note='La fermentación larga reduce los fructanos.', source=M)
pin(QP, 'curiosidad', 50, D, 'Una rebanada de pan integral normal también es baja en FODMAP',
    'Según Monash, una rebanada de pan integral de trigo normal (24 g) es baja en FODMAP: el problema aparece con la ración completa. La dieta baja en FODMAP va de cantidades, no de prohibiciones. Guía del pan con SIBO.',
    kicker='Dato poco conocido', title='Una rebanada de pan integral no suele ser un problema', body='La dieta FODMAP va de cantidades:', list=['1 rebanada de integral (24 g): baja', 'El problema es la ración completa', 'Media taza de pasta de trigo, igual'], source=M)
pin(QP, 'lista', 49, D, 'Qué pan evitar con SIBO en la fase de eliminación',
    'El pan de trigo normal en ración habitual, el pan de centeno (incluso de masa madre) y la espelta sin masa madre son los que conviene evitar al principio. Tabla completa de panes con sus raciones en la guía.',
    kicker='Fase de eliminación', title='Panes que conviene evitar al principio', unit='Por qué',
    rows=[['Trigo normal, ración habitual', 'fructanos'], ['Centeno', 'también de masa madre'], ['Espelta sin masa madre', 'como el trigo'], ['Panes con inulina', 'fructano puro']], source='Basado en los datos de la Universidad de Monash')
pin(QP, 'foto', 50, DE, 'Ideas de tostadas para SIBO: masa madre con huevo y espinacas',
    'Dos rebanadas de masa madre tradicional, huevo revuelto y espinacas: una tostada baja en FODMAP para desayunar con SIBO o colon irritable. Más ideas de tostadas y bocadillos en nuestra guía del pan.',
    kicker='Idea de desayuno', title='Tostada de masa madre con huevo y espinacas', sub='Hasta 2 rebanadas de masa madre tradicional')
pin(QP, 'curiosidad', 49, D, 'El efecto acumulación: cuando juntar alimentos aptos da síntomas',
    'Pan de masa madre, un poco de pasta de trigo y calabacín en la misma comida suman fructanos de varias fuentes. Es el efecto acumulación. En esas comidas mejor pan sin gluten o tortitas de arroz. Lo explicamos en la guía del pan.',
    kicker='Error común', title='Cuidado con sumar fructanos en la misma comida', body='Ejemplo de acumulación:', list=['Pan de masa madre', 'Un poco de pasta de trigo', 'Calabacín en cantidad'])

PS = 'pan-sin-gluten-bajo-en-fodmap-casero'
pin(PS, 'foto', 35, R, 'Pan casero sin gluten y bajo en FODMAP, sin amasar',
    'Harina de arroz, trigo sarraceno, tapioca y psyllium: un pan sin gluten de miga tierna que se hace sin amasar. Apto para la dieta baja en FODMAP, SIBO y colon irritable. Receta con gramos y paso a paso.',
    kicker='Receta fácil', title='Pan sin gluten sin amasar', sub='Bajo en FODMAP, de miga tierna y para toda la semana')
pin(PS, 'receta', 36, R, 'Pan sin gluten bajo en FODMAP: ingredientes y truco del psyllium',
    'La cáscara de psyllium sustituye al gluten y da una miga que no se desmorona. Sin trigo, centeno, legumbres, miel ni inulina. Receta de pan casero bajo en FODMAP para SIBO, con gramos y paso a paso.',
    kicker='Receta casera', title='Pan sin gluten para tostadas', chips=['Sin amasar', 'Sin inulina'], ing=['250 g harina de arroz', '100 g trigo sarraceno', 'Almidón de tapioca', 'Cáscara de psyllium'], tip='El psyllium hace de gluten: la miga no se desmorona.')
pin(PS, 'curiosidad', 34, D, 'Trigo sarraceno: a pesar del nombre, no es trigo',
    'El trigo sarraceno no tiene relación con el trigo y es apto en la dieta baja en FODMAP. Da sabor a pan de verdad en nuestra receta de pan casero sin gluten para SIBO y colon irritable.',
    kicker='¿Sabías que…?', title='El trigo sarraceno no es trigo', body='Por qué lo usamos en el pan:', list=['No tiene relación con el trigo', 'Da sabor y color a pan de verdad', 'Combina bien con harina de arroz'])
pin(PS, 'foto', 36, DE, 'Tostadas con tomate en pan sin gluten bajo en FODMAP',
    'Tu pan con tomate de siempre, en versión sin gluten y baja en FODMAP: pan casero de harina de arroz y trigo sarraceno. Recuerda que el tomate común es bajo hasta medio tomate por comida.',
    kicker='Desayuno de siempre', title='Pan con tomate apto para SIBO', sub='Con pan casero sin gluten y medio tomate')

T = 'tortilla-de-patatas-sin-cebolla-fodmap'
pin(T, 'foto', 66, R, 'Tortilla de patatas sin cebolla: receta jugosa y baja en FODMAP',
    'Patatas pochadas despacio en aceite de oliva y la parte verde de la cebolleta para el aroma. Una tortilla de patatas sin cebolla apta para la dieta baja en FODMAP, SIBO y colon irritable.',
    kicker='Clásico adaptado', title='Tortilla de patatas sin cebolla', sub='Jugosa, con el truco de la cebolleta')
pin(T, 'pregunta', 64, D, '¿Puedo comer patata con SIBO? Sí, y en raciones normales',
    'Según Monash, la patata no contiene FODMAP en cantidades detectables, así que puedes comerla en raciones normales. Es la base perfecta para llenar el plato con SIBO o colon irritable, como en nuestra tortilla sin cebolla.',
    kicker='Pregunta frecuente', title='¿Puedo comer patata con SIBO?', answer=['Sí, en raciones normales', 'Monash no detecta FODMAP', 'Ideal para llenar el plato'], source=M)
pin(T, 'curiosidad', 65, D, 'Por qué la cebolla sienta mal (y cómo sustituirla en la tortilla)',
    'La cebolla es de los alimentos más altos en fructanos, cruda, pochada o caramelizada. La parte verde de la cebolleta da aroma sin esos fructanos. Así hacemos la tortilla de patatas apta para SIBO.',
    kicker='Truco de cocina', title='Cómo quitar la cebolla sin perder sabor', body='La clave:', list=['La cebolla es alta en fructanos', 'Cocinarla no los elimina', 'Usa la parte verde de la cebolleta'])
pin(T, 'receta', 64, R, 'Tortilla de patatas baja en FODMAP: ingredientes y truco',
    'Patatas pochadas lentamente, huevos, aceite de oliva y parte verde de la cebolleta. La tortilla de patatas de siempre, apta para la dieta baja en FODMAP, con gramos y paso a paso.',
    kicker='Receta paso a paso', title='La tortilla de siempre, sin cebolla', chips=['Baja en FODMAP', 'Para tuppers'], ing=['Patatas', 'Huevos', 'Aceite de oliva', 'Verde de cebolleta'], tip='Pocha las patatas a fuego lento para que quede jugosa.')
pin(T, 'pregunta', 66, D, '¿La tortilla del bar es apta para SIBO?',
    'La tortilla de bar casi siempre lleva cebolla, que es alta en fructanos. Si quieres tortilla apta para SIBO o colon irritable, mejor hacerla en casa sin cebolla. Receta y dudas frecuentes en el artículo.',
    kicker='Pregunta frecuente', title='¿Puedo pedir tortilla en el bar?', answer=['Casi siempre lleva cebolla', 'Pregunta antes de pedir', 'Mejor la casera sin cebolla'])

LE = 'lentejas-bajas-en-fodmap-receta'
pin(LE, 'foto', 25, R, 'Lentejas bajas en FODMAP: la receta para comerlas con SIBO',
    'Lentejas de bote bien enjuagadas, patata, zanahoria y sin cebolla: un plato de cuchara bajo en FODMAP, unos 75 g de lentejas por ración. Receta paso a paso en 35 minutos, también con arroz.',
    kicker='Receta de cuchara', title='Lentejas estofadas aptas para SIBO', sub='Con lentejas de bote y sin cebolla')
pin(LE, 'curiosidad', 24, D, 'El truco para comer lentejas con SIBO: enjuagarlas',
    'Los GOS de las lentejas son solubles en agua: en las de bote, parte pasa al líquido de conserva. Si lo tiras y las enjuagas, eliminas una parte importante. Por eso son bajas en FODMAP hasta unos 76 g, según Monash.',
    kicker='El truco', title='Enjuaga las lentejas de bote', body='Por qué funciona:', list=['Los GOS se disuelven en agua', 'Pasan al líquido de la conserva', 'Tíralo y enjuágalas bien'], source=M)
pin(LE, 'lista', 25, D, 'Lentejas y FODMAP: de bote, rojas o pardinas, cuánto puedes comer',
    'Lentejas de bote enjuagadas hasta unos 76 g, rojas secas cocidas hasta 57 g y verdes o pardinas cocidas hasta 34 g por comida, según los umbrales de Monash. Con SIBO, mejor de bote.',
    kicker='Raciones por comida', title='Cuántas lentejas puedes comer', unit='Escurridas, por comida',
    rows=[['Lentejas de bote enjuagadas', 'unos 76 g'], ['Rojas secas, cocidas', 'unos 57 g'], ['Verdes o pardinas, cocidas', 'unos 34 g']], source=M)
pin(LE, 'foto', 24, R, 'Lentejas con arroz bajas en FODMAP: el plato que más cunde',
    'Las lentejas con arroz son un clásico y una forma perfecta de comer lentejas con SIBO: el arroz es bajo en FODMAP y el plato cunde con la misma cantidad de lentejas. Versión con arroz en la receta.',
    kicker='Versión con arroz', title='Lentejas con arroz para SIBO', sub='Más plato con la misma ración de lentejas')
pin(LE, 'curiosidad', 25, D, 'Por qué no conviene quitar las legumbres durante meses',
    'Las lentejas aportan proteína vegetal, fibra, hierro y folatos, y su fibra alimenta a las bacterias beneficiosas del colon. La dieta baja en FODMAP no las prohíbe: busca la cantidad que toleras.',
    kicker='Para pensarlo', title='No quites las legumbres para siempre', body='Lo que aportan las lentejas:', list=['Proteína vegetal y fibra', 'Hierro y folatos', 'Alimento para las bacterias del colon'])
pin(LE, 'pregunta', 24, D, '¿Puedo comer lentejas con SIBO? Sí, con este truco',
    'Sí: lentejas de bote enjuagadas, unos 75 g por ración, guisadas sin cebolla ni ajo y con patata y zanahoria. Si es tu primera vez, empieza por media ración. Receta completa en el blog.',
    kicker='Pregunta frecuente', title='¿Puedo comer lentejas con SIBO?', answer=['Sí, mejor de bote y enjuagadas', 'Unos 75 g por ración', 'Primera vez: media ración'], source=M)

LG = 'legumbres-y-sibo-raciones'
pin(LG, 'versus', 24, D, 'Garbanzos de bote o cocidos en casa: la diferencia en FODMAP',
    'Según los umbrales de Monash, los garbanzos de bote enjuagados son bajos en FODMAP hasta unos 95 g por comida, y cocidos a partir de secos solo hasta 33 g. La tabla completa de legumbres para SIBO en el blog.',
    kicker='El dato clave', title='Garbanzos: de bote mucho mejor', a=['De bote, enjuagados', 'escurridos', 'hasta 95 g', 'por comida'], b=['Secos, cocidos en casa', 'escurridos', 'hasta 33 g', 'por comida'], note='Los GOS pasan al líquido de la conserva.', source=M)
pin(LG, 'lista', 25, D, 'Legumbres y FODMAP: tabla de raciones para SIBO',
    'Tofu firme hasta 175 g, alubias rojas de bote 102 g, garbanzos de bote 95 g, alubias blancas 89 g y lentejas de bote 76 g por comida. Tabla de legumbres bajas en FODMAP según los umbrales de Monash.',
    kicker='Tabla para guardar', title='Legumbres: cuánto puedes comer', unit='De bote, escurridas, por comida',
    rows=[['Tofu firme', '175 g'], ['Alubias rojas de bote', '102 g'], ['Garbanzos de bote', '95 g'], ['Alubias blancas (cannellini)', '89 g'], ['Lentejas de bote', '76 g']], source=M)
pin(LG, 'curiosidad', 69, D, '7 reglas para comer legumbres con SIBO sin hinchazón',
    'Legumbres de bote, siempre enjuagadas, la ración pesada, el plato completado con patata o arroz, sin mezclar legumbres y empezando por media ración. Las reglas para comer legumbres con SIBO.',
    kicker='Reglas básicas', title='Cómo comer legumbres con SIBO', list=['Elige legumbres de bote', 'Tira el líquido y enjuágalas', 'Completa con patata o arroz', 'Empieza con media ración'])
pin(LG, 'versus', 25, D, 'Alubias rojas: 102 g de bote frente a 17 g cocidas en casa',
    'La diferencia más grande entre legumbres de bote y caseras: las alubias rojas de bote son bajas en FODMAP hasta 102 g y cocidas en casa solo hasta 17 g, según Monash. Más datos en la guía de legumbres y SIBO.',
    kicker='¿Sabías que…?', title='Alubias rojas: el bote gana', a=['De bote, enjuagadas', 'escurridas', '102 g', 'por comida'], b=['Cocidas en casa', 'escurridas', '17 g', 'por comida'], note='Con SIBO, mejor legumbres de bote.', source=M)
pin(LG, 'pregunta', 26, D, '¿Puedo comer garbanzos con SIBO? Sí, de bote',
    'Los garbanzos de bote bien enjuagados son bajos en FODMAP hasta unos 95 g por comida según Monash. Ideales para un potaje adaptado con patata, espinacas y huevo duro. Guía completa de legumbres.',
    kicker='Pregunta frecuente', title='¿Puedo comer garbanzos con SIBO?', answer=['Sí, de bote y enjuagados', 'Hasta unos 95 g por comida', 'Añádelos al final del guiso'], source=M)
pin(LG, 'curiosidad', 46, D, 'Cocido y potaje aptos para SIBO: cómo adaptarlos',
    'Para un potaje bajo en FODMAP: garbanzos de bote (unos 80 g por ración), verde de puerro, pimentón, espinacas, patata y huevo duro. En el cocido, añade los garbanzos de bote al final. Adaptaciones en la guía.',
    kicker='Cocina española', title='Potaje de garbanzos apto para SIBO', body='Cómo adaptarlo:', list=['Garbanzos de bote, unos 80 g', 'Verde de puerro y pimentón', 'Espinacas, patata y huevo duro'])
pin(LG, 'foto', 24, D, 'Legumbres con SIBO: no hace falta dejarlas',
    'Con SIBO o colon irritable no hace falta dejar las legumbres: hace falta elegir bien el formato y la cantidad. De bote y enjuagadas tienen muchos menos FODMAP. Tabla completa con raciones en el blog.',
    kicker='Guía de legumbres', title='No hace falta dejar las legumbres', sub='La clave: de bote, enjuagadas y en su ración')
pin(LG, 'pregunta', 25, D, '¿Puedo comer tofu o edamame con SIBO?',
    'Sí: el tofu firme es bajo en FODMAP hasta 175 g y el edamame hasta 195 g por comida, según los umbrales de Monash. Dos proteínas vegetales cómodas para la dieta baja en FODMAP.',
    kicker='Pregunta frecuente', title='¿Puedo comer tofu con SIBO?', answer=['Sí, el tofu firme', 'Hasta 175 g por comida', 'Edamame: hasta 195 g'], source=M)

H = 'helado-vainilla-sin-lactosa-fodmap'
pin(H, 'foto', 21, P, 'Helado de vainilla sin lactosa y bajo en FODMAP, sin heladera',
    'Cinco ingredientes: leche y nata sin lactosa, yemas, azúcar y vainilla. Un helado cremoso casero sin heladera, apto para la dieta baja en FODMAP, SIBO y colon irritable. Receta con trucos contra los cristales.',
    kicker='Sin heladera', title='Helado de vainilla sin lactosa', sub='5 ingredientes, cremoso y bajo en FODMAP')
pin(H, 'curiosidad', 21, P, 'Por qué el helado normal puede sentar mal con SIBO',
    'Una bola pequeña de helado de vainilla normal ya tiene lactosa moderada según Monash, y los helados «sin azúcar» suelen llevar polioles. La alternativa casera, en el blog.',
    kicker='Antes de comprar helado', title='Lo que esconde un helado normal', list=['Lactosa: 1 bola ya es moderada', 'Polioles en los «sin azúcar»', 'Inulina en los «altos en fibra»'], source=M)
pin(H, 'receta', 20, P, 'Helado casero sin lactosa: ingredientes y truco sin cristales',
    'Remueve la mezcla cada 30 a 45 minutos mientras se congela y tendrás un helado cremoso sin cristales de hielo, sin heladera. Receta baja en FODMAP con leche y nata sin lactosa.',
    kicker='Receta casera', title='Helado de vainilla casero', chips=['Sin heladera', 'Sin lactosa'], ing=['Nata sin lactosa', 'Leche sin lactosa', '4 yemas', 'Azúcar y vainilla'], tip='Remueve cada 30-45 min para que no haga cristales.')
pin(H, 'pregunta', 21, P, '¿Qué helado puedo tomar con SIBO?',
    'En una heladería, la opción más segura suele ser el sorbete de limón o frambuesa sin base láctea ni edulcorantes. En casa, nuestro helado de vainilla sin lactosa y bajo en FODMAP.',
    kicker='Pregunta frecuente', title='¿Qué helado puedo tomar con SIBO?', answer=['Casero sin lactosa', 'En heladería: sorbete de limón', 'Evita los «sin azúcar»'])

B = 'bizcocho-bajo-en-fodmap-sin-lactosa'
pin(B, 'foto', 3, P, 'Bizcocho bajo en FODMAP esponjoso, sin lactosa y sin gluten',
    'El bizcocho de yogur de toda la vida con yogur sin lactosa, harina de arroz y maicena. Alto, esponjoso y con aroma a limón, apto para SIBO y colon irritable. Receta en gramos y en vasitos de yogur.',
    kicker='Para merendar', title='Bizcocho de yogur bajo en FODMAP', sub='Esponjoso, sin lactosa y sin gluten')
pin(B, 'receta', 2, P, 'Bizcocho de yogur sin lactosa: ingredientes en vasitos',
    'Tres huevos, yogur sin lactosa, azúcar, aceite, harina de arroz y maicena. La receta del bizcocho de yogur adaptado a la dieta baja en FODMAP, medida con el vasito como siempre.',
    kicker='Receta de la abuela', title='Bizcocho de yogur adaptado', chips=['10 porciones', 'Sin gluten'], ing=['3 huevos', 'Yogur sin lactosa', '200 g harina de arroz', '100 g maicena'], tip='Bate huevos y azúcar 5-6 minutos: es lo que lo hace subir.')
pin(B, 'curiosidad', 3, P, 'Por qué el bizcocho normal puede dar hinchazón',
    'Harina de trigo (fructanos), yogur y leche (lactosa), miel o agave (fructosa) y polioles en los industriales «sin azúcar». Así es un bizcocho tradicional visto desde la dieta FODMAP.',
    kicker='Lo que no se ve', title='Lo que hincha de un bizcocho normal', list=['Harina de trigo: fructanos', 'Yogur y leche: lactosa', 'Miel o agave: fructosa', 'Industriales «sin azúcar»: polioles'])
pin(B, 'curiosidad', 2, P, 'El truco para que un bizcocho sin gluten suba',
    'Sin gluten, el aire que metes al batir es lo que hace subir el bizcocho. Huevos a temperatura ambiente, batir 5-6 minutos y dejar reposar la masa 10 minutos. Trucos en la receta.',
    kicker='Truco de repostería', title='Cómo hacer que suba sin gluten', list=['Huevos a temperatura ambiente', 'Batir 5-6 minutos hasta blanquear', 'Reposar la masa 10 minutos'])
pin(B, 'foto', 2, DE, 'Bizcocho con café: desayuno bajo en FODMAP para el fin de semana',
    'Una porción de bizcocho de yogur sin lactosa con un café o una infusión. Ninguno de sus ingredientes tiene ración límite en estas cantidades. Receta baja en FODMAP para SIBO.',
    kicker='Desayuno de domingo', title='Bizcocho de limón sin lactosa', sub='Una porción, sin preocuparte por los FODMAP')

PO = 'postres-bajos-en-fodmap-dulces-sin-hinchazon'
pin(PO, 'foto', 41, P, 'Postres bajos en FODMAP: dulces sin hinchazón',
    'Bizcochos, crumbles, crepes y cremas adaptados a la dieta baja en FODMAP con harinas digestivas y endulzantes equilibrados. Guía de postres con recetas paso a paso para SIBO y colon irritable.',
    kicker='Guía de postres', title='Postres que no te hinchan', sub='Recetas dulces bajas en FODMAP')
pin(PO, 'lista', 42, P, 'Lo que hace que un postre te hinche: los 4 detonantes',
    'Harina de trigo (fructanos), leche y nata (lactosa), manzana, pera, miel o dátiles (fructosa y sorbitol) y edulcorantes tipo poliol. Los detonantes de la repostería tradicional y cómo sustituirlos.',
    kicker='Repostería', title='Los 4 detonantes de los postres', unit='Qué FODMAP aportan',
    rows=[['Harina de trigo', 'fructanos'], ['Leche, nata, queso fresco', 'lactosa'], ['Manzana, pera, miel, dátiles', 'fructosa y sorbitol'], ['Edulcorantes «sin azúcar»', 'polioles']], source='')
pin(PO, 'curiosidad', 43, P, '5 errores al hornear postres para SIBO',
    'Endulzar con dátiles, usar harinas sin gluten con garbanzo o inulina, abusar de la harina de almendra o juntar mucha fruta en una porción. Los errores más comunes en los postres bajos en FODMAP.',
    kicker='Errores comunes', title='Errores al hacer postres FODMAP', list=['Endulzar con dátiles', 'Harinas sin gluten con inulina', 'Mucha harina de almendra', 'Demasiada fruta junta'])
pin(PO, 'pregunta', 42, P, '¿Puedo tomar chocolate con SIBO?',
    'Sí, en porciones moderadas: el chocolate negro de 70-85 % tiene poco azúcar y prácticamente nada de lactosa. Una onza diaria, unos 15-20 g, se suele tolerar bien. Más en la guía de postres.',
    kicker='Pregunta frecuente', title='¿Puedo tomar chocolate con SIBO?', answer=['Sí, chocolate negro 70-85 %', 'Una onza al día: 15-20 g', 'Evita el chocolate con leche'])
pin(PO, 'curiosidad', 41, P, 'Azúcar o edulcorante: qué sienta mejor a la barriga',
    'Desde el punto de vista de los gases, el azúcar común se absorbe casi entero en el intestino delgado. Para un postre puntual sienta mejor que los polioles o la pasta de dátiles. Lo explicamos en la guía.',
    kicker='¿Sabías que…?', title='Azúcar común frente a edulcorantes', list=['El azúcar se absorbe casi entero', 'Los polioles fermentan con facilidad', 'Los dátiles son altos en fructanos'])
pin(PO, 'foto', 43, P, 'Crumble de frutos rojos bajo en FODMAP',
    'Arándanos y fresas con una cubierta crujiente de harina de avena sin gluten, almendra y mantequilla. Un postre tibio bajo en FODMAP para tres raciones. Receta paso a paso en la guía de postres.',
    kicker='Receta en la guía', title='Crumble de frutos rojos', sub='Con avena sin gluten y fruta medida')

MO = 'mousse-chocolate-baja-fodmap-sibo'
pin(MO, 'foto', 30, P, 'Mousse de chocolate y plátano sin nata ni lactosa',
    'Plátano firme, cacao puro y un toque de crema de cacahuete: una mousse cremosa baja en FODMAP en 10 minutos más nevera. Postre apto para SIBO y colon irritable.',
    kicker='Postre en 10 minutos', title='Mousse de chocolate sin lactosa', sub='Con plátano firme y cacao puro')
pin(MO, 'pregunta', 43, P, '¿Postre de chocolate con SIBO? Esta mousse es baja en FODMAP',
    'Usa plátano firme, sin motas: según Monash es bajo en FODMAP hasta 100 g, mientras que el maduro solo hasta unos 35 g. Así funciona nuestra mousse de chocolate sin nata.',
    kicker='Truco de la receta', title='El secreto de esta mousse', answer=['Plátano firme, sin motas', 'Bajo en FODMAP hasta 100 g', 'Cacao puro sin azúcar'], source=M)
pin(MO, 'receta', 30, P, 'Mousse de chocolate baja en FODMAP: 4 ingredientes',
    'Plátano firme, cacao puro, crema de cacahuete natural y bebida vegetal. Tritura, enfría 30 minutos y listo. Receta de postre bajo en FODMAP para SIBO.',
    kicker='Receta rápida', title='Mousse de cacao y plátano', chips=['10 min', 'Sin lactosa'], ing=['Plátano firme', 'Cacao puro', 'Crema de cacahuete', 'Bebida vegetal'], tip='Enfría al menos 30 minutos en la nevera.')

NA = 'natillas-huevo-sin-lactosa-sibo'
pin(NA, 'foto', 32, P, 'Natillas de huevo sin lactosa: el postre de la abuela apto para SIBO',
    'Yemas, agua infusionada con canela y limón, y cocción al baño María: natillas cremosas sin leche, aptas para la dieta baja en FODMAP y SIBO.',
    kicker='Postre de siempre', title='Natillas sin lactosa', sub='Con canela y limón, como las de la abuela')
pin(NA, 'receta', 32, P, 'Natillas sin leche: receta baja en FODMAP',
    'Cuatro yemas, dos claras, agua con canela y ralladura de limón. Se cuecen al baño María y se enfrían 2 horas. Natillas sin lactosa aptas para SIBO.',
    kicker='Receta casera', title='Natillas de huevo sin leche', chips=['4 raciones', 'Sin lactosa'], ing=['4 yemas y 2 claras', '400 ml de agua', 'Rama de canela', 'Piel de limón'], tip='Al baño María: cremosas, no como un flan.')
pin(NA, 'curiosidad', 32, P, 'Postres sin lactosa que no necesitan bebida vegetal',
    'Estas natillas sustituyen la leche por agua infusionada con canela y limón: la yema da la cremosidad. Un postre tradicional sin lactosa ni FODMAP añadidos.',
    kicker='¿Sabías que…?', title='Natillas cremosas sin leche ni bebida vegetal', list=['La yema aporta la cremosidad', 'El agua con canela da el sabor', 'Cero lactosa'])

BO = 'bocados-platano-chocolate-85-fodmap-sibo'
pin(BO, 'foto', 4, P, 'Bocados de plátano y chocolate 85 %: snack bajo en FODMAP',
    'Plátano firme, chocolate negro 85 % y un toque de crema de almendra o cacahuete. Ocho bocados en 15 minutos para merendar con SIBO sin pasarte.',
    kicker='Snack dulce', title='Bocados de plátano y chocolate', sub='8 bocados en 15 minutos')
pin(BO, 'receta', 4, P, 'Bocados de plátano con chocolate negro: receta fácil',
    'Machaca un plátano firme, forma bolitas, báñalas en chocolate 85 % y enfría 15 minutos. Un dulce bajo en FODMAP que se conserva 3 días en la nevera.',
    kicker='Receta en 15 min', title='Bocados de chocolate y plátano', chips=['8 bocados', '15 min'], ing=['1 plátano firme pequeño', '50 g chocolate 85 %', 'Crema de almendra', 'Canela'], tip='Plátano amarillo sin motas marrones.')
pin(BO, 'pregunta', 4, P, '¿Qué chocolate puedo comer con SIBO?',
    'Chocolate negro 85 % sin azúcar ni leche: tiene muy poco azúcar y aporta polifenoles. Lo usamos en estos bocados de plátano bajos en FODMAP.',
    kicker='Pregunta frecuente', title='¿Qué chocolate elegir con SIBO?', answer=['Negro, 70-85 % de cacao', 'Sin leche añadida', 'En porciones pequeñas'])

DO = 'donuts-mandarina-coco-low-fodmap'
pin(DO, 'curiosidad', 17, P, 'Donuts helados de mandarina y coco, sin horno',
    'Mitades de mandarina con glaseado cítrico y crema de coco montada, congeladas 2-3 horas. Un snack refrescante, vegano y bajo en FODMAP.',
    kicker='Receta original', title='Donuts de mandarina y coco', list=['Mandarinas cortadas por la mitad', 'Crema de coco montada', 'Congelar 2-3 horas'])
pin(DO, 'receta', 17, P, 'Donuts de mandarina: ingredientes y paso a paso',
    'Mandarinas, leche de coco entera, sirope de arce, vainilla y azúcar glas. Un postre sin horno, sin gluten y bajo en FODMAP para SIBO.',
    kicker='Sin horno', title='Donuts helados de mandarina', chips=['Vegano', 'Sin gluten'], ing=['4 mandarinas', 'Leche de coco entera', 'Sirope de arce', 'Vainilla'], tip='Saca la lata de coco de la nevera sin agitarla.')

DS = 'desayunos-bajos-en-fodmap'
pin(DS, 'foto', 12, DE, '5 desayunos bajos en FODMAP para no hincharte',
    'Gachas de avena con arándanos, tostada de masa madre con huevo, pudding de chía, yogur de coco con nueces y tortilla de calabacín. Cinco desayunos para SIBO con raciones de Monash.',
    kicker='Ideas de desayuno', title='5 desayunos que no te hinchan', sub='Con raciones de la Universidad de Monash')
pin(DS, 'lista', 14, DE, 'Desayunos bajos en FODMAP: 5 ideas para la semana',
    'Una idea de desayuno para cada día laborable: gachas de avena, tostada de masa madre, pudding de chía, yogur de coco y tortilla de calabacín. Recetas para SIBO y colon irritable.',
    kicker='Plan de la semana', title='Un desayuno para cada día', unit='Desayunos bajos en FODMAP',
    rows=[['Lunes', 'gachas de avena'], ['Martes', 'tostada con huevo'], ['Miércoles', 'pudding de chía'], ['Jueves', 'yogur de coco'], ['Viernes', 'tortilla de calabacín']], source='')
pin(DS, 'pregunta', 13, DE, '¿Se puede tomar café con SIBO?',
    'El café solo es apto desde el punto de vista FODMAP, pero la cafeína estimula el intestino y puede dar acidez. Si te sienta bien, tómalo solo o con bebida de almendra o arroz.',
    kicker='Pregunta frecuente', title='¿Puedo tomar café con SIBO?', answer=['Solo o filtrado: apto', 'Con bebida de almendra o arroz', 'Ojo si te da acidez'])
pin(DS, 'curiosidad', 11, DE, 'El efecto acumulación en el desayuno: cuidado al mezclar',
    'Avena, almendras y medio plátano son aptos por separado, pero juntos pueden superar tu umbral. Mantén los desayunos simples y con pocos ingredientes. Más en la guía de desayunos.',
    kicker='Error común', title='Desayunos simples, menos síntomas', body='Aptos por separado, no siempre juntos:', list=['Avena', 'Almendras', 'Medio plátano firme'])
pin(DS, 'foto', 14, DE, 'Tostada de masa madre con huevo revuelto: desayuno para SIBO',
    'Una o dos rebanadas de masa madre auténtica de fermentación lenta, huevos revueltos con aceite de oliva y escamas de sal. Un desayuno salado bajo en FODMAP.',
    kicker='Desayuno salado', title='Tostada con huevo revuelto', sub='Pan de masa madre de fermentación lenta')
pin(DS, 'curiosidad', 12, DE, 'Infusiones con SIBO: cuáles evitar por la mañana',
    'El té negro suave y el té verde son seguros, pero la manzanilla, el hinojo y el té chai con mezclas desconocidas pueden concentrar fructanos. Bebidas matutinas explicadas en la guía.',
    kicker='Bebidas', title='Té e infusiones con SIBO', body='Lo que dice la guía:', list=['Té negro suave y té verde: aptos', 'Manzanilla e hinojo: mejor evitar', 'Ojo con el chai y las mezclas'])

PR = 'porridge-avena-bajo-fodmap-sibo'
pin(PR, 'foto', 39, DE, 'Porridge de avena bajo en FODMAP con plátano',
    'Avena sin gluten, bebida vegetal, medio plátano firme y semillas de chía. Un desayuno caliente en 10 minutos, bajo en FODMAP, para empezar el día con SIBO.',
    kicker='Desayuno en 10 min', title='Porridge de avena para SIBO', sub='Con plátano firme y semillas')
pin(PR, 'receta', 39, DE, 'Porridge de avena sin gluten: receta baja en FODMAP',
    'Según Monash, los copos de avena son bajos en FODMAP hasta 52 g. Esta receta usa 40 g con bebida vegetal, medio plátano firme y chía. Paso a paso en el blog.',
    kicker='Receta de desayuno', title='Gachas de avena con plátano', chips=['1 ración', '10 min'], ing=['40 g copos de avena', '200 ml bebida vegetal', '½ plátano firme', 'Chía o lino'], tip='Evita la miel y la fruta seca: son altas en FODMAP.')
pin(PR, 'pregunta', 11, DE, '¿Puedo comer avena con SIBO?',
    'Sí: según Monash, los copos de avena son bajos en FODMAP hasta 52 g por comida. Mejor certificada sin gluten si también lo necesitas. Receta de porridge apto para SIBO.',
    kicker='Pregunta frecuente', title='¿Puedo comer avena con SIBO?', answer=['Sí, en ración medida', 'Copos de avena: hasta 52 g', 'Sin miel ni fruta seca'], source=M)

BA = 'batido-verde-digestivo-bajo-fodmap-sibo'
pin(BA, 'foto', 0, DE, 'Batido verde bajo en FODMAP en 5 minutos',
    'Medio plátano con pintas verdes, espinacas baby, crema de cacahuete y bebida de almendras. Un desayuno rápido y suave, bajo en FODMAP, para mañanas con prisa.',
    kicker='Desayuno en 5 min', title='Batido verde digestivo', sub='Con plátano firme y espinacas baby')
pin(BA, 'receta', 0, DE, 'Batido verde para SIBO: ingredientes y raciones',
    'Medio plátano firme, 30 g de espinacas baby, una cucharadita de crema de cacahuete y 200 ml de bebida de almendras. Todo dentro de las raciones bajas en FODMAP.',
    kicker='Receta rápida', title='Batido verde bajo en FODMAP', chips=['5 min', '1 ración'], ing=['½ plátano firme', '30 g espinacas baby', 'Crema de cacahuete', 'Bebida de almendras'], tip='Plátano con pintas verdes: es el truco de la tolerancia.')
pin(BA, 'curiosidad', 1, DE, 'Batidos para SIBO: el error de mezclar demasiadas frutas',
    'Un batido con plátano maduro, medio mango y dátiles es una bomba de FODMAP aunque se venda como «detox». La clave: una fruta en su ración y verduras de hoja. Receta de batido verde apto.',
    kicker='Error común', title='Batidos «detox» que hinchan', list=['Plátano maduro', 'Mango', 'Dátiles'], body='Combinación muy alta en FODMAP:')

SO = 'sopa-calabaza-zanahoria-baja-fodmap-sibo'
pin(SO, 'foto', 61, R, 'Sopa de calabaza y zanahoria baja en FODMAP',
    'Una crema templada con calabaza en ración moderada, zanahoria y patata para dar volumen. Cena suave y baja en FODMAP para SIBO y colon irritable.',
    kicker='Cena reconfortante', title='Sopa de calabaza y zanahoria', sub='Con la ración de calabaza bien medida')
pin(SO, 'receta', 9, R, 'Crema de calabaza para SIBO: ingredientes y truco',
    'Calabaza en ración moderada, dos zanahorias, una patata y caldo bajo en FODMAP. Si quieres más cantidad, usa calabaza japonesa o completa con zanahoria y patata.',
    kicker='Receta de cena', title='Crema de calabaza apta para SIBO', chips=['2 raciones', 'Sin lácteos'], ing=['120 g calabaza', '2 zanahorias', '1 patata', 'Caldo sin cebolla'], tip='La calabaza japonesa admite más cantidad.')
pin(SO, 'versus', 60, D, 'Calabaza cacahuete o japonesa: cuál admite más ración',
    'Según Monash, la calabaza cacahuete (butternut) es baja en FODMAP hasta 63 g y la japonesa o kabocha hasta 75 g. Para hacer cremas con SIBO, la japonesa da más margen.',
    kicker='¿Sabías que…?', title='Dos calabazas, dos raciones', a=['Cacahuete', 'butternut', 'hasta 63 g', 'por ración'], b=['Japonesa', 'kabocha', 'hasta 75 g', 'por ración'], note='Completa con zanahoria y patata.', source=M)

SA = 'salmon-horno-pure-patata-calabacin-fodmap-sibo'
pin(SA, 'foto', 51, R, 'Salmón al horno con puré de patata y calabacín',
    'Salmón jugoso al horno con un puré cremoso sin lácteos: patata y 65 g de calabacín por ración. Una cena baja en FODMAP, sin ajo ni cebolla, en 30 minutos.',
    kicker='Cena en 30 min', title='Salmón al horno con puré', sub='Sin lácteos, sin ajo y sin cebolla')
pin(SA, 'receta', 52, R, 'Salmón con puré para SIBO: ingredientes',
    'Dos filetes de salmón, patatas, un calabacín pequeño, aceite de oliva, limón y eneldo. Una cena baja en FODMAP con proteína fácil de digerir y omega-3.',
    kicker='Receta de cena', title='Salmón con puré de calabacín', chips=['2 raciones', '30 min'], ing=['2 filetes de salmón', '300 g de patata', '130 g de calabacín', 'Limón y eneldo'], tip='65 g de calabacín por ración: la cantidad baja de Monash.')
pin(SA, 'curiosidad', 44, R, 'Cenas sin ajo ni cebolla: cómo dar sabor',
    'Limón, eneldo, perejil, romero, tomillo y un buen aceite de oliva: así damos sabor a nuestras cenas bajas en FODMAP, como el salmón al horno con puré.',
    kicker='Truco de cocina', title='Sabor sin ajo ni cebolla', list=['Limón y su ralladura', 'Eneldo, perejil o romero', 'Aceite de oliva virgen extra'])

PL = 'pollo-pure-zanahoria-calabacin-fodmap-sibo'
pin(PL, 'foto', 37, R, 'Pollo con puré de zanahoria y calabacín: cena ligera para SIBO',
    'Pechuga a la plancha sobre un puré suave de zanahoria y calabacín. Una cena baja en FODMAP, ligera y lista en 25 minutos.',
    kicker='Cena ligera', title='Pollo con puré de zanahoria', sub='Lista en 25 minutos')
pin(PL, 'receta', 38, R, 'Pollo con puré de verduras bajo en FODMAP',
    '120 g de pechuga, una zanahoria, medio calabacín pequeño y aceite de oliva. Puré suave y pollo jugoso para una cena que no pesa. Receta para SIBO.',
    kicker='Receta en 25 min', title='Pollo con puré suave', chips=['1 ración', '25 min'], ing=['120 g de pechuga', '1 zanahoria', '½ calabacín (65 g)', 'Tomillo o romero'], tip='Evita el ajo o la cebolla en polvo.')
pin(PL, 'curiosidad', 46, D, 'Ajo y cebolla en polvo: también tienen FODMAP',
    'El ajo y la cebolla en polvo, incluso los «sin olor», siguen conteniendo FODMAP altos. Revisa también los caldos y especias preparadas. Un consejo de nuestras recetas bajas en FODMAP.',
    kicker='Ojo con las especias', title='El ajo en polvo también cuenta', list=['Ajo y cebolla en polvo: altos', 'Caldos de pastilla: revisa', 'Mezclas de especias: revisa'])

TC = 'tortilla-claras-espinacas-calabacin-fodmap-sibo'
pin(TC, 'foto', 62, R, 'Tortilla de claras con espinacas y calabacín',
    'Cuatro claras, espinacas y 65 g de calabacín: una cena rica en proteína, baja en grasa y baja en FODMAP, lista en menos de 15 minutos.',
    kicker='Cena en 15 min', title='Tortilla de claras y espinacas', sub='Ligera, con proteína y baja en FODMAP')
pin(TC, 'receta', 63, R, 'Tortilla de claras baja en FODMAP: ingredientes',
    '4 claras, medio calabacín pequeño, una taza de espinacas, aceite de oliva y pimienta. Cena ligera para SIBO, ideal 2-3 horas antes de dormir.',
    kicker='Receta rápida', title='Tortilla de claras ligera', chips=['1 ración', '15 min'], ing=['4 claras de huevo', '½ calabacín (65 g)', '1 taza de espinacas', 'Aceite de oliva'], tip='Fuego medio-bajo para que quede tierna.')
pin(TC, 'pregunta', 62, D, '¿Puedo comer huevo con SIBO?',
    'Sí: el huevo es proteína pura, sin hidratos de carbono fermentables. Es una base perfecta para cenas y desayunos bajos en FODMAP, como esta tortilla de claras.',
    kicker='Pregunta frecuente', title='¿Puedo comer huevo con SIBO?', answer=['Sí, sin límite FODMAP', 'Es proteína, sin hidratos fermentables', 'Ideal para cenas ligeras'])

CR = 'croquetas-pollo-calabacin-sibo-fodmap'
pin(CR, 'foto', 10, R, 'Croquetas de pollo y calabacín al horno, sin gluten ni lactosa',
    'Bechamel con harina de arroz y bebida vegetal, pollo y calabacín, y al horno en lugar de fritas. Unas 12 croquetas bajas en FODMAP para SIBO.',
    kicker='Al horno', title='Croquetas de pollo sin gluten', sub='Sin leche, sin trigo y sin freír')
pin(CR, 'receta', 10, R, 'Croquetas para SIBO: la bechamel sin gluten ni lácteos',
    'Harina de arroz integral, maicena y bebida vegetal hacen una bechamel apta. Pollo cocido, calabacín escurrido y horno 20-25 minutos. Se pueden congelar.',
    kicker='Receta casera', title='Croquetas de pollo y calabacín', chips=['12 croquetas', 'Se congelan'], ing=['250 g de pollo cocido', '120 g de calabacín', 'Harina de arroz', 'Bebida vegetal'], tip='Escurre bien el calabacín para que no queden blandas.')
pin(CR, 'curiosidad', 10, R, 'Truco para croquetas sin gluten que no se rompan',
    'Escurre muy bien el calabacín rallado con un paño, deja templar la masa 10-15 minutos y hornéalas a 200 °C dándoles la vuelta a mitad. Así quedan crujientes por fuera y jugosas por dentro.',
    kicker='Trucos', title='Croquetas crujientes al horno', list=['Escurre el calabacín con un paño', 'Deja templar la masa', '200 °C, vuelta a mitad'])

SL = 'solomillo-romero-boniato-fodmap-sibo'
pin(SL, 'foto', 58, N, 'Solomillo al romero con puré de boniato para Navidad',
    'Un plato festivo bajo en FODMAP: solomillo de ternera marinado con limón y romero sobre un puré de boniato en ración moderada. Sin ajo, sin cebolla y sin lácteos.',
    kicker='Plato de fiesta', title='Solomillo al romero con boniato', sub='Para una Navidad baja en FODMAP')
pin(SL, 'receta', 59, N, 'Solomillo con boniato apto para SIBO: ingredientes',
    'Medallones de solomillo, aceite de oliva, limón, romero y 150 g de boniato para dos. Marcado en sartén y terminado al horno. Receta navideña baja en FODMAP.',
    kicker='Receta de fiesta', title='Solomillo con puré de boniato', chips=['2 raciones', '45 min'], ing=['2 medallones de solomillo', '150 g de boniato', 'Romero y limón', 'Aceite de oliva'], tip='Boniato: hasta 75 g por persona.')
pin(SL, 'pregunta', 58, D, '¿Puedo comer boniato con SIBO?',
    'Sí, en ración moderada: según Monash, el boniato es bajo en FODMAP hasta 75 g por ración. Si quieres más cantidad, combínalo con patata o zanahoria.',
    kicker='Pregunta frecuente', title='¿Puedo comer boniato con SIBO?', answer=['Sí, en ración moderada', 'Hasta 75 g por ración', 'Completa con patata o zanahoria'], source=M)

NV = 'menu-navidad-bajo-en-fodmap-sibo'
pin(NV, 'foto', 29, N, 'Menú de Navidad bajo en FODMAP: 6 recetas sin ajo ni cebolla',
    'Langostinos con mayonesa de limón, consomé sin cebolla, cordero asado, dorada con refrito de pimentón, turrón de chocolate y mantecados sin gluten. Un menú navideño apto para SIBO.',
    kicker='Menú completo', title='Navidad sin ajo ni cebolla', sub='6 recetas bajas en FODMAP')
pin(NV, 'curiosidad', 29, N, 'Las uvas de Nochevieja con SIBO: alternativas',
    'Las uvas son altas en fructosa a partir de solo 3 unidades. Alternativas para las campanadas: 12 gajos de mandarina, 12 arándanos o 6 fresas partidas. Más trucos en el menú de Navidad.',
    kicker='Nochevieja', title='12 uvas con SIBO: qué tomar', body='Las uvas son altas desde 3 unidades. Prueba:', list=['12 gajos de mandarina', '12 arándanos', '6 fresas partidas por la mitad'])
pin(NV, 'lista', 29, N, 'Vino, cava y cerveza en la dieta FODMAP: cuánto en Navidad',
    'Según Monash: vino tinto o blanco seco, una copa de 150 ml; cava, 150 ml; cerveza, unos 375 ml; ginebra, vodka o whisky, 30 ml. Evita vinos dulces y sidra. Guía de Navidad baja en FODMAP.',
    kicker='Bebidas de Navidad', title='Cuánto beber sin pasarte de FODMAP', unit='Ración baja según Monash',
    rows=[['Vino seco', '1 copa (150 ml)'], ['Cava', '1 copa (150 ml)'], ['Cerveza', 'unos 375 ml'], ['Ginebra, vodka, whisky', '30 ml'], ['Vinos dulces, sidra', 'evitar']], source=M)
pin(NV, 'receta', 42, N, 'Turrón casero de chocolate negro crujiente, bajo en FODMAP',
    'Chocolate negro 70-85 %, mantequilla o aceite de coco, arroz inflado sin azúcar y escamas de sal. Unas 16 porciones de turrón apto para una Navidad con SIBO.',
    kicker='Dulce de Navidad', title='Turrón de chocolate crujiente', chips=['16 porciones', 'Sin almendra'], ing=['300 g de chocolate negro', '30 g mantequilla', '60 g arroz inflado', 'Escamas de sal'], tip='Chocolate negro: bajo en FODMAP hasta unos 30 g.')
pin(NV, 'curiosidad', 29, N, 'Turrón, mazapán y castañas con SIBO: qué dice la dieta FODMAP',
    'El turrón de Jijona y Alicante lleva mucha almendra y miel; mazapán, una figurita pequeña como mucho. Las castañas son bajas en FODMAP incluso en raciones generosas. Guía de la Navidad baja en FODMAP.',
    kicker='Dulces navideños', title='Turrón, mazapán y castañas', list=['Turrón tradicional: ración muy pequeña', 'Mazapán: una figurita como mucho', 'Castañas: aptas'])
pin(NV, 'foto', 42, N, 'Mantecados de avena y canela sin gluten para Navidad',
    'Harina de avena sin gluten, mantequilla, azúcar glas, canela y limón. Unos 20 mantecados bajos en FODMAP; dos unidades son una ración. Receta en el menú de Navidad.',
    kicker='Dulce de Navidad', title='Mantecados de avena sin gluten', sub='2 mantecados son una ración')
pin(NV, 'receta', 29, N, 'Consomé navideño sin cebolla: receta baja en FODMAP',
    'Carcasa de pollo, hueso de jamón, zanahoria, chirivía y la parte verde del puerro. Se sirve con huevo duro, jamón y fideos de arroz. Entrante de Navidad apto para SIBO.',
    kicker='Entrante', title='Consomé de Navidad sin cebolla', chips=['Sin ajo', 'Sin cebolla'], ing=['Carcasa de pollo', 'Hueso de jamón', 'Zanahoria y chirivía', 'Verde de puerro'], tip='Sírvelo con huevo duro, jamón y fideos de arroz.')
pin(NV, 'pregunta', 29, N, '¿Puedo comer jamón con SIBO en Navidad?',
    'El jamón curado es carne sin hidratos de carbono, así que es apto en la dieta baja en FODMAP. Revisa la etiqueta por si lleva lactosa o dextrosa añadidas. Más en la guía de Navidad.',
    kicker='Pregunta frecuente', title='¿Puedo comer jamón con SIBO?', answer=['Sí, el jamón curado es apto', 'No tiene hidratos de carbono', 'Revisa si lleva lactosa añadida'])
pin(NV, 'curiosidad', 58, N, 'Cómo sobrevivir a las comidas de Navidad con SIBO',
    'Elige platos de carne o pescado al horno, verduras como judías verdes (hasta 75 g), una o dos copas como mucho y dulces caseros. El menú completo de Navidad bajo en FODMAP en el blog.',
    kicker='Plan de fiestas', title='Comidas de Navidad con SIBO', list=['Carne o pescado al horno', 'Judías verdes: hasta 75 g', 'Una o dos copas como mucho', 'Dulces caseros aptos'])
pin(NV, 'receta', 44, N, 'Dorada a la espalda con refrito de pimentón, sin ajo',
    'Dorada al horno 10-12 minutos con un refrito de aceite, pimentón de la Vera y vinagre. Con judías verdes, hasta 75 g por persona. Alternativa de pescado para Navidad.',
    kicker='Pescado de fiesta', title='Dorada con refrito de pimentón', chips=['Sin ajo', '12 min de horno'], ing=['3 doradas grandes', 'Aceite de oliva', 'Pimentón de la Vera', 'Vinagre y perejil'], tip='Acompaña con judías verdes, hasta 75 g.')
pin(NV, 'foto', 29, N, 'Navidad con SIBO: un menú para disfrutar sin hincharte',
    'Seis recetas pensadas para que la Navidad no sea sinónimo de hinchazón: sin ajo, sin cebolla y con raciones de Monash. Aperitivo, entrante, dos principales y dos postres.',
    kicker='Navidad', title='Una Navidad sin hinchazón', sub='Aperitivo, entrante, principal y postre')
pin(NV, 'lista', 42, N, 'Dulces de Navidad y FODMAP: cuáles puedes comer',
    'Chocolate negro hasta unos 30 g, dos mantecados caseros sin gluten, castañas en un cucurucho compartido y mazapán solo una figurita pequeña. Guía de Navidad baja en FODMAP.',
    kicker='Dulces de Navidad', title='Dulces navideños y su ración', unit='Según la guía del blog',
    rows=[['Chocolate negro 70-85 %', 'hasta 30 g'], ['Mantecados caseros', '2 unidades'], ['Castañas', 'cucurucho pequeño'], ['Mazapán', '1 figurita pequeña']], source=M)

MS = 'menu-fodmap-semanal-recetas-faciles'
pin(MS, 'foto', 27, D, 'Menú semanal de dieta baja en FODMAP: 7 días de recetas fáciles',
    'Desayunos, comidas, meriendas y cenas para una semana, con raciones medidas: salmón con puré, gachas de avena, pavo con arroz, bacalao con boniato y más. También si tienes SIBO.',
    kicker='Organiza tu semana', title='Menú FODMAP de 7 días', sub='Recetas fáciles, también si tienes SIBO')
pin(MS, 'lista', 26, D, 'Menú FODMAP: las comidas de lunes a viernes',
    'Salmón con puré de patata y judías verdes, pavo con arroz basmati, dorada al horno, hamburguesa de ternera y bacalao con boniato. Comidas de la semana bajas en FODMAP.',
    kicker='Comidas de la semana', title='Qué comer de lunes a viernes', unit='Menú FODMAP semanal',
    rows=[['Lunes', 'salmón con puré'], ['Martes', 'pavo con arroz'], ['Miércoles', 'dorada al horno'], ['Jueves', 'hamburguesa de ternera'], ['Viernes', 'bacalao con boniato']], source='')
pin(MS, 'curiosidad', 27, D, 'Lista de la compra para la dieta baja en FODMAP',
    'Huevos, pollo, pescado fresco, zanahorias, calabacines, arroz, quinoa, avena sin gluten y fresas o arándanos. Y fuera ajo, cebolla, manzanas, peras, champiñones y leche de vaca.',
    kicker='Lista de la compra', title='Qué comprar para la semana', list=['Huevos, pollo y pescado', 'Zanahoria, calabacín y patata', 'Arroz, quinoa y avena sin gluten', 'Fresas y arándanos'])
pin(MS, 'curiosidad', 28, D, 'Batch cooking FODMAP: cuánto dura cada cosa en la nevera',
    'Verduras cocidas y arroz: 3 o 4 días en la nevera. Pescado cocinado: 48 horas. Caldos y cremas: congélalos en tarros individuales. Consejos del menú semanal bajo en FODMAP.',
    kicker='Cocina para la semana', title='Cuánto dura cada cosa en la nevera', list=['Verduras cocidas y arroz: 3-4 días', 'Pescado cocinado: 48 horas', 'Caldos y cremas: congelados'])
pin(MS, 'lista', 13, D, 'Cenas fáciles para una semana baja en FODMAP',
    'Crema de calabacín con pollo, tortilla francesa con canónigos, tofu con fideos de arroz, sopa de fideos y brochetas de pollo con quinoa. Cenas del menú FODMAP semanal.',
    kicker='Cenas de la semana', title='Cenas fáciles bajas en FODMAP', unit='Menú FODMAP semanal',
    rows=[['Lunes', 'crema de calabacín y pollo'], ['Martes', 'tortilla con canónigos'], ['Miércoles', 'tofu con fideos de arroz'], ['Jueves', 'sopa de fideos de arroz'], ['Sábado', 'brochetas con quinoa']], source='')

CI = 'que-comer-con-colon-irritable'
pin(CI, 'foto', 46, C, 'Qué comer con colon irritable: guía práctica y menús de un día',
    'Comidas a horas regulares, platos sencillos y alimentos bajos en FODMAP. Menús de un día según tu síntoma principal: diarrea, estreñimiento o hinchazón. Basado en guías clínicas y Monash.',
    kicker='Guía práctica', title='Qué comer con colon irritable', sub='Menús según tu síntoma principal')
pin(CI, 'curiosidad', 44, C, 'Cómo montar un plato que siente bien con colon irritable',
    'La mitad del plato, verduras bien toleradas; un cuarto, proteína sencilla; un cuarto, arroz, patata o quinoa; y aceite de oliva. El plato base de nuestra guía de colon irritable.',
    kicker='El plato base', title='Así se monta un plato para el colon irritable', list=['½ plato: verduras toleradas', '¼: proteína sencilla', '¼: arroz, patata o quinoa', 'Aceite de oliva'])
pin(CI, 'lista', 45, C, 'Colon irritable: tipos según el síntoma principal',
    'SII con diarrea, con estreñimiento o mixto: no hay una sola dieta para el colon irritable y lo que conviene comer cambia según tu síntoma. Lo explicamos con menús de un día.',
    kicker='No hay una sola dieta', title='Los 3 tipos de colon irritable', unit='Síntoma que predomina',
    rows=[['SII-D', 'diarrea o urgencia'], ['SII-E', 'estreñimiento'], ['SII-M', 'alterna los dos']], source='')
pin(CI, 'curiosidad', 46, C, 'Señales para consultar al médico antes de cambiar tu dieta',
    'Sangre en las heces, pérdida de peso sin motivo, fiebre, anemia o síntomas que te despiertan por la noche no encajan con el colon irritable: consúltalo con tu médico antes de cambiar la dieta.',
    kicker='Importante', title='Cuándo consultar antes de cambiar la dieta', list=['Sangre en las heces', 'Pérdida de peso sin motivo', 'Fiebre o anemia', 'Síntomas que te despiertan'])
pin(CI, 'lista', 45, C, 'Frutas aptas con colon irritable y su ración',
    'Kiwi verde hasta 2 unidades, naranja o mandarina una pieza mediana, fresas 65 g y plátano firme 100 g, según Monash. La guía NICE aconseja no pasar de 3 raciones de fruta al día.',
    kicker='Colon irritable', title='Fruta con colon irritable', unit='Ración por comida',
    rows=[['Kiwi verde', '2 unidades'], ['Naranja o mandarina', '1 pieza mediana'], ['Fresas', '65 g'], ['Plátano firme', '100 g']], source=M)
pin(CI, 'curiosidad', 44, C, 'Pautas generales para el colon irritable antes de la dieta FODMAP',
    'Las guías clínicas empiezan por pautas sencillas: comer a horas regulares, beber suficiente, limitar café, alcohol y bebidas con gas, y no abusar del salvado de trigo. Si no basta, dieta baja en FODMAP.',
    kicker='Primer paso', title='Antes de la dieta FODMAP, esto', list=['Comer a horas regulares', 'Limitar café, alcohol y gas', 'No abusar del salvado de trigo'])
pin(CI, 'foto', 44, C, 'Cena para colon irritable: merluza con patata y judías verdes',
    'Pescado blanco al horno, patata y judías verdes (hasta 75 g): una cena sencilla y bien tolerada con colon irritable. Más ideas de menús en la guía práctica.',
    kicker='Idea de cena', title='Merluza con patata y judías', sub='Una cena sencilla para el colon irritable')
pin(CI, 'pregunta', 45, C, '¿Qué desayunar con colon irritable?',
    'Gachas de avena (hasta 52 g de copos) con kiwi, un café si te sienta bien y nada de zumos. Ideas de desayuno según tu tipo de colon irritable en la guía práctica.',
    kicker='Pregunta frecuente', title='¿Qué desayunar con colon irritable?', answer=['Gachas de avena con kiwi', 'Avena: hasta 52 g', 'Fruta entera, no zumo'], source=M)
pin(CI, 'curiosidad', 46, C, 'Colon irritable con diarrea: qué suele ir bien',
    'Hidratos sencillos y cocinados (arroz, patata, avena), proteínas magras a la plancha o al horno y verduras cocidas sin piel. Qué comer cuando predomina la diarrea, en la guía.',
    kicker='SII con diarrea', title='Qué suele ir bien con diarrea', list=['Arroz, patata o avena cocida', 'Pollo, pavo o pescado blanco', 'Verduras cocidas y sin piel'])

PI = 'dieta-baja-en-fodmap-que-es-fases'
pin(PI, 'foto', 27, D, 'Dieta baja en FODMAP: qué es y sus 3 fases',
    'Qué significa FODMAP, para quién está pensada la dieta, cuánto dura cada fase y qué alimentos tienen más y menos FODMAP. Guía con fuentes clínicas (BSG, AGA y Monash).',
    kicker='Guía completa', title='La dieta baja en FODMAP, explicada', sub='Qué es, sus 3 fases y para quién es')
pin(PI, 'lista', 69, D, 'Las 3 fases de la dieta baja en FODMAP y cuánto dura cada una',
    'Fase 1, eliminación: de 2 a 6 semanas. Fase 2, reintroducción: unas 6 a 8 semanas. Fase 3, personalización. No es una dieta para siempre. Guía con fuentes.',
    kicker='Paso a paso', title='Las 3 fases de la dieta FODMAP', unit='Duración aproximada',
    rows=[['1. Eliminación', '2 a 6 semanas'], ['2. Reintroducción', '6 a 8 semanas'], ['3. Personalización', 'a largo plazo']], source='Fuentes: Monash, BSG 2021, AGA 2022')
pin(PI, 'lista', 17, D, 'Qué significa FODMAP: los 5 grupos y dónde están',
    'Fructanos (trigo, ajo, cebolla), GOS (legumbres), lactosa (leche), exceso de fructosa (miel, mango) y polioles (melocotón, champiñones). Los grupos FODMAP explicados.',
    kicker='Para entenderlo', title='Los 5 grupos FODMAP', unit='Dónde están sobre todo',
    rows=[['Fructanos', 'trigo, ajo, cebolla'], ['GOS', 'legumbres'], ['Lactosa', 'leche, yogur'], ['Fructosa', 'miel, mango'], ['Polioles', 'melocotón, champiñón']], source='Según la Universidad de Monash')
pin(PI, 'curiosidad', 8, D, 'La dieta baja en FODMAP no es para siempre (ni para adelgazar)',
    'Se reducen unos azúcares durante unas semanas y después se reintroducen para saber cuáles toleras. Las guías recomiendan hacerla con un dietista-nutricionista. Guía completa.',
    kicker='Mitos', title='Lo que la dieta FODMAP no es', list=['No es para siempre', 'No es para adelgazar', 'No trata la causa del SIBO'])
pin(PI, 'curiosidad', 8, D, 'Cuándo no conviene empezar la dieta FODMAP por tu cuenta',
    'Según la AGA, no conviene empezarla sola si tienes o has tenido un trastorno de la conducta alimentaria o riesgo de desnutrición. En embarazo, lactancia y niños, solo con supervisión.',
    kicker='Importante', title='Cuándo no hacerla por tu cuenta', list=['Trastorno de la conducta alimentaria', 'Riesgo de desnutrición', 'Embarazo, lactancia o niños'])
pin(PI, 'curiosidad', 12, D, 'Dieta FODMAP: de sustitución, no de eliminación',
    'Monash insiste en que no se trata de quitar alimentos sino de cambiarlos por otros del mismo grupo con menos FODMAP, para que la dieta siga siendo variada. Guía de la dieta baja en FODMAP.',
    kicker='Cambio de enfoque', title='Sustituir, no eliminar', list=['Pan de trigo → masa madre', 'Leche → leche sin lactosa', 'Manzana → kiwi o naranja'])
pin(PI, 'pregunta', 6, D, '¿Y si la dieta FODMAP no me funciona?',
    'La AGA la plantea como una prueba: si en 4 a 6 semanas los síntomas no mejoran, probablemente los FODMAP no son tu problema. Vuelve a comer con normalidad y coméntalo con tu médico.',
    kicker='Pregunta frecuente', title='¿Y si no noto mejoría?', answer=['Es una prueba de 4-6 semanas', 'Si no mejora, no sigas restringiendo', 'Coméntalo con tu médico'])
pin(PI, 'curiosidad', 69, D, 'FODMAP no son malos: por qué no hay que quitarlos para siempre',
    'Muchos alimentos ricos en FODMAP son muy saludables. La dieta no busca quitarlos para siempre, sino averiguar cuáles te sientan mal a ti y en qué cantidad. Guía completa con fuentes.',
    kicker='Para pensarlo', title='Los FODMAP no son malos', list=['Están en alimentos muy sanos', 'Solo molestan a un intestino sensible', 'La meta es saber cuánto toleras'])

SI = 'sibo-imo-sintomas-diagnostico-tratamiento-evidencia'
pin(SI, 'versus', 55, S, 'SIBO e IMO: en qué se diferencian',
    'En el SIBO de hidrógeno suelen predominar el dolor, la hinchazón y la diarrea; en el IMO, el metano se asocia a tránsito lento y estreñimiento. Diferencias explicadas con base científica.',
    kicker='Entiéndelo', title='SIBO e IMO no son lo mismo', a=['SIBO', 'hidrógeno', 'Diarrea', 'y urgencia'], b=['IMO', 'metano', 'Estreñimiento', 'y tránsito lento'], note='Hay también patrones mixtos.', source='')
pin(SI, 'lista', 56, S, 'Síntomas más frecuentes del SIBO y del IMO',
    'Hinchazón visible al final del día, dolor, gases, eructos, ruidos intestinales y cambios en el ritmo intestinal. Si te reconoces, consúltalo con tu médico de digestivo.',
    kicker='Síntomas', title='Síntomas frecuentes de SIBO e IMO', unit='Los más habituales',
    rows=[['Hinchazón', 'al final del día'], ['Dolor y gases', 'eructos, ruidos'], ['Diarrea', 'más en SIBO'], ['Estreñimiento', 'más en IMO']], source='')
pin(SI, 'curiosidad', 55, S, 'Cómo se diagnostica el SIBO: la prueba de aliento',
    'La prueba más usada es la de aliento con lactulosa o glucosa, que mide hidrógeno y metano. El cultivo de aspirado es la referencia, pero es invasivo. Siempre interpretada por profesionales.',
    kicker='Diagnóstico', title='Cómo se diagnostica el SIBO', list=['Prueba de aliento: la más usada', 'Mide hidrógeno y metano', 'La interpreta un profesional'])
pin(SI, 'curiosidad', 57, S, 'Factores de riesgo del SIBO: por qué aparece',
    'Alteraciones de la motilidad intestinal, cirugías digestivas previas o el uso prolongado de omeprazol y similares favorecen el SIBO. Identificarlos es clave para evitar recaídas.',
    kicker='Por qué aparece', title='Factores que favorecen el SIBO', list=['Motilidad intestinal lenta', 'Cirugías digestivas previas', 'Uso prolongado de omeprazol'])
pin(SI, 'curiosidad', 57, S, 'Dieta y SIBO: lo que puede y no puede hacer',
    'La dieta baja en FODMAP ayuda a reducir la hinchazón en muchas personas, pero por sí sola no suele resolver el sobrecrecimiento. El tratamiento lo decide tu médico de digestivo.',
    kicker='Con evidencia', title='Qué puede hacer la dieta con el SIBO', list=['Reducir la fermentación', 'Aliviar la hinchazón', 'No sustituye al tratamiento médico'])

QS = 'que-es-el-sibo-sintomas-y-diagnostico'
pin(QS, 'foto', 56, S, 'Qué es el SIBO: síntomas y cómo se diagnostica',
    'Exceso de bacterias en el intestino delgado que fermentan los alimentos y causan hinchazón, gases, dolor y diarrea o estreñimiento. Qué es, cómo se diagnostica y qué hacer.',
    kicker='Guía básica', title='¿Qué es el SIBO?', sub='Síntomas, diagnóstico y qué hacer')
pin(QS, 'curiosidad', 56, S, 'Qué hacer si el test de SIBO sale positivo',
    'El tratamiento lo decide tu médico. Lo que está en tu mano desde el primer día: dieta baja en FODMAP, comidas regulares sin picar entre horas y reintroducción progresiva cuando mejores.',
    kicker='Primeros pasos', title='Test positivo de SIBO: y ahora qué', list=['Tratamiento: lo decide tu médico', 'Dieta baja en FODMAP', 'Comidas regulares, sin picar'])

RE = 'como-reintroducir-alimentos-despues-de-sibo'
pin(RE, 'foto', 8, S, 'Cómo reintroducir alimentos después del SIBO',
    'La fase de reintroducción no es opcional: sirve para saber qué FODMAP toleras y en qué cantidad. Protocolo de 3 días de Monash, alimentos para cada grupo y qué hacer si aparecen síntomas.',
    kicker='Después del tratamiento', title='Cómo reintroducir alimentos', sub='El protocolo de 3 días paso a paso')
pin(RE, 'lista', 6, S, 'Reintroducción FODMAP: qué alimento usar para cada grupo',
    'Fructosa: miel o mango. Lactosa: leche o yogur. Sorbitol: aguacate. Manitol: champiñones. GOS: garbanzos. Fructanos: pan de trigo o ajo. Tabla de dosis en el artículo.',
    kicker='Tabla para guardar', title='Un alimento para probar cada grupo', unit='Alimento de prueba',
    rows=[['Fructosa', 'miel o mango'], ['Lactosa', 'leche o yogur'], ['Sorbitol', 'aguacate'], ['Manitol', 'champiñones'], ['GOS', 'garbanzos cocidos']], source='Protocolo de la Universidad de Monash')
pin(RE, 'curiosidad', 7, S, 'La regla de los 3 días para reintroducir FODMAP',
    'Día 1, cantidad pequeña; día 2, ración habitual; día 3, cantidad generosa. Después, 2 o 3 días de descanso con la dieta base. Así se prueba cada grupo FODMAP según Monash.',
    kicker='Protocolo de Monash', title='La regla de los 3 días', list=['Día 1: cantidad pequeña', 'Día 2: ración habitual', 'Día 3: cantidad generosa', 'Descanso de 2-3 días'])
pin(RE, 'pregunta', 8, S, '¿Cuándo empezar la reintroducción tras el SIBO?',
    'Cuando tus síntomas principales hayan mejorado claramente y lleves una semana sin molestias notables con la dieta base. Si sigues con molestias intensas, consúltalo antes.',
    kicker='Pregunta frecuente', title='¿Cuándo empiezo a reintroducir?', answer=['Síntomas claramente mejores', 'Una semana sin molestias', 'Si no, consulta antes'])
pin(RE, 'curiosidad', 6, S, 'Qué hacer si un alimento te sienta mal al reintroducirlo',
    'Detén la prueba, apunta el resultado y vuelve a la dieta base 3 o 4 días antes de probar otro grupo. Reaccionar a uno o dos grupos es normal. Guía de reintroducción.',
    kicker='Si hay síntomas', title='Si un alimento te sienta mal', list=['Detén la prueba', 'Apunta el resultado', 'Vuelve a la dieta base 3-4 días', 'Reevalúalo en 3-6 meses'])
pin(RE, 'curiosidad', 7, S, 'El error de quedarse en la dieta baja en FODMAP para siempre',
    'Mantener la restricción más de 6 a 8 semanas empobrece la dieta, puede afectar a las bacterias beneficiosas y aumenta el miedo a comer. Por eso la reintroducción es clave.',
    kicker='Error común', title='No te quedes en la fase estricta', list=['Empobrece la dieta', 'Afecta a las bacterias buenas', 'Aumenta el miedo a comer'])

QL = 'bowl-quinoa-pollo-baja-fodmap-sibo'
pin(QL, 'pregunta', 46, D, '¿Se puede comer quinoa con SIBO? Sí, con esta ración',
    'Según Monash, la quinoa cocida es baja en FODMAP hasta 155 g por ración, una taza o unos 55 g en crudo. Uno de los cereales mejor tolerados con SIBO. Receta de bowl de quinoa con pollo.',
    kicker='Pregunta frecuente', title='¿Puedo comer quinoa con SIBO?', answer=['Sí, es de los mejor tolerados', 'Cocida: hasta 155 g', 'Unos 55 g en crudo'], source=M)
pin(QL, 'lista', 26, D, 'Quinoa y FODMAP: cocida, en copos o en harina',
    'Quinoa cocida hasta 155 g, copos de quinoa 45-50 g y harina de quinoa hasta 100 g por ración, según Monash. Lávala bien antes de cocerla para quitar el amargor.',
    kicker='Raciones', title='Cuánta quinoa puedes comer', unit='Ración baja en FODMAP',
    rows=[['Quinoa cocida', 'hasta 155 g'], ['Copos de quinoa', '45-50 g'], ['Harina de quinoa', 'hasta 100 g']], source=M)

# Pines extra para llegar a 150
pin(V, 'curiosidad', 69, D, 'Con qué sustituir la cebolla y el ajo en tus guisos',
    'La parte verde del puerro o de la cebolleta, el hinojo para un toque anisado y un caldo casero de zanahoria y chirivía. Tabla de sustituciones en la guía de verduras bajas en FODMAP.',
    kicker='Sustituciones', title='Sabor sin cebolla en tus guisos', list=['Verde del puerro o cebolleta', 'Bulbo de hinojo', 'Caldo de zanahoria y chirivía'])
pin(LG, 'curiosidad', 25, D, 'Cuántas raciones salen de un bote de legumbres',
    'Un bote estándar de 400 g suele tener unos 240 g escurridos: entre 2 y 4 raciones bajas en FODMAP según la legumbre. Pesa la ración las primeras veces. Guía de legumbres y SIBO.',
    kicker='Truco práctico', title='¿Cuántas raciones da un bote?', list=['Bote de 400 g: unos 240 g escurridos', 'Entre 2 y 4 raciones', 'Pésalas las primeras veces'])
pin(CI, 'curiosidad', 45, C, 'Colon irritable con estreñimiento: ideas que ayudan',
    'Fruta como el kiwi (hasta 2 unidades), avena, agua suficiente y comidas regulares. Ideas para el colon irritable con estreñimiento en nuestra guía práctica con menús de un día.',
    kicker='SII con estreñimiento', title='Ideas si predomina el estreñimiento', list=['Kiwi verde, hasta 2', 'Avena en el desayuno', 'Beber suficiente agua'])
pin(NV, 'curiosidad', 29, N, 'Menú de Nochebuena bajo en FODMAP: el orden de los platos',
    'Langostinos con mayonesa de limón y eneldo, consomé sin cebolla, paletilla de cordero con patatas y romero, y turrón de chocolate. Así queda una Nochebuena apta para SIBO.',
    kicker='Nochebuena', title='Una Nochebuena apta para SIBO', list=['Langostinos con mayonesa de limón', 'Consomé sin cebolla', 'Cordero con patatas', 'Turrón de chocolate'])
pin(NV, 'pregunta', 29, N, '¿Puedo comer castañas con SIBO?',
    'Sí: las castañas están entre los frutos secos mejor tolerados en la dieta baja en FODMAP. Un cucurucho pequeño compartido es un buen picoteo de Navidad. Más trucos en el menú navideño bajo en FODMAP.',
    kicker='Pregunta frecuente', title='¿Puedo comer castañas con SIBO?', answer=['Sí, son bajas en FODMAP', 'De los frutos secos mejor tolerados', 'Un cucurucho pequeño compartido'])

# Recorte a 150 (quitados por repetitivos: 3 de Navidad y 2 de colon irritable)
_QUITAR = {109, 111, 119, 123, 153}
PINS[:] = [p for i, p in enumerate(PINS) if i not in _QUITAR]
assert len(PINS) == 150
