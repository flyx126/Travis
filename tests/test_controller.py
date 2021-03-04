import pytest 
from app import controller 
import datetime
from app.log import log 
import json

class Response:
    def __init__(self, **kwargs):
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

def test_index(mocker):
    mock_dictionary_index={"producto_mas_vendido_bebidas": [{"fecha": "2020-03-20", "nombre": "NARANJADA", "cantidad_platillos": 0,
    "cantidad_bebidas": 6.0, "cantidad_vinos": 0, "grupo_platillo": "B13"}], "producto_mas_vendido_platillos": [{"fecha": "2020-03-20", "nombre": "I FORMAGGI",
    "cantidad_platillos": 2.0, "cantidad_bebidas": 0, "cantidad_vinos": 0, "grupo_platillo": "A11"}], "producto_mas_vendido_vinos": [{"fecha":
    "2020-03-20", "nombre": "CASA MADERO 750ML", "cantidad_platillos": 0, "cantidad_bebidas": 0, "cantidad_vinos": 2.0,
    "grupo_platillo": "V7"}], "utilidad_por_hora": [{"utilidad": 1292.889658872531, "hora": 19.0, "utilidad_bebidas_hora": 452.9315761296559, "utilidad_platillos_hora":
    231.18413274287497, "utilidad_vinos_hora": 608.77395}], "costo_por_hora":
    [{"costo": 1095.230341127469, "hora": 19.0, "costo_bebidas_hora": 450.06842387034396,
    "costo_platillos_hora": 77.935867257125, "costo_vinos_hora": 567.22605}], "venta_por_hora": [{"dinero":
    2388.12, "hora": 19.0, "volumen_venta": 14.0, "volumen_venta_bebidas_hora": 10.0, "volumen_venta_platillos_hora": 2.0,
    "volumen_venta_vinos_hora": 2.0}], "mesero": [{"nombre": "IVAN ROBLES", "monto_bebidas": 918.9599999999998, "monto_platillos": 997.0800839999999, "monto_vinos":
    1176.0, "volumen_platillos": 7.0, "volumen_bebidas": 12.0, "volumen_vinos": 2.0, "utilidad": 1834.20676454159, "venta":
    3092.040084}], "monto_volumen": [{"monto": 10153.500004788, "volumen": 89.5}]}

    mock_dictionary_index_json=Response(producto_mas_vendido_bebidas=mock_dictionary_index['producto_mas_vendido_bebidas'],producto_mas_vendido_platillos=mock_dictionary_index['producto_mas_vendido_platillos'],\
        producto_mas_vendido_vinos=mock_dictionary_index['producto_mas_vendido_vinos'],utilidad_por_hora=mock_dictionary_index['utilidad_por_hora'],costo_por_hora=mock_dictionary_index['costo_por_hora'],venta_por_hora=mock_dictionary_index['venta_por_hora'],\
            mesero=mock_dictionary_index['mesero'],monto_volumen=mock_dictionary_index['monto_volumen'])

    mock_dictionary_index_json_1=json.dumps(mock_dictionary_index_json.__dict__)
    
     
    mocker.patch('app.controller.srv.return_final_response',return_value=mock_dictionary_index_json)

    response_final_response=controller.home()

    assert response_final_response == mock_dictionary_index_json_1


