# ================== CLASE PRODUCTO ==================

class Producto:
    contador_id = 1

    def __init__(self, nombre, precio, cantidad):
        self.id = Producto.contador_id
        Producto.contador_id += 1

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.estado = "Disponible" if cantidad > 0 else "No disponible"

    def actualizar_estado(self):
        if self.cantidad > 0:
            self.estado = "Disponible"
        else:
            self.estado = "No disponible"

    def mostrar_info(self):
        print("===================================")
        print(f"ID: {self.id}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Cantidad disponible: {self.cantidad}")
        print(f"Estado: {self.estado}")
        print("===================================")


# ================== CLASE INVENTARIO ==================

class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self):
        print("\n--- Registrar nuevo producto ---")
        nombre = input("Nombre del producto: ")

        while True:
            try:
                precio = float(input("Precio del producto: "))
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    continue
                break
            except:
                print("Ingrese un valor válido.")

        while True:
            try:
                cantidad = int(input("Cantidad disponible: "))
                if cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    continue
                break
            except:
                print("Ingrese un número válido.")

        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)
        print("Producto registrado correctamente.\n")

    def mostrar_productos(self):
        print("\n--- Lista de productos ---")
        if not self.productos:
            print("No hay productos registrados.\n")
            return

        for producto in self.productos:
            producto.mostrar_info()

    def buscar_por_nombre(self):
        print("\n--- Buscar producto por nombre ---")
        texto = input("Ingrese texto a buscar: ").lower()

        encontrados = [p for p in self.productos if texto in p.nombre.lower()]

        if not encontrados:
            print("No se encontraron productos.\n")
        else:
            for producto in encontrados:
                producto.mostrar_info()

    def eliminar_producto(self):
        print("\n--- Eliminar producto ---")
        try:
            id_buscar = int(input("Ingrese el ID del producto: "))
        except:
            print("ID inválido.\n")
            return

        for producto in self.productos:
            if producto.id == id_buscar:
                self.productos.remove(producto)
                print("Producto eliminado correctamente.\n")
                return

        print("Producto no encontrado.\n")

    def productos_sin_stock(self):
        print("\n--- Productos sin disponibilidad ---")
        sin_stock = [p for p in self.productos if p.cantidad == 0]

        if not sin_stock:
            print("Todos los productos tienen stock.\n")
        else:
            for producto in sin_stock:
                producto.mostrar_info()

    def realizar_venta(self):
        print("\n--- Realizar venta ---")
        try:
            id_buscar = int(input("ID del producto: "))
            cantidad_vender = int(input("Cantidad a vender: "))
        except:
            print("Datos inválidos.\n")
            return

        for producto in self.productos:
            if producto.id == id_buscar:

                if producto.estado == "No disponible":
                    print("El producto no está disponible.\n")
                    return

                if cantidad_vender > producto.cantidad:
                    print("No hay suficiente stock.\n")
                    return

                total = cantidad_vender * producto.precio
                producto.cantidad -= cantidad_vender
                producto.actualizar_estado()

                print("Venta realizada con éxito.")
                print(f"Total a pagar: ${total}\n")
                return

        print("Producto no encontrado.\n")


# ================== MENÚ PRINCIPAL ==================

def menu():
    inventario = Inventario()

    while True:
        print("""
========= SISTEMA DE INVENTARIO =========
1. Registrar nuevo producto
2. Mostrar todos los productos
3. Buscar productos por nombre
4. Eliminar un producto
5. Mostrar productos sin disponibilidad
6. Realizar una venta
7. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.registrar_producto()
        elif opcion == "2":
            inventario.mostrar_productos()
        elif opcion == "3":
            inventario.buscar_por_nombre()
        elif opcion == "4":
            inventario.eliminar_producto()
        elif opcion == "5":
            inventario.productos_sin_stock()
        elif opcion == "6":
            inventario.realizar_venta()
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.\n")


# ================== EJECUCIÓN ==================

menu()

