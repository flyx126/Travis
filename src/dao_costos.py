import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct
from sqlalchemy import exc
from src.db import Db
from src.properties_costos import PropertiesCostos
from src.log import log
from src.customException import BadRequest
from datetime import datetime, timedelta 

db = Db()
queries=PropertiesCostos()

def query_costos(fecha_menor,fecha_mayor):
    lista_diccionario=[]
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_COSTOS.format(fecha_menor,fecha_mayor)))
    for x in consulta:
        lista_diccionario.append(x)
    log.info("Consulta Dao Costos")
    return lista_diccionario

def query_costos_inventario():
    lista_diccionario=[]
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_COSTOS_INVENTARIO))
    for x in consulta:
        lista_diccionario.append(x)
    log.info("Consulta Dao Costos")
    return lista_diccionario

