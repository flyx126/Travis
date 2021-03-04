from src.modelos import DistrubicionDemanda,DistribucionResponse
from src import dao_queries_demanda as dao
from datetime import datetime
from src.log import log
import numpy as np
import pandas as pd


def distribucion_demanda_mes(fecha_menor,fecha_mayor):
    log.info("Consulta Service Distribucion de la Demanda por Mes")
    funcion_cluster=dao.query_distribucion_demanda(fecha_menor,fecha_mayor)
    funcion_cluster_pd = pd.DataFrame(funcion_cluster, columns=["notven", "descripcion", "hora", "pers","dia_vendido", "fecha", "utilidad", "grupo platillo", "cantidad"])
    res = funcion_cluster_pd.groupby("notven")["hora"].agg(hora_inicial="min", hora_final="max").reset_index()
    res['hora'] = res['hora_inicial'].map(lambda x: float(str(x).split(':')[0]))
    res['horario'] = pd.cut(res['hora'], bins=10)
    res['tiempo_estadia'] = (pd.to_datetime(res['hora_final'].astype(str)) - pd.to_datetime(res['hora_inicial'].astype(str)))
    res = res[['notven', 'tiempo_estadia']]
    tiempo_estadia_pd = res.join(funcion_cluster_pd.set_index('notven'), on='notven')
    tiempo_estadia_pd = tiempo_estadia_pd[['notven', 'descripcion', 'pers',
                                        'dia_vendido', 'fecha', 'utilidad', 'grupo platillo', 'cantidad', 'tiempo_estadia']]
    tiempo_estadia_pd['fecha'] = pd.to_datetime(tiempo_estadia_pd['fecha'])
    tiempo_estadia_pd['dia_semana'] = tiempo_estadia_pd['fecha'].dt.day_name()

    limpieza_cluster_df=tiempo_estadia_pd

    limpieza_cluster_df['Categoria'] = 'Sin Categoria'
    
    # Clasificación por alimentos
    grupplat_alimentos=['A11','A12','A13','A14','A15','A16','A17','A18','A19','A21','A22','A23','A7','AS',
                        'A101','A102','A111','A112','A24','A4','A81','A82','A83','O1']
    for x in grupplat_alimentos:
        limpieza_cluster_df["Categoria"][(limpieza_cluster_df['grupo platillo'] == x)] = "alimentos"
    
    
    grupplat_alcohol=['B1','B10','B11','B12','B14','B15','B17','B18','B2','B3','B5','B6','B7','B8','B9','B191']
    for x in grupplat_alcohol:
        limpieza_cluster_df["Categoria"][(limpieza_cluster_df['grupo platillo'] == x)] = "alcohol"

    grupplat_vinos=['V1','V11','V14','V17','V18','V2','V29','V3','V6','V7','V4']
    for x in grupplat_vinos:
        limpieza_cluster_df["Categoria"][(limpieza_cluster_df['grupo platillo'] == x)] = "vinos"

        
    # Clasificación categoría Bebidas No Alcohólicas
    limpieza_cluster_df["Categoria"][(limpieza_cluster_df['grupo platillo'] == 'B13')] = "bebidas_no_alcoholicas"

    # Clasificación Categoría Postres
    limpieza_cluster_df["Categoria"][(limpieza_cluster_df['grupo platillo'] == 'A20')] = "postres"

    # Clasificación categoría Café
    limpieza_cluster_df["Categoria"][(limpieza_cluster_df['grupo platillo'] == 'B16')] = "cafe"

    # Tabla por Dia de la Semana y Categoria

    cluster_por_dia = limpieza_cluster_df[['Categoria', 'cantidad', 'dia_semana']]
    cluster_pivote_semana = cluster_por_dia.pivot_table(index=['dia_semana'], columns='Categoria', aggfunc='sum', fill_value=0, values='cantidad')
    cluster_pivote_semana.columns = [''.join(x).replace('Categoria', '') for x in cluster_pivote_semana.columns]
    cluster_pivote_semana.reset_index(inplace=True)

    # Tabla por Dia Vendido y Categoria
    cluster_pivote_dia = limpieza_cluster_df.pivot_table(index=['dia_vendido'], columns='Categoria', aggfunc='sum', fill_value=0, values='cantidad')
    cluster_pivote_dia.columns = [''.join(x).replace('Categoria', '') for x in cluster_pivote_dia.columns]
    cluster_pivote_dia.reset_index(inplace=True)

    # Tabla por Tiempo de Estadía y Categoria
    cluster_pivote_tiempo = limpieza_cluster_df.pivot_table(index=['tiempo_estadia'], columns='Categoria', aggfunc='sum', fill_value=0, values='cantidad')
    cluster_pivote_tiempo.columns = [''.join(x).replace('Categoria', '') for x in cluster_pivote_tiempo.columns]
    cluster_pivote_tiempo.reset_index(inplace=True)
    cluster_pivote_tiempo['minutos'] = cluster_pivote_tiempo['tiempo_estadia'].dt.total_seconds()/60
    cluster_pivote_tiempo['minutos'].map(lambda x: float(x))
    cluster_pivote_tiempo['tiempo_estadia'].map(lambda x: str(x).replace('0 days ', ""))
    cluster_pivote_tiempo[cluster_pivote_tiempo['minutos'] == 1400]
    cluster_final_tiempo = cluster_pivote_tiempo[(
    cluster_pivote_tiempo['minutos'] <= 200) & (cluster_pivote_tiempo['minutos'] >= 40)]
    cluster_final_tiempo = cluster_final_tiempo[['alcohol', 'alimentos', 'bebidas_no_alcoholicas', 'cafe', 'postres', 'vinos', 'minutos']]

    distribucion_semana=DistrubicionDemanda(dia=cluster_pivote_semana['dia_semana'].tolist(),alcohol=cluster_pivote_semana['alcohol'].tolist(),\
                                        alimentos=cluster_pivote_semana['alimentos'].tolist(),bebidas_no_alcoholicas=cluster_pivote_semana['bebidas_no_alcoholicas'].tolist(),\
                                            cafe=cluster_pivote_semana['cafe'].tolist(),postres=cluster_pivote_semana['postres'].tolist(),vinos=cluster_pivote_semana['vinos'].tolist())
    
    distribucion_mes=DistrubicionDemanda(dia=cluster_pivote_dia['dia_vendido'].tolist(),alcohol=cluster_pivote_dia['alcohol'].tolist(),\
                                        alimentos=cluster_pivote_dia['alimentos'].tolist(),bebidas_no_alcoholicas=cluster_pivote_dia['bebidas_no_alcoholicas'].tolist(),\
                                            cafe=cluster_pivote_dia['cafe'].tolist(),postres=cluster_pivote_dia['postres'].tolist(),vinos=cluster_pivote_dia['vinos'].tolist())

    distribucion_tiempo=DistrubicionDemanda(dia=cluster_final_tiempo['minutos'].tolist(),alcohol=cluster_final_tiempo['alcohol'].tolist(),\
                                        alimentos=cluster_final_tiempo['alimentos'].tolist(),bebidas_no_alcoholicas=cluster_final_tiempo['bebidas_no_alcoholicas'].tolist(),\
                                            cafe=cluster_final_tiempo['cafe'].tolist(),postres=cluster_final_tiempo['postres'].tolist(),vinos=cluster_final_tiempo['vinos'].tolist())
    distribucion_semana_dict=distribucion_semana.__dict__
    distribucion_mes_dict=distribucion_mes.__dict__
    distribucion_tiempo_dict=distribucion_tiempo.__dict__
    
    return DistribucionResponse(semana=distribucion_semana_dict,mes=distribucion_mes_dict,tiempo=distribucion_tiempo_dict)

    
  
