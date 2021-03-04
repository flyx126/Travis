import pytest 
from app import service_objetos 
import datetime
from app.log import log

def test_ultima_fecha(mocker):
    mock_response_dao='2020-03-20'
    
    mocker.patch('app.service_objetos.dao.ultima_fecha',return_value=mock_response_dao)
    
    response_fecha=service_objetos.ultima_fecha("fecha")
  
    assert response_fecha=='2020-03-20'

def test_producto_mas_vendido_query(mocker):
    mock_response_dao=[{'nombre': 'I FORMAGGI', 'grupo_platillo': 'A11', 'fecha': datetime.date(2020, 3, 20), 
    'cantidad_platillos': 2.0, 'cantidad_bebidas': None, 'cantidad_vinos': None}, {'nombre': 'GINGER TOSCALIA', 
    'grupo_platillo': 'B13', 'fecha': datetime.date(2020, 3, 20), 'cantidad_platillos': None, 
    'cantidad_bebidas': 3.0, 'cantidad_vinos': None}, {'nombre': 'CASA MADERO 750ML', 'grupo_platillo': 'V7', 
    'fecha': datetime.date(2020, 3, 20), 'cantidad_platillos': None, 'cantidad_bebidas': None, 
    'cantidad_vinos': 2.0}]

    mocker.patch('app.service_objetos.dao.query_producto_mas_vendido',return_value=mock_response_dao)

    response_lista_bebidas,response_lista_platillos,response_lista_vinos=service_objetos.producto_mas_vendido_query("2020-03-20")
    
    assert len(response_lista_bebidas)==1
    assert response_lista_bebidas[0]['nombre']=='GINGER TOSCALIA'

    assert len(response_lista_platillos)==1
    assert response_lista_platillos[0]['fecha']=="2020-03-20"

    assert len(response_lista_vinos)==1
    assert response_lista_vinos[0]['cantidad_vinos']==2.0

def test_utilidad_por_hora_query(mocker):
    mock_response_dao=[{'hora_vendido': 14.0, 'utilidad_total': 717.003320987953, 'utilidad_platillos': 347.126359529129, 
    'utilidad_bebidas': 75.394297458824, 'utilidad_vinos': 294.482664}]

    mocker.patch('app.service_objetos.dao.query_utilidad_por_hora',return_value=mock_response_dao)

    response_lista_utilidad_por_hora=service_objetos.utilidad_por_hora_query("2020-03-20")

    assert response_lista_utilidad_por_hora[0]['hora']==14.0
    assert response_lista_utilidad_por_hora[0]['utilidad']==717.003320987953
    assert response_lista_utilidad_por_hora[0]['utilidad_bebidas_hora']==75.394297458824
    assert response_lista_utilidad_por_hora[0]['utilidad_platillos_hora']==347.126359529129
    assert response_lista_utilidad_por_hora[0]['utilidad_vinos_hora']==294.482664

def test_costo_por_hora_query(mocker):
    mock_response_dao=[{'hora_vendido': 14.0, 'costo_total': 455.63684701204704, 'costo_platillos': 94.713640470871, 
    'costo_bebidas': 25.405702541175998, 'costo_vinos': 335.51750400000003}]

    mocker.patch('app.service_objetos.dao.query_costo_por_hora',return_value=mock_response_dao)

    response_lista_costo_por_hora=service_objetos.costo_por_hora_query("2020-03-20")

    assert response_lista_costo_por_hora[0]['hora']==14.0
    assert response_lista_costo_por_hora[0]['costo']==455.63684701204704
    assert response_lista_costo_por_hora[0]['costo_bebidas_hora']==25.405702541175998
    assert response_lista_costo_por_hora[0]['costo_platillos_hora']==94.713640470871
    assert response_lista_costo_por_hora[0]['costo_vinos_hora']==335.51750400000003

def test_venta_por_hora_query(mocker):
    mock_response_dao=[{'hora': 14.0, 'dinero': 668.6401679999999, 'volumen_venta': 9.2, 'volumen_venta_platillos_hora': 4.0, 
    'volumen_venta_bebidas_hora': 3.0, 'volumen_venta_vinos_hora': 2.2}]

    mocker.patch('app.service_objetos.dao.query_venta_por_hora',return_value=mock_response_dao)

    response_lista_venta_por_hora=service_objetos.venta_por_hora_query("2020-03-20")

    assert response_lista_venta_por_hora[0]['hora']==14.0
    assert response_lista_venta_por_hora[0]['dinero']==668.6401679999999
    assert response_lista_venta_por_hora[0]['volumen_venta']==9.2
    assert response_lista_venta_por_hora[0]['volumen_venta_bebidas_hora']==3.0
    assert response_lista_venta_por_hora[0]['volumen_venta_platillos_hora']==4.0
    assert response_lista_venta_por_hora[0]['volumen_venta_vinos_hora']==2.2

