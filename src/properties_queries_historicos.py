class PropertiesQueriesHistorico(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesQueriesHistorico.__instance is None:
            PropertiesQueriesHistorico.__instance = self
        if yaml is not None:
            PropertiesQueriesHistorico.__properties = yaml

    @property
    def QUERY_MESERO_HISTORICO(self):
        return self.__properties['query_mesero_historico']
    @property    
    def QUERY_PRODUCTOS_MAS_VENDIDO_HISTORICO(self):
        return self.__properties['query_producto_mas_vendido_historico']
    @property    
    def QUERY_UTILIDAD_POR_HORA_HISTORICO(self):
        return self.__properties['query_utilidad_por_hora_historico']
    @property    
    def QUERY_COSTO_POR_HORA_HISTORICO(self):
        return self.__properties['query_costo_por_hora_historico']
    @property
    def QUERY_VENTA_POR_HORA_HISTORICO(self):
        return self.__properties['query_venta_por_hora_historico']
    @property
    def QUERY_MONTO_VOLUMEN_HISTORICO(self):
        return self.__properties['query_monto_volumen_historico']
    @property
    def QUERY_PERSONAS(self):
        return self.__properties['query_personas_historico']









    
    @property
    def QUERY_FUNCION_CONSULTA(self):
        return self.__properties['query_funcion_consulta']
    
    @property
    def QUERY_FUNCION_CONSULTA_2(self):
        return self.__properties['query_funcion_consulta_2']
    
    @property
    def QUERY_ARTICULOS_MAS_VENDIDOS(self):
        return self.__properties['query_articulos_mas_vendidos']
       
    @property
    def QUERY_VALORES_ACUMULADOS(self):
        return self.__properties['query_valores_acumulados']
       
    @property
    def QUERY_VALORES_HORA(self):
        return self.__properties['query_valores_hora']
       
    @property
    def QUERY_VOLUMEN_VENTA_HORA(self):
        return self.__properties['query_volumen_venta_hora']
       
    @property
    def QUERY_TOTAL_PERSONAS_DIA(self):
        return self.__properties['query_total_personas_dia']
    
    @property
    def QUERY_TOTAL_PERSONAS_DIA_2(self):
        return self.__properties['query_total_personas_dia_2']
       
    @property
    def QUERY_VOLUMEN_VENTA_GRUPPLAT_MESERO(self):
        return self.__properties['query_volumen_venta_grupplat_mesero']
       
    @property
    def QUERY_MONTO_VENTA_GRUPPLAT_MESERO(self):
        return self.__properties['query_monto_venta_grupplat_mesero']
       
    @property
    def QUERY_DESCUENTO(self):
        return self.__properties['query_descuento']
       
    
    
    
    
    
    
    
    
    