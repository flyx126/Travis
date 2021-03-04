import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func,select, distinct, create_engine, MetaData, Table, Column, Integer, String,Float,Date,Time
from dbfread import DBF
from collections import OrderedDict
import pandas as pd
import re
from datetime import datetime,time
import logging
import rutas as ppt
import time
import numpy as np
start=time.time()

#Asignar rutas de archivos DBF a variables usadas en metodo de lectura de tablas DBF
ruta_notven=ppt.ruta_notven
ruta_inventario=ppt.ruta_inventario
ruta_cat_meseros=ppt.ruta_cat_meseros

log = logging.getLogger(__name__)
logging.basicConfig(filename='ETLdemo.log', level=logging.DEBUG)

# Metodo que abre una tabla DBF y la convierte en dataframe
def lectura_tablas(nombre_tabla):
    log.info(str(datetime.now())+" Iniciando metodo de lectura de tablas DBF y conversion a DataFrame")
    table_name=nombre_tabla
    table_ventas = DBF(f'{table_name}', load=True,ignore_missing_memofile=True)
    table_new=[]
    for record in table_ventas.records:
        table_new.append(record)
    dataframe= pd.DataFrame(table_new)
    log.info(str(datetime.now())+" Terminado metodo de lectura de tablas DBF y conversion a DataFrame")
    return dataframe

# Metodo que seleciona las columnas que se necesitan del dataframe creado 
def seleccionar_columnas(df_name,nombre_columnas=[]):
    log.info(str(datetime.now())+" Iniciando metodo de selección de columnas dataframe creado")
    df_limpio=df_name.loc[:,(nombre_columnas)]
    log.info(str(datetime.now())+" Terminado metodo de selección de columnas dataframe creado")
    return df_limpio

#Metodo que convierte los valores de las celdas del dataframe de hora en formato datetime de una columna seleccionada por el usuario
def formato_hora(df_name,columna_hora):
    log.info(str(datetime.now())+" Iniciando metodo de cambio de formato de columna hora")
    df_name[columna_hora]=pd.to_datetime(df_name[columna_hora],format='%H%M').dt.time
    log.info(str(datetime.now())+" Terminado metodo de cambio de formato de hora")


#Metodo para remover espacios
def limpiar_espacios_en_una_columna(df_name,columna):
    log.info(str(datetime.now())+" Iniciando metodo de limpieza de escpacios")
    data_type_dict=dict(df_name.dtypes)
    if data_type_dict[columna]=='O':
        if columna == "DESCR":
            df_name.loc[:,(columna)]=df_name.loc[:,(columna)].str.strip()
        else:
            df_name.loc[:,(columna)]=df_name.loc[:,(columna)].str.replace(" ","") 
    log.info(str(datetime.now())+" Terminado metodo de limpieza de escpacios")
    return df_name

#Metodo para remover valores NAN
def limpiar_nans(df_name):
    log.info(str(datetime.now())+" Iniciando metodo de limpieza de valores NAN")
    df_name=df_name.fillna(0)
    log.info(str(datetime.now())+" Terminado metodo de limpieza de valores NAN")
    return df_name

#Metodo para remover caracteres especiales definidos por el usuario
def limpiar_caracteres(df_name,columna,char=[]):
    log.info(str(datetime.now())+" Iniciando metodo de limpieza de caracteres especiales en columnas")
    data_type_dict=dict(df_name.dtypes)
    if data_type_dict[columna]=='O':
        for i in char:
                df_name.loc[:,(columna)]=df_name.loc[:,(columna)].str.replace(i,"")
 
    log.info(str(datetime.now())+" Terminado metodo de limpieza de caracteres especiales en columnas")
    return df_name

#Metodo que recorre las celdas del dataframe creado y llama los metodos para limpieza del dataframe
def recorrer_columnas_para_limpiar(df_name):
    log.info(str(datetime.now())+" Iniciando metodo de limpieza de columnas")
    columnas=df_name.columns
    limpiar_nans(df_name)
    try:
        for columnax in columnas:
            limpiar_espacios_en_una_columna(df_name,columnax)
            limpiar_caracteres(df_name,columnax,ppt.caracteres_especiales)
    except:
        print("No es posible limpiar columna "+columnax)
    log.info(str(datetime.now())+" Terminado metodo de limpieza de columnas")
    return df_name

