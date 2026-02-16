from inventario import Inventario
from producto import Producto


def mostrar_menu():
    print("\n==============================")
    print("   SISTEMA DE INVENTARIOS")
    print("==============================")
    print("1) Añadir producto")
    print("2) Eliminar producto por ID")
    print("3) Actualizar producto")
    print("4) Buscar producto por nombre")
    print("5) Mostrar todos los productos")
    print("0) Salir")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            pid = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(pid, nombre, cantidad, precio)

            if inventario.agregar_producto(producto):
                print("Producto agregado correctamente.")
            else:
                print("Ya existe un producto con ese ID.")

        elif opcion == "2":
            pid = input("ID a eliminar: ")
            if inventario.eliminar_producto_por_id(pid):
                print("Producto eliminado.")
            else:
                print("No se encontró el producto.")

        elif opcion == "3":
            pid = input("ID a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deja vacío si no quieres cambiar): ")
            nuevo_precio = input("Nuevo precio (deja vacío si no quieres cambiar): ")

            cantidad = int(nueva_cantidad) if nueva_cantidad else None
            precio = float(nuevo_precio) if nuevo_precio else None

            if inventario.actualizar_producto(pid, cantidad, precio):
                print("Producto actualizado.")
            else:
                print("No se encontró el producto.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_productos_por_nombre(nombre)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron productos.")

        elif opcion == "5":
            productos = inventario.obtener_todos()
            if productos:
                for p in productos:
                    print(p)
            else:
                print("Inventario vacío.")

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
