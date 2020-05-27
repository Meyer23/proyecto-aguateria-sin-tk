import os 
import sys 
import logging 
import datetime
import time 
import hashlib 

logging.basicConfig(filename = 'application.log', level = logging.DEBUG)
logger = logging

class Util():
	
	def limpiar_pantalla():
		'''---Limpia la pantalla---'''
		os.system('clear')
		
	def leer_numero(msg, valor_minimo, valor_maximo = None, default = None): 
		'''---Valida que se ingrese un numero dentro de un rango---'''
			
		while(True): 
			cualquier_valor = input(msg)
			try:
				#tratamos de convertira un numero entero
				number = int(cualquier_valor)
				#controlar si el numero se encuentra o no en el rango
				if((not valor_maximo == None) and (number<valor_minimo or number>valor_maximo)) or ((valor_maximo == None) and (number<valor_minimo)):
					raise Exception("Numero fuera de rango [min_value = " +
					str(valor_minimo)+ ", max_value = "+ str(valor_maximo) + "]: ")
				#se retorna el valor válido ingresado por el usuario
				return number
			except ValueError as e: 
				print("Debe ingresar un numero") 
			except TypeError as e: 
				print("Debe ingresar un numero")
			except Exception as e:
				print (e)
				
	def leer_cadena(msg, obligatorio, default = None):
		'''---Función que obtiene una cadena'''
		
		while(True): 
			if default: 
				msg = msg + default + chr(8) * len(default)
			
			data = input(msg)
			data = data or default
			try:
				if obligatorio and len(data.strip()) == 0:
					raise Exception("Debe ingresar valor!") 
				#se retorna valor valido ingresado por el usuario
				return data
			except Exception as e:
				print(e)
	
	def leer_fecha(msg, obligatorio, default = None):
		
		'''Lee una fecha, debe ser obligatoria'''
		
		while(True):
			data = input(msg)
			try:
				if obligatorio and len(data.strip()) == 0:
					raise Exception("Debe ingresar valor!")
					
				return datetime.datetime.strptime(data, '%d/%m/%y').date()
			except Exception as e: 
				print(e)
				
	def get_logger():
		return logging
	
	def pause():
		
		'''El programa se queda en espera hasta presionar la tecla enter'''
		
		key = input("Presione la tecla enter para continuar...")
		
	def get_md5(source):
		'''Permite el uso de caracteres especiales'''
		return haslib.md5(source.encode("utf-8")).hexdigest()
				
