import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from sqlalchemy import select, distinct 
from sqlalchemy import exc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, date
import datetime as dt
from functools import reduce
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import time

engine = create_engine('postgresql://postgres:12345@localhost:5432/Dashboard-Toscalia')
engine.connect()
base = automap_base()
base.prepare(engine, reflect=True)
session = Session(engine)

print("Ingresa el platillo que deseas analizar")
platillo=input()
platillo=str(platillo).strip().replace("  "," ")
print("Ingresa el año que quieres analizar")
anio=int(input())
start=time.time()
consulta=engine.execute(f"SELECT descr,notven,fecha,utilidad,cantidad,mesa,grupplat,mes_vendido,anio_vendido FROM tbl_maestra WHERE anio_vendido='{anio}' AND (notven) IN(SELECT notven from tbl_maestra where descr like '{platillo}') GROUP BY notven,id ORDER BY notven ASC")
notas_top_15=[]
for c in consulta:
    notas_top_15.append(c)
notas_top_15_pd=pd.DataFrame(notas_top_15,columns=["descripcion","notven","fecha","utilidad","cantidad","mesa","grupplat","mes_vendido","anio_vendido"])
notas_top_15_pd['fecha'] = pd.to_datetime(notas_top_15_pd['fecha'])
notas_top_15_pd['dia_semana'] = notas_top_15_pd['fecha'].dt.day_name() 
notas_top_15_pd=notas_top_15_pd.drop(notas_top_15_pd[notas_top_15_pd['descripcion']==platillo].index)
sin_antipasti_notas=notas_top_15_pd.drop(notas_top_15_pd[notas_top_15_pd['descripcion']=='ANTIPASTI DE LA CASA'].index)
sin_com_notas=sin_antipasti_notas.drop(sin_antipasti_notas[sin_antipasti_notas['descripcion']=='COM'].index)
sin_comr_notas=sin_com_notas.drop(sin_com_notas[sin_com_notas['descripcion']=='COMBO R'].index)
sin_pesto_notas=sin_comr_notas.drop(sin_comr_notas[sin_comr_notas['descripcion']=='PESTO SSA'].index)
sin_segundo_notas=sin_pesto_notas.drop(sin_pesto_notas[sin_pesto_notas['descripcion']=='SEGUNDO TIEMPO'].index)
limpieza_tercer=sin_segundo_notas.drop(sin_segundo_notas[sin_segundo_notas['descripcion']=='TERCER TIEMPO'].index)
limpieza_notas_sin_2015=limpieza_tercer.drop(limpieza_tercer[limpieza_tercer['anio_vendido']==2015.0].index)
limpieza_notas_df=limpieza_notas_sin_2015.drop(limpieza_notas_sin_2015[limpieza_notas_sin_2015['anio_vendido']==2020.0].index)
limpieza_notas_df_pivote_cantidad_mesa=limpieza_notas_df.pivot_table(columns=['mesa'],index=['descripcion','grupplat'],values=['cantidad'],aggfunc='sum',fill_value=0)
limpieza_notas_df_pivote_cantidad_mesa.columns=[''.join(x).replace('cantidad','cant_') for x in limpieza_notas_df_pivote_cantidad_mesa.columns]
limpieza_notas_df_pivote_cantidad_dia=limpieza_notas_df.pivot_table(columns=['dia_semana'],index=['descripcion','grupplat'],values=['cantidad'],aggfunc='sum',fill_value=0)
limpieza_notas_df_pivote_cantidad_dia.columns=[''.join(x).replace('cantidad','cant_') for x in limpieza_notas_df_pivote_cantidad_dia.columns]
limpieza_notas_df_pivote_cantidad_dia.reset_index(inplace=True)
limpieza_notas_df_pivote_cantidad_anio=limpieza_notas_df.pivot_table(columns=['anio_vendido'],index=['descripcion','grupplat'],values=['cantidad'],aggfunc='sum',fill_value=0)
limpieza_notas_df_pivote_cantidad_anio.columns=[''.join(str(x).replace('cantidad','cant_').replace('"','').replace("'",'').replace(',','').replace('(','').replace(')','')) for x in limpieza_notas_df_pivote_cantidad_anio.columns]
limpieza_notas_df_pivote_cantidad_anio.reset_index(inplace=True)
limpieza_notas_df_pivote_utilidad_mesa=limpieza_notas_df.pivot_table(columns=['mesa'],index=['descripcion','grupplat'],values=['utilidad'],aggfunc='sum',fill_value=0)
limpieza_notas_df_pivote_utilidad_mesa.columns=[''.join(x).replace('utilidad','util_') for x in limpieza_notas_df_pivote_utilidad_mesa.columns]
limpieza_notas_df_pivote_utilidad_mesa.reset_index(inplace=True)
limpieza_notas_df_pivote_utilidad_dia=limpieza_notas_df.pivot_table(columns=['dia_semana'],index=['descripcion','grupplat'],values=['utilidad'],aggfunc='sum',fill_value=0)
limpieza_notas_df_pivote_utilidad_dia.columns=[''.join(x).replace('utilidad','util_') for x in limpieza_notas_df_pivote_utilidad_dia.columns]
limpieza_notas_df_pivote_utilidad_dia.reset_index(inplace=True)
limpieza_notas_df_pivote_utilidad_anio=limpieza_notas_df.pivot_table(columns=['anio_vendido'],index=['descripcion','grupplat'],values=['utilidad'],aggfunc='sum',fill_value=0)
limpieza_notas_df_pivote_utilidad_anio.columns=[''.join(str(x).replace('utilidad','util_').replace('"','').replace("'",'').replace(',','').replace('(','').replace(')','')) for x in limpieza_notas_df_pivote_utilidad_anio.columns]
limpieza_notas_df_pivote_utilidad_anio.reset_index(inplace=True)
lista_df=[limpieza_notas_df_pivote_cantidad_mesa,limpieza_notas_df_pivote_cantidad_dia,limpieza_notas_df_pivote_cantidad_anio,limpieza_notas_df_pivote_utilidad_mesa,limpieza_notas_df_pivote_utilidad_dia,limpieza_notas_df_pivote_utilidad_anio]
limpieza_cluster_df=reduce(lambda x,y: pd.merge(x,y,on=['descripcion','grupplat']),lista_df)
pd.options.mode.chained_assignment = None
limpieza_cluster_df['categoria']='Sin Categoria'
grupplat_alimentos=['A11','A12','A13','A14','A15','A16','A17','A18','A19','A21','A22','A23','A7','AS',
                    'A101','A102','A111','A112','A24','A4','A81','A82','A83','O1']
