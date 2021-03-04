class PropertiesDemanda(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesDemanda.__instance is None:
            PropertiesDemanda.__instance = self
        if yaml is not None:
            PropertiesDemanda.__properties = yaml
    
    @property
    def QUERY_DISTRIBUCION(self):
        return self.__properties['query_distribucion']
    
