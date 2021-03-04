class PropertiesTendencia(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesTendencia.__instance is None:
            PropertiesTendencia.__instance = self
        if yaml is not None:
            PropertiesTendencia.__properties = yaml
    
    @property
    def QUERY_TENDENCIA(self):
        return self.__properties['query_tendencia']