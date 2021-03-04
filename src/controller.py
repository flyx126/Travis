from flask import Blueprint, Flask, jsonify, request, render_template,json,session, abort,url_for,redirect
import src.service_objetos as srv
import src.service_objetos_historicos as srv_historicos
import src.service_demanda as srv_demanda
import src.service_tendencia as srv_tendencia
import src.service_estancia as srv_estancia
import src.service_usuario as srv_usuario
import src.service_costos as srv_costos
from src.db import Db
from datetime import date
import json
from sqlalchemy.orm import sessionmaker
from src.tabledef import create_engine,User,sessionmaker,engine
from src.log import log

controller_module = Blueprint('controller_module', __name__,url_prefix='/api/v1/indicadores')

@controller_module.route("/index")
def home():
    # if session['logged_in']==True:
    log.info("Consulta API Indicadores Actuales")
    dictionary_index=srv.return_final_response()
    dictionary_index_json=json.dumps(dictionary_index.__dict__)
    log.info("Termina Consulta API Indicadores Actuales")
    return render_template("index.html", index_dictionary=dictionary_index_json)
    # else:
    #     return render_template('errors_login.html')


@controller_module.route("/")
def login():
    return render_template('login.html')


@controller_module.route("/login", methods=['GET','POST'])
def do_admin_login():
    
    if request.method=="POST":
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])

        db=Db()     
        engine = db.create_session()
        # Base = declarative_base()
        Session = sessionmaker(bind=engine)
        s = Session()
        
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
        result = query.first()

        if result:
            session['logged_in'] = True
            # session['nombre']=result.nombre      
            return home()
        else:
            return render_template("errors_users.html")
                
    else:
            return redirect(url_for('controller_module.home'))

@controller_module.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template("login.html")

@controller_module.route("/historicos")
def historicos():
    if session['logged_in'] == True:
        return render_template("index_historicos.html")
    else:
        return "Error"

@controller_module.route("/historicos/historico_dia", methods=["POST"])
def get_fecha():
    log.info("Consulta API Historicos")
    fecha_menor=request.json["fecha_menor"]
    fecha_mayor=request.json["fecha_mayor"]
    dictionary_index=srv_historicos.return_final_response(fecha_menor,fecha_mayor)
    dictionary_index_json=json.dumps(dictionary_index.__dict__)
    log.info("Termina Consulta API Historicos")
    return dictionary_index_json

@controller_module.route("/productos")
def productos():
    if session['logged_in'] == True:
        return render_template("index_productos.html")
    else: "Error"
@controller_module.route("/productos/productos_consulta",methods=["POST"])
def consulta_productos():
    
    log.info("Consulta API Productos")
    fecha_menor=request.json["fecha_menor"]
    fecha_mayor=request.json["fecha_mayor"]
    try:
        dictionary_index=srv_historicos.return_final_response(fecha_menor,fecha_mayor)
        dictionary_index_json=json.dumps(dictionary_index.__dict__)
        log.info("Termina API Productos")
        return dictionary_index_json
    except:
        return json.dumps("Error")

@controller_module.route("/modelos")
def modelos_estadisticos():
    if session['logged_in'] == True:
        return render_template("index_modelos.html")
    else: "Error"
@controller_module.route("/modelos/distribucion_demanda",methods=["POST"])
def distribucion_demada():
    log.info("Consulta API Distribucion Demanda")
    fecha_menor=request.json["fecha_menor"]
    fecha_mayor=request.json["fecha_mayor"]
    try:
        service_response=srv_demanda.distribucion_demanda_mes(fecha_menor,fecha_mayor)
        log.info("Termina Consulta API Distribucion Demanda")
        return json.dumps(service_response.__dict__)
    except:
        return json.dumps("Error")

@controller_module.route("/modelos/tendencia_venta",methods=["POST"])
def tendencia_venta():
    log.info("Consulta API Tendencia Venta")
    grupplat=request.json["grupplat"]
    service_response=srv_tendencia.tendencia_venta(grupplat)
    log.info("Termina Consulta API Tendencia Venta")
    return json.dumps(service_response.__dict__)

@controller_module.route("/modelos/estancia",methods=["POST"])
def estancia():
    log.info("Consulta API Tendencia Venta")
    fecha_menor=request.json["fecha_menor"]
    fecha_mayor=request.json["fecha_mayor"]
    try:
        service_response=srv_estancia.estancia(fecha_menor,fecha_mayor)
        log.info("Termina Consulta API Tendencia Venta")
        return json.dumps(service_response)
    except:
        return json.dumps("Error")

@controller_module.route("/usuarios")
def usuarios():
    if session['logged_in'] == True:
        usuarios=srv_usuario.seleccion_usuario()
        tabla_usuarios=json.dumps(usuarios)
        return render_template("index_usuarios.html",tabla_usuarios=tabla_usuarios)
    else:
        "Error"

@controller_module.route("/usuarios/crear_usuario",methods=["POST"])
def nuevo_usuario():
    nombre=request.json["nombre"]
    apellido=request.json["apellido"]
    username=request.json["username"]
    password=request.json["password"]
    srv_usuario.nuevo_usuario(nombre,apellido,username,password)
    log.info("Consulta API nuevo usario")
    return "Usuario Creado"
    
@controller_module.route("/usuarios/eliminar_usuario",methods=["POST"])
def eliminar_usuario():
    nombre=request.json["nombre"]
    apellido=request.json["apellido"]
    srv_usuario.eliminar_usuario(nombre,apellido)
    log.info("Consulta API eliminar usario")
    return "Usuario Eliminado"

@controller_module.route("/analisis_costos")
def tabla_costos():
    if session['logged_in'] == True:
        return render_template("index_costos.html")
    else:
        "Error"

@controller_module.route("/analisis_costos/costos", methods=["POST"])
def costos():
    log.info("Consulta API Costos")
    fecha_menor=request.json["fecha_menor"]
    fecha_mayor=request.json["fecha_mayor"]
    try:
        service_response=srv_costos.costos(fecha_menor,fecha_mayor)
        log.info("Termina Consulta API Costos")
        return json.dumps(service_response)
    except:
        return json.dumps("Error")


@controller_module.route("/status")
def status():
    return "Response(status=200)"