#Metodo que establece los nombres de las columnas en letras minisculas
def renombrar_columnas(df_name):
    log.info(str(datetime.now())+" Iniciando metodo para renombrar columnas a minusculas")
    df_name.columns = map(str.lower, df_name.columns)
    log.info(str(datetime.now())+" Terminado metodo para renombrar columnas a minusculas")
    return df_name

#Metodo que quita el I.V.A al precio de venta del dataframe creado
def precio_sin_iva(df_name,columna_precio,impuesto):
    log.info(str(datetime.now())+" Iniciando metodo para quitar I.V.A. del precio de columna de precio")
    df_name.loc[:,(f"{columna_precio}")]=df_name.loc[:,(f"{columna_precio}")]*(1-impuesto)
    log.info(str(datetime.now())+" Terminado metodo para quitar I.V.A. del precio de columna de precio")
    return df_name
    
#Metodo que realiza la conexion con SQL
def conexion_SQL(usuario,contrasena,puerto,base_datos):
    log.info(str(datetime.now())+" Iniciando metodo para conexion a POSTGRESQL")
    connection_string = f"{usuario}:{contrasena}@localhost:{puerto}/{base_datos}"
    engine = create_engine(f'postgresql://{connection_string}')
    log.info(str(datetime.now())+" Terminado metodo para conexion a POSTGRESQL ")
    return engine

#mMetodo que envia el dataframe trabajado a una base de datos en Postgresql 
def enviar_sql(df_name,nombre_tabla,engine):
    log.info(str(datetime.now())+" Iniciando metodo para envio de tabla a POSTGRESQL")
    df_name.to_sql(name=f'{nombre_tabla}',con=engine,if_exists='append',index=False)
    log.info(str(datetime.now())+" Terminado metodo para envio de tabla a POSTGRESQL")
    return True

#Metodo que crea el dataframe df_notven a partir de una tabla DBF seleccionada por el usuario
def crear_df_notven():
    log.info(str(datetime.now())+" Iniciando metodo para creacion de dataframe notven")
    dataframe=lectura_tablas(ruta_notven)
    df_notven = seleccionar_columnas(dataframe,nombre_columnas=[ppt.df_columna_platillo,ppt.df_columna_precio,ppt.df_columna_cantidad,\
        ppt.df_columna_fecha,ppt.df_columna_mesero,ppt.df_columna_hora,ppt.df_columna_mesa,ppt.df_columna_notven,ppt.df_columna_pers,\
            ppt.df_columna_grupplat,ppt.df_columna_partida,ppt.df_columna_descuento])
    recorrer_columnas_para_limpiar(df_notven)
    renombrar_columnas(df_notven)
    df_notven=df_notven.rename(columns={"platillo":"clave"})
    precio_sin_iva(df_notven,"precio",0.16)
    log.info(str(datetime.now())+" Terminado metodo para creacion de dataframe notven")
    return df_notven

#Metodo que crea el dataframe df_inventario a partir de una tabla DBF seleccionada por el usuario
def crear_df_inventario():
    log.info(str(datetime.now())+" Iniciando metodo para creacion de dataframe inventario")
    dataframe=lectura_tablas(ruta_inventario)
    df_inventario = seleccionar_columnas(dataframe,nombre_columnas=[ppt.df_columna_clave,ppt.df_columna_descr,ppt.df_columna_costo,ppt.df_columna_unidad])
    recorrer_columnas_para_limpiar(df_inventario) 
    renombrar_columnas(df_inventario)
    log.info(str(datetime.now())+" Terminado metodo para creacion de dataframe inventario")
    return df_inventario

#Metodo que realiza una funcion merge para dos dataframes seleccionados por el usuario 
def merge_dataframes(dataframe1,dataframe2):
    log.info(str(datetime.now())+" Iniciando metodo para realizar merge de dataframes notven e inventario")
    df_merge=pd.merge(dataframe1,dataframe2,on='clave',how='right')
    df_merge=df_merge.dropna()
    df_merge['dia_vendido'] = pd.DatetimeIndex(df_merge['fecha']).day
    df_merge['mes_vendido'] = pd.DatetimeIndex(df_merge['fecha']).month
    df_merge['anio_vendido'] = pd.DatetimeIndex(df_merge['fecha']).year
    df_merge["utilidad"]=df_merge["precio"]-df_merge["costo"]
    df_merge["hora_vendido"]=df_merge["hora"].str[0:2]
    df_merge["hora_vendido"]=df_merge["hora_vendido"].astype(int)
    log.info(str(datetime.now())+" Terminado metodo para realizar merge de dataframes notven e inventario")
    return df_merge

