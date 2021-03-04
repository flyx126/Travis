import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct
from sqlalchemy import exc
from src.db import Db
from src.properties_tendencia import PropertiesTendencia
from src.log import log
from src.customException import BadRequest
from datetime import datetime, timedelta 
import time

db = Db()
queries=PropertiesTendencia()

def query_tendencia(grupplat):
    
    engine=db.create_session()
    start=time.time()
    consulta=engine.execute(sqlalchemy.text(queries.QUERY_TENDENCIA.format(grupplat)))
    end=time.time()
    print("Engine Execute",end-start)
    lista_diccionario =[]
    start=time.time()
    # for c in consulta:
    #     lista_diccionario.append(c)
    lista_diccionario=list(consulta)
    end=time.time()
    print("For Query",end-start)
    log.info("Consulta Dao Tendencia Venta")
    return lista_diccionario
