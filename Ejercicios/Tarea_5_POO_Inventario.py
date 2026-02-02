# =========================
# CLASE PRODUCTO
# =========================
class Producto:
    contador_id = 1  # Atributo de clase (compartido por todos los productos)

    def __init__(self, nombre, precio, cantidad):
        self.id = Producto.contador_id
        Producto.contador_id += 1

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = cantidad > 0

    def actualizar_estado(self):
        self.disponible = self.cantidad > 0

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"ID: {self.id} | "
            f"Nombre: {self.nombre} | "
            f"Precio: ${self.precio} | "
            f"Cantidad: {self.cantidad} | "
            f"Estado: {estado}"
        )


# =========================
# CLASE INVENTARIO
# =========================
class Inventario:
    def __init__(self):
        self.productos = []

    def registrar_producto(self, nombre, precio, cantidad):
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            print(producto)

    def buscar_por_nombre(self, texto):
        texto = texto.lower()
        encontrados = [
            p for p in self.productos if texto in p.nombre.lower()
        ]

        if not encontrados:
            print("No se encontraron productos.")
            return

        for producto in encontrados:
            print(producto)

    def eliminar_producto(self, producto_id):
        for producto in self.productos:
            if producto.id == producto_id:
                self.productos.remove(producto)
                print("Producto eliminado.")
                return

        print("Error: ID no encontrado.")

    def productos_sin_disponibilidad(self):
        sin_stock = [p for p in self.productos if p.cantidad == 0]

        if not sin_stock:
            print("Todos los productos tienen disponibilidad.")
            return

        for producto in sin_stock:
            print(producto)

    def realizar_venta(self, producto_id, cantidad):
        for producto in self.productos:
            if producto.id == producto_id:

                if not producto.disponible:
                    print("Producto no disponible.")
                    return

                if cantidad > producto.cantidad:
                    print("Cantidad insuficiente en inventario.")
                    return

                producto.cantidad -= cantidad
                producto.actualizar_estado()

                total = cantidad * producto.precio
                print(f"Venta realizada. Total a pagar: ${total}")
                return

        print("Producto no encontrado.")


# =========================
# MENÚ PRINCIPAL
# =========================
def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Buscar producto por nombre")
        print("4. Eliminar producto")
        print("5. Mostrar productos sin disponibilidad")
        print("6. Realizar venta")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            inventario.registrar_producto(nombre, precio, cantidad)

        elif opcion == "2":
            inventario.mostrar_productos()

        elif opcion == "3":
            texto = input("Texto a buscar: ")
            inventario.buscar_por_nombre(texto)

        elif opcion == "4":
            producto_id = int(input("ID del producto: "))
            inventario.eliminar_producto(producto_id)

        elif opcion == "5":
            inventario.productos_sin_disponibilidad()

        elif opcion == "6":
            producto_id = int(input("ID del producto: "))
            cantidad = int(input("Cantidad a vender: "))
            inventario.realizar_venta(producto_id, cantidad)

        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


menu()