def test_mesero_query(mocker):
    mock_response_dao=[{'nombre': 'IVAN ROBLES', 'utilidad': 1834.20676454159, 'venta': 3092.0400839999998, 
    'fecha': datetime.date(2020, 3, 20), 'volumen_platillos': 7.0, 'monto_platillos': 997.0800839999999, 
    'volumen_bebidas': 12.0, 'monto_bebidas': 918.9599999999999, 'volumen_vinos': 2.0, 'monto_vinos': 1176.0}]

    mocker.patch('app.service_objetos.dao.query_mesero',return_value=mock_response_dao)

    response_lista_mesero=service_objetos.mesero_query('2020-03-20')

    assert response_lista_mesero[0]['nombre']=='IVAN ROBLES'
    assert response_lista_mesero[0]['utilidad']==1834.20676454159
    assert response_lista_mesero[0]['venta']==3092.0400839999998
    assert response_lista_mesero[0]['monto_bebidas']==918.9599999999999
    assert response_lista_mesero[0]['volumen_platillos']==7.0
    assert response_lista_mesero[0]['monto_vinos']==1176.0

def test_monto_volumen(mocker):
    mock_response_dao=[{'volumen': 118.2, 'monto': 12835.200167999998}]
    
    mocker.patch('app.service_objetos.dao.query_monto_volumen',return_value=mock_response_dao)

    response_lista_valores=service_objetos.monto_volumen('2020-03-20')

    assert response_lista_valores[0]['monto']==12835.200167999998
    assert response_lista_valores[0]['volumen']==118.2

def test_return_final_response(mocker):  

    mock_ultima_fecha='2020-03-20'

    mock_producto_mas_vendido_dao=[{'nombre': 'I FORMAGGI', 'grupo_platillo': 'A11', 'fecha': datetime.date(2020, 3, 20), 
    'cantidad_platillos': 2.0, 'cantidad_bebidas': None, 'cantidad_vinos': None}, {'nombre': 'GINGER TOSCALIA', 
    'grupo_platillo': 'B13', 'fecha': datetime.date(2020, 3, 20), 'cantidad_platillos': None, 
    'cantidad_bebidas': 3.0, 'cantidad_vinos': None}, {'nombre': 'CASA MADERO 750ML', 'grupo_platillo': 'V7', 
    'fecha': datetime.date(2020, 3, 20), 'cantidad_platillos': None, 'cantidad_bebidas': None, 
    'cantidad_vinos': 2.0}]

    mock_utilidad_por_hora_dao=[{'hora_vendido': 14.0, 'utilidad_total': 717.003320987953, 'utilidad_platillos': 347.126359529129, 
    'utilidad_bebidas': 75.394297458824, 'utilidad_vinos': 294.482664}]

    mock_costo_por_hora_dao=[{'hora_vendido': 14.0, 'costo_total': 455.63684701204704, 'costo_platillos': 94.713640470871, 
    'costo_bebidas': 25.405702541175998, 'costo_vinos': 335.51750400000003}]

    mock_venta_por_hora_dao=[{'hora': 14.0, 'dinero': 668.6401679999999, 'volumen_venta': 9.2, 'volumen_venta_platillos_hora': 4.0, 
    'volumen_venta_bebidas_hora': 3.0, 'volumen_venta_vinos_hora': 2.2}]

    mock_mesero_dao=[{'nombre': 'IVAN ROBLES', 'utilidad': 1834.20676454159, 'venta': 3092.0400839999998, 
    'fecha': datetime.date(2020, 3, 20), 'volumen_platillos': 7.0, 'monto_platillos': 997.0800839999999, 
    'volumen_bebidas': 12.0, 'monto_bebidas': 918.9599999999999, 'volumen_vinos': 2.0, 'monto_vinos': 1176.0}]

    mock_monto_volumen_dao=[{'volumen': 118.2, 'monto': 12835.200167999998}]   

    mocker.patch('app.service_objetos.dao.ultima_fecha', return_value=mock_ultima_fecha)

    mocker.patch('app.service_objetos.dao.query_producto_mas_vendido',return_value=mock_producto_mas_vendido_dao) 

    mocker.patch('app.service_objetos.dao.query_utilidad_por_hora',return_value=mock_utilidad_por_hora_dao)

    mocker.patch('app.service_objetos.dao.query_costo_por_hora',return_value=mock_costo_por_hora_dao)

    mocker.patch('app.service_objetos.dao.query_venta_por_hora',return_value=mock_venta_por_hora_dao)

    mocker.patch('app.service_objetos.dao.query_mesero',return_value=mock_mesero_dao)

    mocker.patch('app.service_objetos.dao.query_monto_volumen',return_value=mock_monto_volumen_dao)

    response=service_objetos.return_final_response()

    assert len(response.producto_mas_vendido_bebidas)==1
    assert response.producto_mas_vendido_platillos[0]['grupo_platillo']=='A11'
    assert response.utilidad_por_hora[0]['utilidad']==717.003320987953
    assert response.costo_por_hora[0]['costo_vinos_hora']==335.51750400000003
    assert response.venta_por_hora[0]['dinero']==668.6401679999999
    assert response.mesero[0]['monto_platillos']==997.0800839999999
    assert response.monto_volumen[0]['volumen']==118.2

