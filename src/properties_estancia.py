class PropertiesEstancia(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesEstancia.__instance is None:
            PropertiesEstancia.__instance = self
        if yaml is not None:
            PropertiesEstancia.__properties = yaml
    
    @property
    def QUERY_ESTANCIA(self):
        return self.__properties['query_estancia']