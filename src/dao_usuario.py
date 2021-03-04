import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct
from sqlalchemy import exc
from src.db import Db
from src.properties_usuario import PropertiesUsuario
from src.log import log
from src.customException import BadRequest

db = Db()
queries=PropertiesUsuario()

def nuevo_usuario(nombre,apellido,username,password):
    engine=db.create_session()
    nombre=nombre.strip()
    apellido=apellido.strip()
    username=username.strip()
    password=password.strip()
    engine.execute(sqlalchemy.text(queries.NUEVO_USUARIO.format(nombre,apellido,username,password)))
    return log.info("Consulta Dao Nuevo Usuario")
    
def eliminar_usuario(nombre,apellido):
    nombre=nombre.strip()
    apellido=apellido.strip()
    engine=db.create_session()
    engine.execute(sqlalchemy.text(queries.ELIMINAR_USUARIO.format(nombre,apellido)))
    return log.info("Consulta Dao Eliminar Usuario")

def seleccion_usuario():
    engine=db.create_session()
    query=engine.execute(sqlalchemy.text(queries.SELECCION_USUARIO))
    lista_diccionario=[]
    for x in query:
        lista_diccionario.append(x)
    return lista_diccionario