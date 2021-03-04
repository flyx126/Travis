import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct
from sqlalchemy import exc
from src.db import Db
from src.properties_queries_historicos import PropertiesQueriesHistorico
from src.log import log
from src.customException import BadRequest
from datetime import datetime, timedelta 

db = Db()
queries=PropertiesQueriesHistorico()

def query_mesero_historico(fecha_menor,fecha_mayor):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_MESERO_HISTORICO.format(fecha_menor,fecha_mayor)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Historicos Mesero Historico")
    return lista_diccionario

def query_producto_mas_vendido_historico(fecha_menor,fecha_mayor):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_PRODUCTOS_MAS_VENDIDO_HISTORICO.format(fecha_menor,fecha_mayor)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Historicos Producto Mas Vendido Historico")
    return lista_diccionario

def query_utilidad_por_hora_historico(fecha_menor,fecha_mayor):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_UTILIDAD_POR_HORA_HISTORICO.format(fecha_menor,fecha_mayor)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Historicos Utilidad Por Hora Historico")
    return lista_diccionario

def query_costo_por_hora_historico(fecha_menor,fecha_mayor):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_COSTO_POR_HORA_HISTORICO.format(fecha_menor,fecha_mayor)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Historicos Costo Por Hora Historico")
    return lista_diccionario

def query_venta_por_hora_historico(fecha_menor,fecha_mayor):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_VENTA_POR_HORA_HISTORICO.format(fecha_menor,fecha_mayor)))
    diccionario, lista_diccionario = {}, []
    for rowproxy in consulta:
        for column, value in rowproxy.items():
            if value==None:
                value=0
            diccionario = {**diccionario, **{column: value}}
        lista_diccionario.append(diccionario)
    log.info("Consulta Dao Historicos Venta Por Hora Historico")
    return lista_diccionario

def query_monto_volumen_historico(fecha_menor,fecha_mayor):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_MONTO_VOLUMEN_HISTORICO.format(fecha_menor,fecha_mayor)))
    consulta2=engine.execute(sqlalchemy.text(queries.QUERY_PERSONAS.format(fecha_menor,fecha_mayor)))
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
    log.info("Consulta Dao Historicos Monto Volumen")
    return lista_diccionario