#Metodo que abre un archivo CSV con la informacion de los nombres de los meseros y crea el dataframe cat_meseros
def crear_cat_meseros():
    log.info(str(datetime.now())+" Iniciando metodo para abrir archivo Catalogo de Meseros.csv y creacion dataframe cat_meseros")
    archivo=pd.read_csv(ruta_cat_meseros)
    cat_meseros=pd.DataFrame(archivo)
    log.info(str(datetime.now())+" Terminado metodo para abrir archivo Catalogo de Meseros.csv y creacion dataframe cat_meseros")
    return cat_meseros

#Metodo que realiza la funcion merge del catalogo de meseros creado y el dataframe seleccionado por el usuario
def crear_tabla_maestra(dataframe,cat_meseros):
    log.info(str(datetime.now())+" Iniciando metodo para creacion de dataframe tabla_maesta")
    df_merge=pd.merge(dataframe,cat_meseros,on='mesero',how='right')
    df_merge=df_merge.dropna()
    formato_hora(df_merge,"hora")
    df_merge=df_merge.rename(columns={"desc":"descuento"})
    log.info(str(datetime.now())+" Terminado metodo para creacion de dataframe tabla_maesta")
    return df_merge

#Metodo que crea la base de la tabla en SQL con los nombres de columnas necesarios
def crear_tabla_SQL(engine_conexion):
    log.info(str(datetime.now())+" Iniciando metodo para creacion de tabla_maesta en POSTGRESQL")
    meta = MetaData()
    tbl_maestra = Table(
    'tbl_maestra', meta, 
    Column(ppt.SQL_columna_id, Integer, primary_key = True),
    Column(ppt.SQL_columna_clave, String), 
    Column(ppt.SQL_columna_precio, Float),
    Column(ppt.SQL_columna_cantidad, Float),
    Column(ppt.SQL_columna_fecha, Date),
    Column(ppt.SQL_columna_mesero, String),
    Column(ppt.SQL_columna_hora, Time),
    Column(ppt.SQL_columna_mesa, String),
    Column(ppt.SQL_columna_notven, String),
    Column(ppt.SQL_columna_pers, Float),
    Column(ppt.SQL_columna_grupplat, String),
    Column(ppt.SQL_columna_partida, Float),
    Column(ppt.SQL_columna_descuento, Float),
    Column(ppt.SQL_columna_descr, String),
    Column(ppt.SQL_columna_costo, Float),
    Column(ppt.SQL_columna_unidad, String),
    Column(ppt.SQL_columna_dia_vendido, Float),
    Column(ppt.SQL_columna_mes_vendido, Float),
    Column(ppt.SQL_columna_anio_vendido, Float),
    Column(ppt.SQL_columna_utilidad, Float),
    Column(ppt.SQL_columna_hora_vendido, Float),
    Column(ppt.SQL_columna_nombre_mesero, String),
    )
    meta.create_all(engine_conexion)
    log.info(str(datetime.now())+" Terminado metodo para creacion de tabla_maesta en POSTGRESQL")
    return True
    
def main():
    log.info(str(datetime.now())+" Iniciando proceso ETL")
    df_notven=crear_df_notven()
    df_inventario=crear_df_inventario()
    df_notven_inventario=merge_dataframes(df_notven,df_inventario)
    cat_meseros=crear_cat_meseros()
    tabla_maestra=crear_tabla_maestra(df_notven_inventario,cat_meseros)
    taba_maestra.to_csv("tabla_maestra.csv")
    # engine=conexion_SQL(ppt.usuario,ppt.contrasena,ppt.puerto,ppt.base_datos)    
    # df_inventario.to_sql('costo_inventario',engine,if_exists='replace')
    # crear_tabla_SQL(engine)   
    # enviar_sql(tabla_maestra,'tbl_maestra_prueba',engine)
    # log.info(str(datetime.now())+ " Terminado proceso ETL")
end=time.time()
main()
print(end-start)

