from src.customException import BadRequest 
from flask import Blueprint, jsonify
from src.log import log


errors = Blueprint('errors', __name__)

def create_body_error(error_type, code, description, location):
    error_response = {
        "type": error_type,
        "code": code, 
        "description": description,
        "location": location
    }
    log.error("%s",description)
    return jsonify(error_response)

@errors.app_errorhandler(404)
def handle_error(error):
    return create_body_error("ERROR", 404, error.description, "URL"), 404
    #return create_body_error("ERROR", 404, error.description, "Base de datos"), 404
    #return render_template('pages/404.html')

@errors.app_errorhandler(400)
def handle_error_bad_request(error):
    return create_body_error("ERROR", 400, error.description, "Bad Request"), 400
    #return render_template('pages/400.html')

@errors.app_errorhandler(500)
def handle_error_internal_error(error):
    return create_body_error("ERROR", 500, error.description, "Internal Server Error"),500
    #return render_template('pages/500.html')


@errors.app_errorhandler(502)
def handle_error_bad_gateway(error):
    return create_body_error("ERROR", 502, error.description, "Bad Gateway"),502
    #return render_template('pages/502.html')

@errors.app_errorhandler(504)
def handle_error_gateway_timeout(error):
    return create_body_error("ERROR", 504, error.description, "Gateway Timeout"),504
    #return render_template('pages/504.html')

@errors.app_errorhandler(BadRequest)
def handle_error_custom_exception(error):
    print(error)
    return create_body_error("ERROR", error.status, error.description, "Bad Request"), error.status