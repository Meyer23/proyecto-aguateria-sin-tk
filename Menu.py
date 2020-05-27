__author__ = "Robert Fernando Meyer Meza"
__license__ = "Public Domain"
__version__ = "1.0.0"
__email__ = "rmeyer93@fpuna.edu.py"
__status__ = "Prototype"

from Metodos import *
from Util import Util
from Impresiones import *


class Aplicacion():
    '''---Contiene el menú principal y permitirá al usuario elegir entre las siguientes opciones---'''

    def main():
        Menu.vista_menu()


class Menu():

    def vista_menu():

        '''Se muestra el menú principal, seleccionando una opción, se mostrará un sub-menú para cada operación'''
        Util.limpiar_pantalla()
        Pantalla.menu_principal()
        opcion = Util.leer_numero("\nElija una opcion: ", 0, 4)
        if opcion == 1:
            Util.limpiar_pantalla()
            Pantalla.menu_usuario()
            opc = Util.leer_numero('\nSeleccione una opción: ', 0, 2)
            if opc == 1:
                Metodo.agregar_usuario()
            elif opc == 2:
                Metodo.buscar_usuario()
            elif opc == 0:
                Menu.vista_menu()
        elif opcion == 2:
            Util.limpiar_pantalla()
            Pantalla.menu_empleado()
            opc = Util.leer_numero('\nSeleccione una opción: ', 0, 2)
            if opc == 1:
                Metodo.agregar_empleado()
            elif opc == 2:
                Metodo.buscar_empleado()
            elif opc == 0:
                Menu.vista_menu()
        elif opcion == 3:
            Util.limpiar_pantalla()
            Pantalla.menu_solicitud()
            opc = Util.leer_numero('\nSeleccione una opción: ', 0, 4)
            if opc == 1:
                Metodo.agregar_solicitud_conexion()
            elif opc == 2:
                Metodo.agregar_solicitud_desconexion()
            elif opc == 3:
                Metodo.agregar_solicitud_reparacion()
            elif opc == 4:
                Metodo.buscar_solicitud()
            elif opc == 0:
                Menu.vista_menu()
        elif opcion == 4:
            Util.limpiar_pantalla()
            Pantalla.menu_orden()
            opc = Util.leer_numero('\nSeleccione una opción: ', 0, 2)
            if opc == 1:
                Metodo.generar_orden()
            elif opc == 2:
                Metodo.buscar_orden()
            elif opc == 0:
                Menu.vista_menu()
        elif opcion == 0:
            Metodo.salir()

        while (True):
            Menu.vista_menu()


if __name__ == '__main__':
    Aplicacion.main()
