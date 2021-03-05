import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.log import log
from src.customException import BadRequest
from src.properties_db import PropertiesDb
import yaml

class Db(object):

    __session = None
    __instance = None

    def __new__(self):
        if not self.__instance:
            self.__instance = object.__new__(self)
        return self.__instance
    
    def get_session(self):
        if self.__session is None:
            self.create_session()
        return self.__session
         
    def create_session(self):
        os.environ['PATH_CONFIG']='./config/Dashboard_dev.yaml'
        with open(os.environ['PATH_CONFIG']) as file:
            yml=yaml.load(file, Loader=yaml.FullLoader)
        properties=PropertiesDb(yml['db'])
        connection_string = f'{properties.USER}:{properties.PASSWORD}@postgres:{properties.PORT}/{properties.DATABASE}'
        try:
            engine = create_engine(f'postgresql://{connection_string}')
            engine.connect()
            log.info("Conexion exitosa")
            return engine
        except Exception as ex:
            log.info(ex)



        

