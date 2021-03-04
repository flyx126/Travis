from src.modelos import TendenciaVenta,TendenciaResponse
from src import dao_queries_tendencia as dao
from datetime import datetime
from src.log import log
import numpy as np
import pandas as pd
import time

def tendencia_venta(grupplat):
    log.info("Consulta Service Tendencia Venta")

    start=time.time()
    platillos_demanda=dao.query_tendencia(grupplat)
    end=time.time()
    print("Query",end-start)

    start=time.time()
    platillos_demanda_pd=pd.DataFrame(platillos_demanda,columns=["descripcion","cantidad","grupplat","año","mes"])
    end=time.time()
    print("DataFrame",end-start)
    
    start=time.time()
    sin_antipasti_demanda=platillos_demanda_pd.drop(platillos_demanda_pd[platillos_demanda_pd['descripcion']=='ANTIPASTI DE LA CASA'].index)
    sin_com_demanda=sin_antipasti_demanda.drop(sin_antipasti_demanda[sin_antipasti_demanda['descripcion']=='COM'].index)
    sin_segundo_demanda=sin_com_demanda.drop(sin_com_demanda[sin_com_demanda['descripcion']=='SEGUNDO TIEMPO'].index)
    limpieza_platillos_demanda=sin_segundo_demanda.drop(sin_segundo_demanda[sin_segundo_demanda['descripcion']=='PESTO SSA'].index)
    grupos_pd_platillos_demanda=limpieza_platillos_demanda['cantidad'].groupby([limpieza_platillos_demanda.año, limpieza_platillos_demanda.mes]).agg('sum').reset_index() 
    grupos_pd_platillos_demanda['target']=grupos_pd_platillos_demanda['cantidad']
    grupos_pd_platillos_demanda['target']=grupos_pd_platillos_demanda.target.shift(-1)
    grupos_pd_platillos_demanda.dropna(inplace=True)
    end=time.time()
    print("Limpieza DataFrame",end-start)

    start=time.time()
    res_2016=grupos_pd_platillos_demanda['año']==2016.0
    res_2017=grupos_pd_platillos_demanda['año']==2017.0
    res_2018=grupos_pd_platillos_demanda['año']==2018.0
    res_2019=grupos_pd_platillos_demanda['año']==2019.0
    res_2020=grupos_pd_platillos_demanda['año']==2020.0
    end=time.time()
    print("Grupos por Año",end-start)

    start=time.time()
    venta_platillos_2016=grupos_pd_platillos_demanda[res_2016].reset_index()
    venta_platillos_2017=grupos_pd_platillos_demanda[res_2017].reset_index()
    venta_platillos_2018=grupos_pd_platillos_demanda[res_2018].reset_index()
    venta_platillos_2019=grupos_pd_platillos_demanda[res_2019].reset_index()
    venta_platillos_2020=grupos_pd_platillos_demanda[res_2020].reset_index()
    end=time.time()
    print("Reset Index",end-start)

    start=time.time()
    venta_platillos_2016=venta_platillos_2016.drop(columns='index')
    venta_platillos_2017=venta_platillos_2017.drop(columns='index')
    venta_platillos_2018=venta_platillos_2018.drop(columns='index')
    venta_platillos_2019=venta_platillos_2019.drop(columns='index')
    venta_platillos_2020=venta_platillos_2020.drop(columns='index')
    end=time.time()
    print("Drop Index",end-start)

    start=time.time()
    tendencia_2016=TendenciaVenta(mes=venta_platillos_2016['mes'].tolist(),cantidad=venta_platillos_2016['cantidad'].tolist())
    tendencia_2017=TendenciaVenta(mes=venta_platillos_2017['mes'].tolist(),cantidad=venta_platillos_2017['cantidad'].tolist())
    tendencia_2018=TendenciaVenta(mes=venta_platillos_2018['mes'].tolist(),cantidad=venta_platillos_2018['cantidad'].tolist())
    tendencia_2019=TendenciaVenta(mes=venta_platillos_2019['mes'].tolist(),cantidad=venta_platillos_2019['cantidad'].tolist())
    tendencia_2020=TendenciaVenta(mes=venta_platillos_2020['mes'].tolist(),cantidad=venta_platillos_2020['cantidad'].tolist())
    end=time.time()
    print("Crear Objetos",end-start)

    start=time.time()
    tendencia_2016_dict=tendencia_2016.__dict__
    tendencia_2017_dict=tendencia_2017.__dict__
    tendencia_2018_dict=tendencia_2018.__dict__
    tendencia_2019_dict=tendencia_2019.__dict__
    tendencia_2020_dict=tendencia_2020.__dict__
    end=time.time()
    print("Crear Diccionarios de Objetos",end-start)
    
    return TendenciaResponse(venta_platillos_2016=tendencia_2016_dict,venta_platillos_2017=tendencia_2017_dict,\
        venta_platillos_2018=tendencia_2018_dict,venta_platillos_2019=tendencia_2019_dict,venta_platillos_2020=tendencia_2020_dict)