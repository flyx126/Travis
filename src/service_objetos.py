from src.modelos import ProductoMasVendido, UtilidadPorHora, CostoPorHora, VentaPorHora
from src.modelos import Mesero, MontoVolumen, Response
from src import dao_queries as dao
from datetime import datetime
from src.log import log

def ultima_fecha(columna1):
    log.info("Consulta Service Ultima Fecha")
    query=dao.ultima_fecha(columna1)
    log.info(len(query))
    return query

def producto_mas_vendido_query(fecha):
    log.info("Consulta Service Producto Mas Vendido")
    lista_producto_mas_vendido_platillos=[]
    lista_producto_mas_vendido_bebidas=[]
    lista_producto_mas_vendido_vinos=[]
    diccionario=dao.query_producto_mas_vendido(fecha)
    for d in diccionario:
        fecha_final=d['fecha'].strftime('%Y-%m-%d')
        p=ProductoMasVendido(fecha=fecha_final,nombre=d['nombre'],cantidad_platillos=d['cantidad_platillos'],\
            cantidad_bebidas=d['cantidad_bebidas'],cantidad_vinos=d['cantidad_vinos'],grupo_platillo=d['grupo_platillo'])
        if d['grupo_platillo'].startswith('A'):
            lista_producto_mas_vendido_platillos.append(p.__dict__)
        elif d['grupo_platillo'].startswith('B'):
            lista_producto_mas_vendido_bebidas.append(p.__dict__)
        elif d['grupo_platillo'].startswith('V'):
            lista_producto_mas_vendido_vinos.append(p.__dict__)            
    log.info(len(lista_producto_mas_vendido_bebidas))
    log.info(len(lista_producto_mas_vendido_platillos))
    log.info(len(lista_producto_mas_vendido_vinos))
    return lista_producto_mas_vendido_bebidas,lista_producto_mas_vendido_platillos,lista_producto_mas_vendido_vinos
    
def utilidad_por_hora_query(fecha):
    log.info("Consulta Service Utilidad Por Hora")
    lista_utilidad_por_hora=[]
    diccionario=dao.query_utilidad_por_hora(fecha)
    for d in diccionario:
        u=UtilidadPorHora(hora=d['hora_vendido'],utilidad=d['utilidad_total'],utilidad_bebidas_hora=d['utilidad_bebidas'],\
            utilidad_platillos_hora=d['utilidad_platillos'],utilidad_vinos_hora=d['utilidad_vinos'])
        lista_utilidad_por_hora.append(u.__dict__)
    log.info(len(lista_utilidad_por_hora))
    return lista_utilidad_por_hora

def costo_por_hora_query(fecha):
    log.info("Consulta Service Costo Por Hora")
    lista_costo_por_hora=[]
    diccionario=dao.query_costo_por_hora(fecha)
    for d in diccionario:
        c=CostoPorHora(hora=d['hora_vendido'],costo=d['costo_total'],costo_bebidas_hora=d['costo_bebidas'],\
            costo_platillos_hora=d['costo_platillos'],costo_vinos_hora=d['costo_vinos'])
        lista_costo_por_hora.append(c.__dict__)
    log.info(len(lista_costo_por_hora))
    return lista_costo_por_hora

def venta_por_hora_query(fecha):
    log.info("Consulta Service Venta Por Hora")
    lista_venta_por_hora=[]
    diccionario=dao.query_venta_por_hora(fecha)
    for d in diccionario:
        v=VentaPorHora(dinero=d['dinero'],hora=d['hora'],volumen_venta=d['volumen_venta'],\
            volumen_venta_bebidas_hora=d['volumen_venta_bebidas_hora'],volumen_venta_platillos_hora=d['volumen_venta_platillos_hora'],\
                volumen_venta_vinos_hora=d['volumen_venta_vinos_hora'],monto_venta_bebidas_hora=d['monto_venta_bebidas_hora'],monto_venta_platillos_hora=d['monto_venta_platillos_hora'],\
                    monto_venta_vinos_hora=d['monto_venta_vinos_hora'])
        lista_venta_por_hora.append(v.__dict__)
    log.info(len(lista_venta_por_hora))
    return lista_venta_por_hora

def mesero_query(fecha):
    log.info("Consulta Service Mesero")
    lista_mesero=[]
    lista_venta=[]
    diciconario=dao.query_mesero(fecha)
    for d in diciconario:
        m=Mesero(nombre=d['nombre'],utilidad=d['utilidad'],venta=d['venta'],monto_bebidas=d['monto_bebidas'],\
            monto_platillos=d['monto_platillos'],monton_vinos=d['monto_vinos'],volumen_platillos=d['volumen_platillos'],\
                volumen_bebidas=d['volumen_bebidas'],volumen_vinos=d['volumen_vinos'])
        lista_mesero.append(m.__dict__)
    for x in lista_mesero:
        lista_venta.append(x['venta'])
    lista_venta.sort(reverse=True)
    mayor_venta='{0:,.2f}'.format(lista_venta[0])
    return lista_mesero,mayor_venta

def monto_volumen(fecha):
    log.info("Consulta Service Monto Volumen")
    lista_valores=[]
    diccionario=dao.query_monto_volumen(fecha)
    for d in diccionario:
        val=MontoVolumen(monto='{0:,.2f}'.format(d['monto']),volumen='{0:,.2f}'.format(d['volumen']),utilidad='{0:,.2f}'.format(d['utilidad']),\
            costo='{0:,.2f}'.format(d['costo']),personas=d['personas'],venta=d['monto'])
        lista_valores.append(val.__dict__)
    log.info(len(lista_valores))
    return lista_valores

def return_final_response():
    log.info("Consulta Service Final Response")
    fecha=ultima_fecha('fecha')
    bebidas,platillos,vinos=producto_mas_vendido_query(fecha)

    return Response(producto_mas_vendido_bebidas=bebidas,\
            producto_mas_vendido_platillos=platillos, producto_mas_vendido_vinos=vinos,\
                utilidad_por_hora=utilidad_por_hora_query(fecha),costo_por_hora=costo_por_hora_query(fecha),\
                    venta_por_hora=venta_por_hora_query(fecha),mesero=mesero_query(fecha),monto_volumen=monto_volumen(fecha))
