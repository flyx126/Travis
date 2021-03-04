class PropertiesUsuario(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesUsuario.__instance is None:
            PropertiesUsuario.__instance = self
        if yaml is not None:
            PropertiesUsuario.__properties = yaml

    
    @property
    def NUEVO_USUARIO(self):
        return self.__properties['query_nuevo_usuario'] 
    
    @property
    def ELIMINAR_USUARIO(self):
        return self.__properties['query_eliminar_usuario']
    
    @property
    def SELECCION_USUARIO(self):
        return self.__properties['query_seleccion_usuario']