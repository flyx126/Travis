class PropertiesGenerales(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesGenerales.__instance is None:
            PropertiesGenerales.__instance = self
        if yaml is not None:
            PropertiesGenerales.__properties = yaml
    
    @property
    def RUTA_NOTVEN(self):
        return self.__properties['ruta_notven']
    
    @property
    def RUTA_INVENTARIO(self):
        return self.__properties['ruta_inventario']

    @property
    def RUTA_CAT_MESEROS(self):
        return self.__properties['ruta_cat_meseros']

    @property
    def CARACTERES_ESPECIALES(self):
        return self.__properties['caracteres_especiales']
    
    @property
    def SELECCION_COLUMNAS_INVENTARIO(self):
        return self.__properties['seleccion_columnas_inventario']
        
    @property
    def SELECCION_COLUMNAS_NOTVEN(self):
        return self.__properties['seleccion_columnas_notven']
    
