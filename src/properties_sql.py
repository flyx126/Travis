class PropertiesSQL(object):

    __instance = None
    __properties = None

    def __init__(self, yaml = None):
        if PropertiesSQL.__instance is None:
            PropertiesSQL.__instance = self
        if yaml is not None:
            PropertiesSQL.__properties = yaml

    @property
    def SQL_COLUMNA_ID(self):
        return self.__properties['sql_columna_id']

    @property
    def SQL_COLUMNA_CLAVE(self):
        return self.__properties['sql_columna_clave']
    
    @property
    def SQL_COLUMNA_PRECIO(self):
        return self.__properties['sql_columna_precio']
    
    @property
    def SQL_COLUMNA_CANTIDAD(self):
        return self.__properties['sql_columna_cantidad']
    
    @property
    def SQL_COLUMNA_FECHA(self):
        return self.__properties['sql_columna_fecha']

    @property
    def SQL_COLUMNA_MESERO(self):
        return self.__properties['sql_columna_mesero']
    
    @property
    def SQL_COLUMNA_HORA(self):
        return self.__properties['sql_columna_hora']
    
    @property
    def SQL_COLUMNA_MESA(self):
        return self.__properties['sql_columna_mesa']

    @property
    def SQL_COLUMNA_NOTVEN(self):
        return self.__properties['sql_columna_notven']
    
    @property
    def SQL_COLUMNA_PERS(self):
        return self.__properties['sql_columna_pers']
    
    @property
    def SQL_COLUMNA_GRUPPLAT(self):
        return self.__properties['sql_columna_grupplat']
    
    @property
    def SQL_COLUMNA_PARTIDA(self):
        return self.__properties['sql_columna_partida']
    
    @property
    def SQL_COLUMNA_DESCUENTO(self):
        return self.__properties['sql_columna_descuento']
    
    @property
    def SQL_COLUMNA_DESCR(self):
        return self.__properties['sql_columna_descr']
    
    @property
    def SQL_COLUMNA_ID_2(self):
        return self.__properties['sql_columna_id']
    
    @property
    def SQL_COLUMNA_COSTO(self):
        return self.__properties['sql_columna_costo']
    
    @property
    def SQL_COLUMNA_UNIDAD(self):
        return self.__properties['sql_columna_unidad']
    
    @property
    def SQL_COLUMNA_DIA_VENDIDO(self):
        return self.__properties['sql_columna_dia_vendido']
    
    @property
    def SQL_COLUMNA_MES_VENDIDO(self):
        return self.__properties['sql_columna_mes_vendido']
    
    @property
    def SQL_COLUMNA_ANIO_VENDIDO(self):
        return self.__properties['sql_columna_anio_vendido']
    
    @property
    def SQL_COLUMNA_UTILIDAD(self):
        return self.__properties['sql_columna_utilidad']
    
    @property
    def SQL_COLUMNA_HORA_VENDIDO(self):
        return self.__properties['sql_columna_hora_vendido']
    
    @property
    def SQL_COLUMNA_NOMBRE_MESERO(self):
        return self.__properties['sql_columna_nombre_mesero']