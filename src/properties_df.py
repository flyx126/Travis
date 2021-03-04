class PropertiesDf(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesDf.__instance is None:
            PropertiesDf.__instance = self
        if yaml is not None:
            PropertiesDf.__properties = yaml

    
    @property
    def DF_COLUMNA_PLATILLO(self):
        return self.__properties['df_columna_platillos'] 
    
    @property
    def DF_COLUMNA_PRECIO(self):
        return self.__properties['df_columna_precios']
    
    @property
    def DF_COLUMNA_CANTIDAD(self):
        return self.__properties['df_columna_cantidad']
    
    @property
    def DF_COLUMNA_FECHA(self):
        return self.__properties['df_columna_fecha']
    
    @property
    def DF_COLUMNA_MESERO(self):
        return self.__properties['df_columna_mesero']
    
    @property
    def DF_COLUMNA_HORA(self):
        return self.__properties['df_columna_hora']

    @property
    def DF_COLUMNA_MESA(self):
        return self.__properties['df_columna_mesa']
    
    @property
    def DF_COLUMNA_NOTVEN(self):
        return self.__properties['df_columna_notven']
    
    @property
    def DF_COLUMNA_PERS(self):
        return self.__properties['df_columna_pers']
    
    @property
    def DF_COLUMNA_PRECIO(self):
        return self.__properties['df_columna_precio']
    
    @property
    def DF_COLUMNA_GRUPPLAT(self):
        return self.__properties['df_columna_grupplat']
    
    @property
    def DF_COLUMNA_PARTIDA(self):
        return self.__properties['df_columna_partida']

    @property
    def DF_COLUMNA_DESCUENTO(self):
        return self.__properties['df_columna_descuento']

    @property
    def DF_COLUMNA_CLAVE(self):
        return self.__properties['df_columna_clave']

    @property
    def DF_COLUMNA_DESCR(self):
        return self.__properties['df_columna_descr']
    
    @property
    def DF_COLUMNA_COSTO(self):
        return self.__properties['df_columna_costo']
    
    @property
    def DF_COLUMNA_UNIDAD(self):
        return self.__properties['df_columna_unidad']