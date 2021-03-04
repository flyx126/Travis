import datetime
from src.customException import BadRequest
from src.log import log
from datetime import date

def validar_fecha(fecha):
    try:
        log.info(fecha)
        date=fecha.split("-")
        log.info(date)
        if len(date[0])== 4 and len(date[1])==2 and len(date[2])==2:
            log.info("Cumplio con validaciones")
            datetime.datetime.strptime(fecha,'%Y-%m-%d')
        else:
            log.info("Fallo en longitud de fecha, o fallo en formato de fecha")
            raise BadRequest("Error en longitud de la fecha","formato de fecha","Error",400)
    except (ValueError, IndexError):
        log.info("Error en el formato de la fecha")
        raise BadRequest("Error en el formato de la fecha","formato de fecha","Error",400)

