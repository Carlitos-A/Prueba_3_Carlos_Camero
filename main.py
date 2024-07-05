# --------------------------- Imports  ----------------------
import os
import globales

# -------------------------- Menus --------------------------


def menu_estadisticas():
    while True:
        print("1. Producto con valor más alto")
        print("2. Producto con valor del IVA más bajo")
        print("3. Promedio del valor de los productos")
        print("4. Media geométrica del valor de los productos")
        print("5. Salir del programa")

        op = globales.seleccionar_opcion(5)

        if op == 1:
            globales.buscar_producto("alto")

        if op == 2:
            globales.buscar_producto("bajo")

        if op == 3:
            globales.promedio()

        if op == 4:
            globales.geometrica()

        if op == 5:
            input("Saliendo del programa (Enter)")
            return




def menu_principal():
    while True:
        os.system("cls")
        print("1. Asignar montos aleatorios")
        print("2. Ver estadisticas")
        print("3. Salir del programa")

        op = globales.seleccionar_opcion(3)

        if op == 1:
            globales.aleatorio()
        
        if op == 2:
            menu_estadisticas()
        
        if op == 3:
            input("Saliendo del programa (Enter)")
            return


if __name__ == "__main__":
    menu_principal()