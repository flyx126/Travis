from src.properties_db import PropertiesDb
from src.properties_generales import PropertiesGenerales
from src.properties_df import PropertiesDf
from src.properties_sql import PropertiesSQL
from src.properties_queries import PropertiesQueries
from src.properties_queries_historicos import PropertiesQueriesHistorico
from src.properties_demanda import PropertiesDemanda
from src.properties_tendencia import PropertiesTendencia
from src.properties_estancia import PropertiesEstancia
from src.properties_usuario import PropertiesUsuario
from src.properties_costos import PropertiesCostos
from src.db import Db
from src.error_handler import errors
from src.controller import controller_module
from src.log import log
from flask import Flask
import yaml
import secrets
import os 

def create_app():
    app_flask = Flask(__name__)
    secret = secrets.token_urlsafe(32)
    app_flask.secret_key = secret
    app_flask.config.from_object('src.custom_config.DevelopmentConfig')
    # path = src.config['PATH_CONFIG']
    os.environ['PATH_CONFIG']='./config/Dashboard_dev.yaml'
    yml = init_properties(os.environ['PATH_CONFIG'])

    PropertiesDb(yml['db'])
    PropertiesGenerales(yml['generales'])
    PropertiesDf(yml['df'])
    PropertiesSQL(yml['sql'])
    PropertiesQueries(yml['queries'])
    PropertiesQueriesHistorico(yml['queries_historicos'])
    PropertiesDemanda(yml['queries_distribucion_demanda'])
    PropertiesTendencia(yml['queries_tendencia_venta'])
    PropertiesEstancia(yml['queries_estancia'])
    PropertiesUsuario(yml['nuevo_usuario'])
    PropertiesCostos(yml['costos'])
	
    app_flask.register_blueprint(controller_module)
    app_flask.register_blueprint(errors)

    db = Db()
    db.create_session()
    
    log.info("Empieza la aplicacion")
    return app_flask

def init_properties(path_config):
    with open(path_config) as file:
        return yaml.load(file, Loader=yaml.FullLoader)