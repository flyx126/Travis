import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct
from sqlalchemy import exc
from src.db import Db
from src.properties_queries import PropertiesQueries
from src.log import log
from src.customException import BadRequest
from datetime import datetime, timedelta 

db = Db()
queries=PropertiesQueries()

def ultima_fecha(columna1):
    engine=db.create_session()
    make_query=engine.execute(queries.QUERY_ULTIMA_FECHA.format(columna1))
    diccionario, lista_diccionario = {}, []
    for rowproxy in make_query:
        for column, value in rowproxy.items():
            diccionario = {**diccionario, **{column: value.strftime('%Y-%m-%d')}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Ultima Fecha")
    return lista_diccionario[0]['ultima_fecha']
    

def query_mesero(fecha):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_MESERO.format(fecha)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Mesero")
    return lista_diccionario

def query_producto_mas_vendido(fecha):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_PRODUCTOS_MAS_VENDIDO.format(fecha)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Producto Mas Vendido")
    return lista_diccionario

def query_utilidad_por_hora(fecha):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_UTILIDAD_POR_HORA.format(fecha)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Utilidad Por Hora")
    return lista_diccionario

def query_costo_por_hora(fecha):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_COSTO_POR_HORA.format(fecha)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Costo Por Hora")
    return lista_diccionario

def query_venta_por_hora(fecha):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_VENTA_POR_HORA.format(fecha)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Venta Por Hora")
    return lista_diccionario

def query_monto_volumen(fecha):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_MONTO_VOLUMEN.format(fecha)))
    consulta2=engine.execute(sqlalchemy.text(queries.QUERY_PERSONAS.format(fecha)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    for row in consulta2:
        for column,value in row.items():
            diccionario[column]=value
    log.info("Consulta Dao Monto Volumen")
    return lista_diccionario

