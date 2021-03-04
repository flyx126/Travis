import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct 
from sqlalchemy import exc
import numpy as np
import pandas as pd
from datetime import datetime, date

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

def funcion_consulta_tiempo():
    try:
        engine = conexion_sql('postgres', '12345', '5432', 'Dashboard-Toscalia')
        consulta=engine.execute(f"select notven,hora,pers,mesa from tbl_maestra WHERE fecha='2019-03-01' GROUP BY notven,id ORDER BY notven ASC")
        grupos=[]
        for c in consulta:
            grupos.append(c)
        return grupos
    except AttributeError:
        raise BadRequest("atribute error funcion consulta 1","funcion consulta","Fatal",500)
    except exc.SQLAlchemyError:
        raise BadRequest("sqlalchemy error funcion consulta 1","funcion consulta","Fatal",400)

funcion_tiempo=funcion_consulta_tiempo()
funcion_tiempo_pd=pd.DataFrame(funcion_tiempo,columns=["notven","hora","pers","mesa"])
res = funcion_tiempo_pd.groupby("notven")["hora"].agg(hora_inicial="min", hora_final="max").reset_index()
res['hora']=res['hora_inicial'].map(lambda x: float(str(x).split(':')[0]))
res['horario']=pd.cut(res['hora'],bins=10)
res['tiempo_estadia']= (pd.to_datetime(res['hora_final'].astype(str)) - pd.to_datetime(res['hora_inicial'].astype(str)))
res=res[['notven','tiempo_estadia']]
tiempo_estadia_pd=res.join(funcion_tiempo_pd.set_index('notven'),on='notven')
tiempo_estadia_pd=tiempo_estadia_pd[['notven','pers','mesa','tiempo_estadia']]
estadia_toscalia=tiempo_estadia_pd.drop_duplicates()
estadia_toscalia['minutos'] = estadia_toscalia['tiempo_estadia'].dt.total_seconds()/60
estadia_toscalia['minutos'].map(lambda x: float(x))
estadia_toscalia['tiempo_estadia'].map(lambda x: str(x).replace('0 days ',""))
estadia_toscalia[estadia_toscalia['minutos']==1400]
estadia_toscalia_final=estadia_toscalia[(estadia_toscalia['minutos']<=200) & (estadia_toscalia['minutos']>=15)]
estadia_final=estadia_toscalia_final.values.tolist()

print(estadia_toscalia_final)
    

# #Envio Dataframe a POstgres 
# engine = conexion_sql('postgres', '12345', '5432', 'Dashboard-Toscalia')
# estadia_toscalia_final.to_sql('histograma', engine)