import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct
from sqlalchemy import exc
from src.db import Db
from src.properties_demanda import PropertiesDemanda
from src.log import log
from src.customException import BadRequest
from datetime import datetime, timedelta 

db = Db()
queries=PropertiesDemanda()

def query_distribucion_demanda(fecha_menor,fecha_mayor):
    engine=db.create_session()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_DISTRIBUCION.format(fecha_menor,fecha_mayor)))
    lista_diccionario =[]
    for c in consulta:
        lista_diccionario.append(c)
    log.info("Consulta Dao Distribucion Demanda")
    return lista_diccionario
