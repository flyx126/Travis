from src.modelos import Usuario
from src import dao_usuario as dao
from datetime import datetime
from src.log import log

def nuevo_usuario(nombre,apellido,username,password):
    query=dao.nuevo_usuario(nombre,apellido,username,password)
    return log.info("Consulta Service Nuevo Usuario")

def eliminar_usuario(nombre,apellido):
    query=dao.eliminar_usuario(nombre,apellido)

def seleccion_usuario():
    lista_usuarios=[]
    query=dao.seleccion_usuario()
    for x in query:
        usuarios=Usuario(nombre=x['nombre'],apellido=x['apellido'],username=x['username'],password=x['password'])
        lista_usuarios.append(usuarios.__dict__)
    return lista_usuarios



