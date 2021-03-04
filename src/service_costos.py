from src.modelos import GrupoPlatillo
from src import dao_costos as dao
from datetime import datetime
from src.log import log
import numpy as np
import pandas as pd


def costos(fecha_menor,fecha_mayor):
    log.info("Consulta Service Costos")

    consulta=dao.query_costos(fecha_menor,fecha_mayor)
    consulta_costos=dao.query_costos_inventario()   
    
    tbl_maestra=pd.DataFrame(consulta,columns=["FECHA","DESCR","PRECIO","GRUPPLAT","MES_VENDIDO","ANIO_VENDIDO","COSTO_MAESTRA","UNIDAD"])
    costos_IN=pd.DataFrame(consulta_costos,columns=['AUXCOSP','DESCR','UNIDAD','GRUPPLAT'])

    costos_total=pd.merge(tbl_maestra,costos_IN,on=['DESCR','UNIDAD','GRUPPLAT'],how='left')
    
    costos_total=costos_total.dropna()

    costos_total.loc[:,'PORCENTAJE_COSTO']=(costos_total['AUXCOSP']/costos_total['PRECIO'])*100

    grupplat=costos_total['GRUPPLAT'].unique().tolist()

    porcentajes_grupplat=[]
    porcentajes_platillos=[]
    for x in grupplat:
        grupos_platillos=costos_total[costos_total['GRUPPLAT']==x]
        porcentaje_grupos_platillos=grupos_platillos['PORCENTAJE_COSTO'].mean()
        porcentajes_grupplat.append([x,porcentaje_grupos_platillos])
        platillos=grupos_platillos['DESCR'].unique().tolist()
        for y in platillos:
            platillos_grupo=grupos_platillos[grupos_platillos['DESCR']==y]
            porcentaje= platillos_grupo['PORCENTAJE_COSTO'].mean()
            porcentajes_platillos.append([x,y,porcentaje])

   
    lista_objeto=list()
    for x in porcentajes_grupplat: 
        lista_plato=[ {'nombre':y[1],'porcentaje':y[2]} for y in porcentajes_platillos if y[0] == x[0]]
        objeto=GrupoPlatillo(grupo=x[0],porcentaje=x[1],platos=lista_plato)
        lista_plato=list()
        lista_objeto.append(objeto.__dict__)
        
    return lista_objeto
            
   
    

    
  
