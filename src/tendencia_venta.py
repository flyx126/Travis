import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct 
from sqlalchemy import exc
import numpy as np
import pandas as pd

def conexion_sql(usuario,contrasena,puerto,base_datos):
    connection_string = f'{usuario}:{contrasena}@localhost:{puerto}/{base_datos}'
    try:
        engine = create_engine(f'postgresql://{connection_string}')
        engine.connect()
        #log.info("Conexión exitosa")
        return engine
    except exc.SQLAlchemyError:
        raise BadRequest("atribute error conexion a SQL","conexion a SQL","Fatal",500)
    return True

def crear_session():
    engine1 = conexion_sql('postgres', '12345', '5432', 'Dashboard-Toscalia')
    base = automap_base()
    base.prepare(engine1, reflect=True)
    session = Session(engine1)
    return session,base

def funcion_consulta_demanda():
    try:
        engine = conexion_sql('postgres', '12345', '5432', 'Dashboard-Toscalia')
        consulta=engine.execute(f"SELECT descr,notven,cantidad,grupplat,anio_vendido,mes_vendido,pers FROM tbl_maestra WHERE grupplat LIKE 'A%%' GROUP BY notven,id ORDER BY notven ASC")
        grupos=[]
        for c in consulta:
            grupos.append(c)
        return grupos
    except AttributeError:
        raise BadRequest("atribute error funcion consulta 1","funcion consulta","Fatal",500)
    except exc.SQLAlchemyError:
        raise BadRequest("sqlalchemy error funcion consulta 1","funcion consulta","Fatal",400)


platillos_demanda=funcion_consulta_demanda()

platillos_demanda_pd=pd.DataFrame(platillos_demanda,columns=["descripcion","notven","cantidad","grupplat","año","mes","dia_vendido"])

sin_antipasti_demanda=platillos_demanda_pd.drop(platillos_demanda_pd[platillos_demanda_pd['descripcion']=='ANTIPASTI DE LA CASA'].index)
sin_com_demanda=sin_antipasti_demanda.drop(sin_antipasti_demanda[sin_antipasti_demanda['descripcion']=='COM'].index)
sin_segundo_demanda=sin_com_demanda.drop(sin_com_demanda[sin_com_demanda['descripcion']=='SEGUNDO TIEMPO'].index)
limpieza_platillos_demanda=sin_segundo_demanda.drop(sin_segundo_demanda[sin_segundo_demanda['descripcion']=='PESTO SSA'].index)
grupos_pd_platillos_demanda=limpieza_platillos_demanda['cantidad'].groupby([limpieza_platillos_demanda.año, limpieza_platillos_demanda.mes]).agg('sum').reset_index() 
grupos_pd_platillos_demanda['target']=grupos_pd_platillos_demanda['cantidad']
grupos_pd_platillos_demanda['target']=grupos_pd_platillos_demanda.target.shift(-1)
grupos_pd_platillos_demanda.dropna(inplace=True)

res_2016=grupos_pd_platillos_demanda['año']==2016.0
res_2017=grupos_pd_platillos_demanda['año']==2017.0
res_2018=grupos_pd_platillos_demanda['año']==2018.0
res_2019=grupos_pd_platillos_demanda['año']==2019.0
res_2020=grupos_pd_platillos_demanda['año']==2020.0

venta_platillos_2016=grupos_pd_platillos_demanda[res_2016].reset_index()
venta_platillos_2017=grupos_pd_platillos_demanda[res_2017].reset_index()
venta_platillos_2018=grupos_pd_platillos_demanda[res_2018].reset_index()
venta_platillos_2019=grupos_pd_platillos_demanda[res_2019].reset_index()
venta_platillos_2020=grupos_pd_platillos_demanda[res_2020].reset_index()

venta_platillos_2016=venta_platillos_2016.drop(columns='index')
venta_platillos_2017=venta_platillos_2017.drop(columns='index')
venta_platillos_2018=venta_platillos_2018.drop(columns='index')
venta_platillos_2019=venta_platillos_2019.drop(columns='index')
venta_platillos_2020=venta_platillos_2020.drop(columns='index')

# Envío tablas a sql 
# engine = conexion_sql('postgres', '12345', '5432', 'Dashboard-Toscalia')
# venta_platillos_2016.to_sql('venta_2016_tendencia', engine,if_exists='replace')
# venta_platillos_2017.to_sql('venta_2017_tendencia', engine,if_exists='replace')
# venta_platillos_2018.to_sql('venta_2018_tendencia', engine,if_exists='replace')
# venta_platillos_2019.to_sql('venta_2019_tendencia', engine,if_exists='replace')

print(venta_platillos_2020)