SELECT SUM(cantidad),nombre_mesero FROM tbl_maestra WHERE fecha= '2020-03-20' AND grupplat NOT LIKE 'O%%'  GROUP BY nombre_mesero ORDER BY nombre_mesero ASC

SELECT DISTINCT(fecha) FROM tbl_maestra ORDER BY fecha DESC

SELECT nombre_mesero,SUM(utilidad) as utilidad, SUM(cantidad*precio) as venta, fecha,
SUM(cantidad) filter (WHERE grupplat LIKE 'A%') as volumen_platillos,
SUM(cantidad*precio) filter (WHERE grupplat LIKE 'A%') as monto_platillos,
SUM(cantidad) filter (WHERE grupplat LIKE 'B%') as volumen_bebidas,
SUM(cantidad*precio) filter (WHERE grupplat LIKE 'B%') as monto_bebidas,
SUM(cantidad) filter (WHERE grupplat LIKE 'V%') as volumen_vinos,
SUM(cantidad*precio) filter (WHERE grupplat LIKE 'V%') as monto_vinos
FROM tbl_maestra
WHERE fecha= '2020-03-20'
GROUP BY nombre_mesero,fecha
ORDER BY nombre_mesero ASC

SELECT descr as nombre, grupplat as grupo_platillo, fecha,
SUM(cantidad) filter (WHERE grupplat LIKE 'A%') as cantidad_platillos,
SUM(cantidad) filter (WHERE grupplat LIKE 'B%') as cantidad_bebidas,
SUM(cantidad) filter (WHERE grupplat LIKE 'V%') as cantidad_vinos
FROM tbl_maestra 
WHERE fecha = '2020-03-20'
AND grupplat NOT LIKE 'O%'
AND clave != '11083' AND clave != '2'
GROUP BY descr,grupplat,fecha
ORDER BY grupo_platillo ASC, SUM(cantidad) DESC

SELECT hora_vendido,sum(utilidad) as utilidad_total, fecha,
SUM(utilidad) filter (WHERE grupplat LIKE 'A%') as utilidad_platillos,
SUM(utilidad) filter (WHERE grupplat LIKE 'B%') as utilidad_bebidas,
SUM(utilidad) filter (WHERE grupplat LIKE 'V%') as utilidad_vinos
FROM tbl_maestra
WHERE fecha = '2020-03-20'
AND grupplat NOT LIKE 'O%'
AND clave != '11083' AND clave != '2'
GROUP BY hora_vendido,fecha
ORDER BY hora_vendido ASC

SELECT hora_vendido,sum(costo) as costo_total,
SUM(costo) filter (WHERE grupplat LIKE 'A%') as costo_platillos,
SUM(costo) filter (WHERE grupplat LIKE 'B%') as costo_bebidas,
SUM(costo) filter (WHERE grupplat LIKE 'V%') as costo_vinos
FROM tbl_maestra
WHERE fecha = '2020-03-10'
AND grupplat NOT LIKE 'O%'
AND clave != '11083' AND clave != '2'
GROUP BY hora_vendido
ORDER BY hora_vendido ASC

SELECT hora_vendido as hora, SUM(cantidad*precio) as dinero, SUM(cantidad) as volumen_venta,
SUM(cantidad) filter (WHERE grupplat LIKE 'A%') as volumen_venta_platillos_hora,
SUM(cantidad) filter (WHERE grupplat LIKE 'B%') as volumen_venta_bebidas_hora,
SUM(cantidad) filter (WHERE grupplat LIKE 'V%') as volumen_venta_vinos_hora
FROM tbl_maestra
WHERE fecha = '2020-03-10'
AND grupplat NOT LIKE 'O%'
AND clave != '11083' AND clave != '2'
GROUP BY hora_vendido
ORDER BY hora_vendido ASC

SELECT SUM(cantidad) as volumen, SUM(cantidad*precio) as monto
FROM tbl_maestra
WHERE fecha = '2020-03-10'
AND grupplat NOT LIKE 'O%'
AND clave != '11083' AND clave != '2'

SELECT DISTINCT(fecha) as ultima_fecha FROM tbl_maestra ORDER BY fecha DESC LIMIT 1


 

SELECT * FROM tbl_maestra
