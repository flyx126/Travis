from src.customException import BadRequest
import src.dao_queries as dao 
import src.utils as utl
import operator


class ProductoMasVendido():
    def __init__(self,nombre,cantidad_platillos,cantidad_bebidas,cantidad_vinos,grupo_platillo,fecha):
        self.fecha=fecha
        self.nombre=nombre
        self.cantidad_platillos=cantidad_platillos
        self.cantidad_bebidas=cantidad_bebidas
        self.cantidad_vinos=cantidad_vinos
        self.grupo_platillo=grupo_platillo 

class UtilidadPorHora():
    def __init__(self,utilidad,hora,utilidad_bebidas_hora,utilidad_platillos_hora,utilidad_vinos_hora):
        self.utilidad=utilidad
        self.hora=hora
        self.utilidad_bebidas_hora=utilidad_bebidas_hora
        self.utilidad_platillos_hora=utilidad_platillos_hora
        self.utilidad_vinos_hora=utilidad_vinos_hora
    
class CostoPorHora():
    def __init__(self,costo,hora,costo_bebidas_hora,costo_platillos_hora,costo_vinos_hora):
        self.costo=costo
        self.hora=hora
        self.costo_bebidas_hora=costo_bebidas_hora
        self.costo_platillos_hora=costo_platillos_hora
        self.costo_vinos_hora=costo_vinos_hora

class VentaPorHora():
    def __init__(self,dinero,hora,volumen_venta,volumen_venta_bebidas_hora,volumen_venta_platillos_hora,volumen_venta_vinos_hora,monto_venta_bebidas_hora, monto_venta_platillos_hora,monto_venta_vinos_hora):
        self.dinero=dinero
        self.hora=hora
        self.volumen_venta=volumen_venta
        self.volumen_venta_bebidas_hora=volumen_venta_bebidas_hora
        self.volumen_venta_platillos_hora=volumen_venta_platillos_hora
        self.volumen_venta_vinos_hora=volumen_venta_vinos_hora
        self.monto_venta_bebidas_hora=monto_venta_bebidas_hora
        self.monto_venta_platillos_hora=monto_venta_platillos_hora
        self.monto_venta_vinos_hora=monto_venta_vinos_hora
	
class Mesero():
    def __init__(self,nombre,monto_bebidas,monto_platillos,monton_vinos,utilidad,venta,volumen_platillos,volumen_bebidas,volumen_vinos):
        self.nombre=nombre
        self.monto_bebidas=monto_bebidas
        self.monto_platillos=monto_platillos
        self.monto_vinos=monton_vinos
        self.volumen_platillos=volumen_platillos
        self.volumen_bebidas=volumen_bebidas
        self.volumen_vinos=volumen_vinos
        self.utilidad=utilidad
        self.venta=venta

class MontoVolumen():
    def __init__(self,monto,volumen,costo,utilidad,personas,venta):
        self.monto=monto
        self.volumen=volumen
        self.costo=costo
        self.utilidad=utilidad
        self.personas=personas
        self.venta=venta

class DistrubicionDemanda():
    def __init__(self,dia,alcohol,alimentos,bebidas_no_alcoholicas,cafe,postres,vinos):
        self.dia=dia
        self.alcohol=alcohol
        self.alimentos=alimentos
        self.bebidas_no_alcoholicas=bebidas_no_alcoholicas
        self.cafe=cafe
        self.postres=postres
        self.vinos=vinos

class DistribucionResponse():
    def __init__(self,semana,mes,tiempo):
        self.semana=semana
        self.mes=mes
        self.tiempo=tiempo

class Response:
    def __init__(self, **kwargs):
        for k in kwargs.keys():
            self.__setattr__(k, kwargs[k])

class TendenciaVenta():
    def __init__(self,mes,cantidad):
        self.mes=mes
        self.cantidad=cantidad

class TendenciaResponse():
    def __init__(self,venta_platillos_2016,venta_platillos_2017,venta_platillos_2018,venta_platillos_2019,venta_platillos_2020):
        self.venta_platillos_2016=venta_platillos_2016
        self.venta_platillos_2017=venta_platillos_2017
        self.venta_platillos_2018=venta_platillos_2018
        self.venta_platillos_2019=venta_platillos_2019
        self.venta_platillos_2020=venta_platillos_2020

class Estancia():
    def __init__(self,tiempo):
        self.tiempo=tiempo

class EstanciaResponse():
    def __init__(self,response):
        self.response=response

class Usuario():
    def __init__(self,nombre,apellido,username,password):
        self.nombre=nombre
        self.apellido=apellido
        self.username=username
        self.password=password

class GrupoPlatillo():
    def __init__(self,grupo,porcentaje,platos=[]):
        self.grupo=grupo
        self.porcentaje=porcentaje
        self.platos=platos  




    

