import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func,select, distinct, create_engine, MetaData, Table, Column, Integer, String,Float,Date,Time
from dbfread import DBF
import pandas as pd
from datetime import datetime
import rutas as ppt
from simpledbf import Dbf5

ruta_notven=ppt.ruta_notven
ruta_inventario=ppt.ruta_inventario
ruta_cat_meseros=ppt.ruta_cat_meseros

engine = create_engine('postgresql://postgres:12345@localhost:5432/Dashboard-Toscalia')
engine.connect()
base = automap_base()
base.prepare(engine, reflect=True)
session = Session(engine)

def lectura_tablas(nombre_tabla):
    table_ventas = DBF(f'{nombre_tabla}', load=True,ignore_missing_memofile=True)
    table_new=[]
    for record in table_ventas.records:
        table_new.append(record)
    dataframe= pd.DataFrame(table_new)
    return dataframe

inventario=lectura_tablas(ruta_notven)
costos_IN=inventario[['AUXCOSP','DESCR','UNIDAD','GRUPPLAT']].copy()
costos_IN=costos_IN.rename(columns={'AUXCOSP':'auxcosp','DESCR':'descr','UNIDAD':'unidad','GRUPPLAT':'grupplat'}) 
for x in costos_IN.columns:
    try:
        costos_IN[x]=costos_IN[x].str.replace(" ","")
    except:
        pass  
costos_IN.to_sql('costo_inventario', engine, if_exists='replace')