for x in grupplat_alimentos:
    limpieza_cluster_df["categoria"][(limpieza_cluster_df['grupplat'] == x)] = "alimentos"

grupplat_alcohol=['B1','B10','B11','B12','B14','B15','B17','B18','B2','B3','B5','B6','B7','B8','B9','B191']
for x in grupplat_alcohol:
    limpieza_cluster_df["categoria"][(limpieza_cluster_df['grupplat'] == x)] = "alcohol"

grupplat_vinos=['V1','V11','V14','V17','V18','V2','V29','V3','V6','V7','V4']    
for x in grupplat_vinos:
    limpieza_cluster_df["categoria"][(limpieza_cluster_df['grupplat'] == x)] = "vinos"

limpieza_cluster_df["categoria"][(limpieza_cluster_df['grupplat']== 'B13')]= "bebidas_no_alcoholicas"
limpieza_cluster_df["categoria"][(limpieza_cluster_df['grupplat']== 'A20')]= "postres"
limpieza_cluster_df["categoria"][(limpieza_cluster_df['grupplat']== 'B16')]= "cafe"
limpieza_cluster_2=limpieza_cluster_df[['categoria','descripcion','util_Monday','util_Tuesday','util_Wednesday','util_Thursday','util_Friday','util_Saturday','util_Sunday','util_ 2019.0']]
auxut=limpieza_cluster_2.set_index(['descripcion','categoria'])
mm = MinMaxScaler()
aux2 = pd.DataFrame(mm.fit_transform(auxut), columns= auxut.columns)
pca = PCA(n_components=2)
aux_pcaut = pd.DataFrame(pca.fit_transform(aux2), columns=["p1","p2"])
pca.explained_variance_ratio_.cumsum()
inercias = []
for i in range(1,10):
    cl = KMeans(n_clusters=i)
    cl.fit(aux2) #entrenamos con los escalados
    inercias.append(cl.inertia_)
cl = KMeans(n_clusters=3)
cl.fit(aux2)
auxut["cl"]= aux_pcaut["cl"] = aux2["cl"] = cl.predict(aux2)
datos_cluster_ut=aux2.groupby("cl").mean()
(aux2.groupby('cl').mean())*100
auxut['utilidad_total']=auxut[['util_ 2019.0']].sum(axis=1)
tabla_clusters=auxut    
tabla_clusters['clusters']=None
# print("Ingresa el nivel de rentabilidad del cluster 0")
# cluster_0=input()
# print("Ingresa el nivel de rentabilidad del cluster 1")
# cluster_1=input()
# print("Ingresa el nivel de rentabilidad del cluster 2")
# cluster_2=input()
tabla_clusters["clusters"][(tabla_clusters['cl']== 0)]= f"Cluster Alta Rentabilidad"
tabla_clusters["clusters"][(tabla_clusters['cl']== 1)]= f"Cluster Media Rentabilidad"
tabla_clusters["clusters"][(tabla_clusters['cl']== 2)]= f"Cluster Baja Rentabilidad"
tabla_clusters.reset_index(inplace=True)
tabla_clusters_bubbles=tabla_clusters[['descripcion','categoria','utilidad_total','clusters']]
tabla_mayor_rentabilidad=tabla_clusters_bubbles[tabla_clusters_bubbles['clusters']=='Cluster Alta Rentabilidad']
tabla_media_rentabilidad=tabla_clusters_bubbles[tabla_clusters_bubbles['clusters']=='Cluster Media Rentabilidad']
tabla_baja_rentabilidad=tabla_clusters_bubbles[tabla_clusters_bubbles['clusters']=='Cluster Baja Rentabilidad']
tabla_baja_rentabilidad['ranking'] = tabla_baja_rentabilidad['utilidad_total'].rank(method='max')
tabla_baja_rentabilidad=tabla_baja_rentabilidad.sort_values('ranking').tail(15)
# print(tabla_mayor_rentabilidad)
end=time.time()
print(end-start)

# platillo=platillo.lower()
# platillo=platillo.replace(" ","_")
# tabla_mayor_rentabilidad.to_sql(f'cluster_mayor_{platillo}', engine,if_exists='replace')
# tabla_media_rentabilidad.to_sql(f'cluster_media_{platillo}', engine,if_exists='replace')
# tabla_baja_rentabilidad.to_sql(f'cluster_baja_{platillo}', engine,if_exists='replace')

end=time.time()




