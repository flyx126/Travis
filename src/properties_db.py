class PropertiesDb(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesDb.__instance is None:
            PropertiesDb.__instance = self
        if yaml is not None:
            PropertiesDb.__properties = yaml
    
    @property
    def USER(self):
        return self.__properties['user']
    
    @property
    def PASSWORD(self):
        return self.__properties['password']

    @property
    def PORT(self):
        return self.__properties['port']

    @property
    def DATABASE(self):
        return self.__properties['database']