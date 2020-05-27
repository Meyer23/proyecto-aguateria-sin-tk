from Util import * 
from Modelo import *
from Menu import * 
from Controlador import * 

class Metodo(): 

	@staticmethod
	def agregar_usuario():
			
		'''Función para agregar un nuevo usuario'''
	
		lista_usuarios = []
		Util.limpiar_pantalla()
		print("---*Agregar nuevo usuario*---")
		cedula = Util.leer_numero("Ingrese el número de cedula del nuevo usuario: ", True)
		controlar_cedula = ControladorUsuario()
		cedula_buscada = controlar_cedula.buscar_usuario(cedula) 
		if cedula_buscada is None: #Verificamos si ya existe algún usuario con la cedula ingresada
			nombre = Util.leer_cadena("Ingrese el nombre del nuevo usuario: ", True)
			apellido = Util.leer_cadena("Ingrese el apellido del nuevo usuario: ", True)
			direccion = Util.leer_cadena("Ingrese la dirección del nuevo usuario: ", True) 
			nrotelefono = Telefono(Util.leer_numero("Digite el número de teléfono del nuevo usuario: ", True))
			email = CorreoElectronico(Util.leer_cadena('Ingrese la dirección de correo electrónico del nuevo usuario: ', False))
			contactos = [str(nrotelefono), str(email)]
			nueva_persona = Persona(cedula = cedula, nombre = nombre, apellido = apellido, direccion = direccion, contactos = contactos) 
			nuevo_usuario = Usuario(nueva_persona)
			lista_usuarios.append(nuevo_usuario)
			usuario_controlador = ControladorUsuario()
			usuario_controlador.crear(nueva_persona)
		else: 
			print("\nYa existe un usuario con la cedula ingresada!") 
		Util.pause()


	@staticmethod
	def buscar_usuario():
		"""A través de la cedula ingresada, se busca al usuario,
		pasandole la cedula al ControladorUsuario"""
		Util.limpiar_pantalla()
		print("Búsqueda de Usuario. . .") 
		cedula = Util.leer_numero("Ingrese el número de cedula: ", True) 
		usuario_controlador = ControladorUsuario()
		usuario_buscado = usuario_controlador.buscar_usuario(cedula)
		if usuario_buscado is None:
			print("\nNo existe un usuario con la cedula ingresada...")
		else:
			print("\nEl usuario buscado es: " +usuario_buscado.__str__())
		Util.pause()


	@staticmethod
	def agregar_empleado():
			
		'''Función para agregar un nuevo empleado'''
	
		lista_empleados = []
		Util.limpiar_pantalla()
		print("---*Agregar nuevo empleado*---")
		cedula = Util.leer_numero("Ingrese el número de cedula del nuevo empleado: ", True)
		buscar_cedula = ControladorEmpleado()
		cedula_buscada = buscar_cedula.buscar_empleado(cedula)
		if cedula_buscada is None: #Verificamos si ya existe algún empleado con la cedula ingresada
			nombre = Util.leer_cadena("Ingrese el nombre del nuevo empleado: ", True)
			apellido = Util.leer_cadena("Ingrese el apellido del nuevo empleado: ", True)
			direccion = Util.leer_cadena("Ingrese la dirección del nuevo empleado: ", True) 
			nrotelefono = Telefono(Util.leer_numero("Digite el número de teléfono del nuevo empleado: ", True))
			email = CorreoElectronico(Util.leer_cadena('Ingrese la dirección de correo electrónico del nuevo empleado: ', False))
			contactos = [str(nrotelefono), str(email)]
			nueva_persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, direccion=direccion, contactos=contactos)
			nuevo_empleado = Empleado(nueva_persona)
			lista_empleados.append(nuevo_empleado)
			empleado_controlador = ControladorEmpleado()
			empleado_controlador.crear(nueva_persona)
		else: 
			print("\nYa existe un empleado con la cedula ingresada!")
		Util.pause()


	@staticmethod
	def buscar_empleado():
		
		'''Método que sirve para buscar un empleado ingresando el número de cedula'''
		
		Util.limpiar_pantalla()
		print("Búsqueda de Empleado. . .") 
		cedula = Util.leer_numero("Ingrese el número de cedula: ", True) 
		empleado_controlador = ControladorEmpleado()
		empleado_buscado = empleado_controlador.buscar_empleado(cedula)
		if empleado_buscado is None: 
			print("\nNo existe ningun empleado con la cedula ingresada...")
		else: 
			print("\nEl empleado buscado es: " +empleado_buscado.__str__())
		Util.pause()


	@staticmethod
	def agregar_solicitud_conexion():
		
		'''Método que sirve para agregar una nueva solicitud del tipo CONEXIÓN, 
		el usuario debe estar REGISTRADO antes de poder solicitar un servicio.'''
		
		Util.limpiar_pantalla()
		print("Solicitud de conexión. . .")
		cedula = Util.leer_numero("Ingrese el número de cedula: ", True) 
		usuario_controlador = ControladorUsuario()
		usuario_buscado = usuario_controlador.buscar_usuario(cedula)
		if usuario_buscado is None: #Debe existir un usuario con la cedula ingresada para poder realizar una solicitud
			print("\nNo existe ningún usuario con la cedula ingresada, para realizar una solicitud, \ndebe agregar al nuevo usuario.")
		else: #Si existe el usuario, se continua pidiendo los datos necesarios. 
			print("\nCreando solicitud para el usuario: " +usuario_buscado.__str__())
			descripcion = Util.leer_cadena("\nDetalles de lo que necesita el usuario: ", True)
			fecha = Util.leer_fecha("\nIngrese la fecha: ", True) 
			nueva_solicitud = Solicitud(cedula = cedula, descripcion = descripcion, fecha = fecha) 
			solicitud_controlador = ControladorSolicitud()
			solicitud_controlador.crear(nueva_solicitud) 
		Util.pause()


	@staticmethod
	def agregar_solicitud_desconexion():
		
		'''Este método permite agregar una solicitud de desconexión'''
		
		Util.limpiar_pantalla()
		print("Solicitud de desconexión. . .")
		cedula = Util.leer_numero("Ingrese el número de cedula: ", True) 
		usuario_controlador = ControladorUsuario()
		usuario_buscado = usuario_controlador.buscar_usuario(cedula)
		if usuario_buscado is None:
			print("\nNo existe ningún usuario con la cedula ingresada, para realizar una solicitud, \ndebe agregar al nuevo usuario.")
		else:
			print("\Creando solicitud de desconexión del usuario : " +usuario_buscado.__str__())
			descripcion = Util.leer_cadena("\nRazón por la cual solicita la desconexión : ", True)
			fecha = Util.leer_fecha("\nIngrese la fecha: ", True) 
			nueva_solicitud = Solicitud(cedula = cedula, descripcion = descripcion, fecha = fecha) 
			solicitud_controlador = ControladorSolicitud()
			solicitud_controlador.crear(nueva_solicitud) 
		Util.pause()


	@staticmethod
	def agregar_solicitud_reparacion():
		Util.limpiar_pantalla()
		print("Solicitud de reparación. . .")
		cedula = Util.leer_numero("Ingrese el número de cedula: ", True) 
		usuario_controlador = ControladorUsuario()
		usuario_buscado = usuario_controlador.buscar_usuario(cedula)
		if usuario_buscado is None:
			print("\nNo existe ningún usuario con la cedula ingresada, para realizar una solicitud, \ndebe agregar al nuevo usuario.")
		else:
			print("\nCreando solicitud de reparación para el usuario: " +usuario_buscado.__str__())
			descripcion = Util.leer_cadena("\n¿Qué tipo de reparación necesita el usuario?: ", True)
			fecha = Util.leer_fecha("\nIngrese la fecha: ", True) 
			nueva_solicitud = Solicitud(cedula = cedula, descripcion = descripcion, fecha = fecha) 
			solicitud_controlador = ControladorSolicitud()
			solicitud_controlador.crear(nueva_solicitud) 
		Util.pause()


	@staticmethod
	def buscar_solicitud():
		Util.limpiar_pantalla()
		print("Búsqueda de Solicitud. . .") 
		cedula = Util.leer_numero("Ingrese el número de cedula: ", True) 
		solicitud_controlador = ControladorSolicitud()
		solicitud_buscada = solicitud_controlador.buscar_solicitud(cedula)
		if solicitud_buscada is None: 
			print("\nNo existe ninguna solicitud con la cedula ingresada...")
		else: 
			print("\nSolicitud encontrada: " +solicitud_buscada.__str__())
		Util.pause()


	@staticmethod
	def generar_orden():
		'''Genera una orden de trabajo en el caso que exista una solicitud previa'''
		Util.limpiar_pantalla()
		print("\nGenerar Orden, se buscará previamente una solicitud. . .") 
		cedula = Util.leer_numero("Ingrese el número de cedula: ", True) 
		solicitud_controlador = ControladorSolicitud()
		solicitud_buscada = solicitud_controlador.buscar_solicitud(cedula)
		if solicitud_buscada is None: 
			print("\nNo existe una solicitud registrada previamente con la cedula ingresada. . . ")
			print("\nPara generar una orden, debe existir una solicitud previamente registrada!") 
		else: 
			print("\nSolicitud encontrada, se generará una orden de trabajo para: " +solicitud_buscada.__str__())
			cedula = Util.leer_numero("\nAsigne un empleado encargado, ingresando el número de cedula: ", True) 
			empleado_controlador = ControladorEmpleado()
			empleado_buscado = empleado_controlador.buscar_empleado(cedula)
			if empleado_buscado is None:
				print("\nNo existe un empleado con el número de cedula ingresado.")
			else:
				print("\nEl empleado a cargo será: " +empleado_buscado.__str__())
				descripcion = Util.leer_cadena("\nDescriba el trabajo a ser realizado: ", True)
				fecha = Util.leer_fecha("\nIngrese la fecha en la cual se realizará el trabajo: ", True)
				direccion = Util.leer_cadena("\nIngrese la dirección donde va realizarse el trabajo: ", True)
				nueva_orden = Orden(cedula = cedula, descripcion = descripcion, fecha = fecha, direccion = direccion)
				controlador_orden = ControladorOrden()
				controlador_orden.crear(nueva_orden)
		Util.pause()


	@staticmethod
	def buscar_orden():
		Util.limpiar_pantalla()
		print("Búsqueda de Ordenes de trabajo . .") 
		cedula = Util.leer_numero("Ingrese el número de cedula (Empleado a Cargo): ", True) 
		orden_controlador = ControladorOrden()
		orden_buscada = orden_controlador.buscar_orden(cedula)
		if orden_buscada is None: 
			print("\nNo existe ninguna orden de trabajo con la cedula ingresada...")
		else: 
			print("\nOrden encontrada: " +orden_buscada.__str__())
		Util.pause()

	def salir():
		'''Cierra la aplicacion'''
		Util.limpiar_pantalla()
		print(("***Se cerrará la aplicación***") + 'Desea cerrar la aplicación? Si(1), No(0)')
		opcion_menu = Util.leer_numero('\n', 0, 1)
		if opcion_menu == 0:
			Util.pause()
		elif opcion_menu == 1:
			Util.limpiar_pantalla()
			exit()

