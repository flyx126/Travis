import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func,select, distinct, create_engine, MetaData, Table, Column, Integer, String,Float,Date,Time
import pandas as pd
import rutas as ppt


engine = create_engine(f'postgresql://postgres:12345@localhost:5432/Dashboard-Toscalia')
engine.connect()

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
meta.create_all(engine)




tbl_maestra_2015=pd.read_csv("/home/ubuntu/tablas/tabla_maestra_2015.csv")
tbl_maestra_2016=pd.read_csv("/home/ubuntu/tablas/tabla_maestra_2016.csv")
tbl_maestra_2017=pd.read_csv("/home/ubuntu/tablas/tabla_maestra_2017.csv")
tbl_maestra_2018=pd.read_csv("/home/ubuntu/tablas/tabla_maestra_2018.csv")
tbl_maestra_2019=pd.read_csv("/home/ubuntu/tablas/tabla_maestra_2019.csv")
tbl_maestra_2020=pd.read_csv("/home/ubuntu/tablas/tabla_maestra_2020.csv")
costo_inventario=pd.read_csv("/home/ubuntu/tablas/costo_inventario.csv")
tbl_maestra_2015=tbl_maestra_2015.drop(['Unnamed: 0'],axis=1)
tbl_maestra_2016=tbl_maestra_2016.drop(['Unnamed: 0'],axis=1)
tbl_maestra_2017=tbl_maestra_2017.drop(['Unnamed: 0'],axis=1)
tbl_maestra_2018=tbl_maestra_2018.drop(['Unnamed: 0'],axis=1)
tbl_maestra_2019=tbl_maestra_2019.drop(['Unnamed: 0'],axis=1)
tbl_maestra_2020=tbl_maestra_2020.drop(['Unnamed: 0'],axis=1)

tbl_maestra_2015.to_sql('tbl_maestra',engine,if_exists='append',index=False,chunksize=10000,method='multi')
print("2015")
tbl_maestra_2016.to_sql('tbl_maestra',engine,if_exists='append',index=False,chunksize=10000,method='multi')
print("2016")
tbl_maestra_2017.to_sql('tbl_maestra',engine,if_exists='append',index=False,chunksize=10000,method='multi')
print("2017")
tbl_maestra_2018.to_sql('tbl_maestra',engine,if_exists='append',index=False,chunksize=10000,method='multi')
print("2018")
tbl_maestra_2019.to_sql('tbl_maestra',engine,if_exists='append',index=False,chunksize=10000,method='multi')
print("2019")
tbl_maestra_2020.to_sql('tbl_maestra',engine,if_exists='append',index=False,chunksize=10000,method='multi')
print("2020")
costo_inventario.to_sql("costo_inventario",engine,if_exists='replace',index=False,chunksize=10000,method='multi')
print("costo_inventario")