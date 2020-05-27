 
#Constantes 
SALIR = 0 
OPCION1 = 1 
OPCION2 = 2 
OPCION3 = 3 
OPCION4 = 4

class Pantalla():
	"""Esta clase representa el menú principal con el que el usuario
		va interactuar, contiene las impresiones que se muestran en el menú"""
			
	@staticmethod
	def menu_principal(): 
		"""---Menú Principal"""
			
		mensaje = "---Aguatería Vecinal---\n" + \
				"Ingrese una opción: \n" + \
				str(OPCION1) + " - Usuario\n" +\
				str(OPCION2) + " - Empleado\n" +\
				str(OPCION3) + " - Solicitud\n" +\
				str(OPCION4) + " - Orden de trabajo\n" + \
				str(SALIR) + " - Salir\n"
						
		Pantalla.impresion(mensaje)
			
	@staticmethod
	def menu_usuario(): 
		"""Menú del usuario"""
				
		mensaje = "---Usuario---\n" + \
			"Ingrese una opción: \n" + \
			str(OPCION1) + " - Cargar nuevo Usuario\n" +\
			str(OPCION2) + " - Buscar Usuario\n" + \
			str(OPCION3) + " ----\n" + \
			str(SALIR) + " - Volver al menú\n"
						
		Pantalla.impresion(mensaje)
				
	@staticmethod 
	def menu_empleado(): 
		"""Menú del empleado"""
				
		mensaje = "---Empleado---\n" + \
			"Ingrese una opción: \n" + \
			str(OPCION1) + " - Agregar Empleado\n" + \
			str(OPCION2) + " - Buscar Empleado\n" + \
			str(OPCION3) + " ---\n" + \
		    str(SALIR) + " - Volver al menú\n"
						
		Pantalla.impresion(mensaje)
			
	@staticmethod
	def menu_solicitud(): 
		"""Menú de las solicitudes"""
				
		mensaje = "---Solicitud---\n" + \
			"Ingrese una opción: \n" + \
			str(OPCION1) + "- Solicitar Conexión\n" + \
			str(OPCION2) + "- Solicitar Desconexión\n" + \
			str(OPCION3) + "- Solicitar Reparación\n" + \
			str(OPCION4) + "- Buscar Solicitud\n" + \
			str(SALIR) + "- Volver al menú\n"
						
		Pantalla.impresion(mensaje)
				
	@staticmethod
	def menu_orden(): 
		"""Menú de las ordenes de trabajo""" 
				
		mensaje = "---Ordenes de trabajo---\n" + \
		"Ingrese una opción: \n" + \
			str(OPCION1) + " - Generar Orden de Trabajo\n" + \
			str(OPCION2) + " - Buscar Orden de Trabajo\n" + \
			str(SALIR) + " - Volver al menú\n"
						
		Pantalla.impresion(mensaje)
				
	@staticmethod
	def impresion(mensaje): 
		"""---Impríme el texto enviado---"""
		print(mensaje)
