import pytest 
from app import service_objetos_historicos 
import datetime
from app.log import log 

def test_producto_mas_vendido_historico_query(mocker):
    mock_response_dao=[{'nombre': 'MENU EJECUTIVO 169', 'grupo_platillo': 'A102', 'fecha': datetime.date(2020, 3, 12), 
    'cantidad_platillos': 2.0, 'cantidad_bebidas': 0, 'cantidad_vinos': 0}, {'nombre': 'AMERICANO', 'grupo_platillo': 'B16', 
    'fecha': datetime.date(2020, 3, 10), 'cantidad_platillos': 0, 'cantidad_bebidas': 2.0, 'cantidad_vinos': 0},{'nombre': 'CASA MADERO 750ML', 
    'grupo_platillo': 'V7', 'fecha': datetime.date(2020, 3, 17), 'cantidad_platillos': 0, 'cantidad_bebidas': 0, 'cantidad_vinos': 1.0}]

    mocker.patch('app.service_objetos_historicos.dao.query_producto_mas_vendido_historico',return_value=mock_response_dao)

    response_lista_bebidas,response_lista_platillos,response_lista_vinos=service_objetos_historicos.producto_mas_vendido_query_historico("2020-03-10","2020-03-20")
    
    log.info(response_lista_bebidas)

    assert len(response_lista_bebidas)==1
    assert response_lista_bebidas[0]['nombre']=='AMERICANO'

    assert len(response_lista_platillos)==1
    assert response_lista_platillos[0]['fecha']=="2020-03-12"

    assert len(response_lista_vinos)==1
    assert response_lista_vinos[0]['cantidad_vinos']==1.0

def test_utilidad_por_hora_historico_query(mocker):
    mock_response_dao=[{'hora_vendido': 20.0, 'utilidad_total': 2300.954994876819, 'utilidad_platillos': 1302.997158252635, 
    'utilidad_bebidas': 231.79886162418398, 'utilidad_vinos': 766.1589749999999}]

    mocker.patch('app.service_objetos_historicos.dao.query_utilidad_por_hora_historico',return_value=mock_response_dao)

    response_lista_utilidad_por_hora=service_objetos_historicos.utilidad_por_hora_query_historico("2020-03-10","2020-03-20")

    assert response_lista_utilidad_por_hora[0]['hora']==20.0
    assert response_lista_utilidad_por_hora[0]['utilidad']==2300.954994876819
    assert response_lista_utilidad_por_hora[0]['utilidad_bebidas_hora']==231.79886162418398
    assert response_lista_utilidad_por_hora[0]['utilidad_platillos_hora']==1302.997158252635
    assert response_lista_utilidad_por_hora[0]['utilidad_vinos_hora']==766.1589749999999

def test_costo_por_hora_historico_query(mocker):
    mock_response_dao=[{'hora_vendido': 21.0, 'costo_total': 6843.368155218679, 'costo_platillos': 3368.994767139463, 
    'costo_bebidas': 2406.507988079217, 'costo_vinos': 1067.8654000000001}]

    mocker.patch('app.service_objetos_historicos.dao.query_costo_por_hora_historico',return_value=mock_response_dao)

    response_lista_costo_por_hora=service_objetos_historicos.costo_por_hora_query_historico("2020-03-10","2020-03-20")

    assert response_lista_costo_por_hora[0]['hora']==21.0
    assert response_lista_costo_por_hora[0]['costo']==6843.368155218679
    assert response_lista_costo_por_hora[0]['costo_bebidas_hora']==2406.507988079217
    assert response_lista_costo_por_hora[0]['costo_platillos_hora']==3368.994767139463
    assert response_lista_costo_por_hora[0]['costo_vinos_hora']==1067.8654000000001

