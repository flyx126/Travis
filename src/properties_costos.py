class PropertiesCostos(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesCostos.__instance is None:
            PropertiesCostos.__instance = self
        if yaml is not None:
            PropertiesCostos.__properties = yaml

    @property
    def QUERY_COSTOS(self):
        return self.__properties['query_costo']
    
    @property
    def QUERY_COSTOS_INVENTARIO(self):
        return self.__properties['query_costos_inventario']
    



    
    
    
    
    
    
    
    
    