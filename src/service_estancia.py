from src.modelos import Estancia
from src import dao_queries_estancia as dao
from datetime import datetime
from src.log import log
import numpy as np
import pandas as pd

def estancia(fecha_menor,fecha_mayor):
    log.info("Consulta Service Tiempo de estancia")
    funcion_tiempo=dao.query_estancia(fecha_menor,fecha_mayor)
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
    estancia=Estancia(tiempo=estadia_toscalia_final['minutos'].tolist())
    estancia_dict=estancia.__dict__

    return estancia_dict