def test_venta_por_hora_historico_query(mocker):
    mock_response_dao=[{'hora': 15.0, 'dinero': 21234.360029064002, 'volumen_venta': 195.0, 'volumen_venta_platillos_hora': 110.0, 
    'volumen_venta_bebidas_hora': 82.0, 'volumen_venta_vinos_hora': 3.0}]

    mocker.patch('app.service_objetos_historicos.dao.query_venta_por_hora_historico',return_value=mock_response_dao)

    response_lista_venta_por_hora=service_objetos_historicos.venta_por_hora_query_historico("2020-03-10","2020-03-20")

    assert response_lista_venta_por_hora[0]['hora']==15.0
    assert response_lista_venta_por_hora[0]['dinero']==21234.360029064002
    assert response_lista_venta_por_hora[0]['volumen_venta']==195.0
    assert response_lista_venta_por_hora[0]['volumen_venta_bebidas_hora']==82.0
    assert response_lista_venta_por_hora[0]['volumen_venta_platillos_hora']==110.0
    assert response_lista_venta_por_hora[0]['volumen_venta_vinos_hora']==3.0

def test_mesero_historico_query(mocker):
    mock_response_dao=[{'nombre': 'JORGE RUIZ', 'utilidad': 4752.7757897085085, 'venta': 7465.080672000003, 
    'fecha': datetime.date(2020, 3, 14), 'volumen_platillos': 60.0, 'monto_platillos': 5327.280503999998, 
    'volumen_bebidas': 38.0, 'monto_bebidas': 1726.2000000000003, 'volumen_vinos': 4.2, 'monto_vinos': 411.60016799999994}]

    mocker.patch('app.service_objetos_historicos.dao.query_mesero_historico',return_value=mock_response_dao)

    response_lista_mesero=service_objetos_historicos.mesero_query_historico("2020-03-10","2020-03-20")

    assert response_lista_mesero[0]['nombre']=='JORGE RUIZ'
    assert response_lista_mesero[0]['utilidad']==4752.7757897085085
    assert response_lista_mesero[0]['venta']==7465.080672000003
    assert response_lista_mesero[0]['monto_bebidas']==1726.2000000000003
    assert response_lista_mesero[0]['volumen_platillos']==60.0
    assert response_lista_mesero[0]['monto_vinos']==411.60016799999994
    assert response_lista_mesero[0]['volumen_vinos']==4.2

def test_monto_volumen_historico(mocker):
    mock_response_dao=[{'volumen': 1370.9, 'monto': 141059.94153888006}]
    
    mocker.patch('app.service_objetos_historicos.dao.query_monto_volumen_historico',return_value=mock_response_dao)

    response_lista_valores=service_objetos_historicos.monto_volumen_historico("2020-03-10","2020-03-20")

    assert response_lista_valores[0]['volumen']==1370.9
    assert response_lista_valores[0]['monto']==141059.94153888006
    

def test_return_final_response(mocker):  

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

    mocker.patch('app.service_objetos_historicos.dao.query_producto_mas_vendido_historico',return_value=mock_producto_mas_vendido_dao) 

    mocker.patch('app.service_objetos_historicos.dao.query_utilidad_por_hora_historico',return_value=mock_utilidad_por_hora_dao)

    mocker.patch('app.service_objetos_historicos.dao.query_costo_por_hora_historico',return_value=mock_costo_por_hora_dao)

    mocker.patch('app.service_objetos_historicos.dao.query_venta_por_hora_historico',return_value=mock_venta_por_hora_dao)

    mocker.patch('app.service_objetos_historicos.dao.query_mesero_historico',return_value=mock_mesero_dao)

    mocker.patch('app.service_objetos_historicos.dao.query_monto_volumen_historico',return_value=mock_monto_volumen_dao)

    response=service_objetos_historicos.return_final_response('2020-03-10','2020-03-20')

    assert len(response.producto_mas_vendido_bebidas)==1
    assert response.producto_mas_vendido_platillos[0]['grupo_platillo']=='A11'
    assert response.utilidad_por_hora[0]['utilidad']==717.003320987953
    assert response.costo_por_hora[0]['costo_vinos_hora']==335.51750400000003
    assert response.venta_por_hora[0]['dinero']==668.6401679999999
    assert response.mesero[0]['monto_platillos']==997.0800839999999
    assert response.monto_volumen[0]['volumen']==118.2

