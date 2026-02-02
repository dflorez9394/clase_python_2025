productos = []
id_actual = 1


def mostrar_menu():
    print("\n SISTEMA DE INVENTARIO Y VENTAS ")
    print("1. Registrar nuevo producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar productos por nombre")
    print("4. Eliminar un producto")
    print("5. Mostrar productos sin disponibilidad")
    print("6. Realizar una venta")
    print("7. Salir")

# 1. Registrar nuevo producto
def registrar_producto():
    global id_actual

    nombre = input("Nombre del producto: ")
    precio = float(input("Precio de venta: "))
    cantidad = int(input("Cantidad disponible: "))

    estado = "Disponible"
    if cantidad == 0:
        estado = "No disponible"

    producto = {
        "id": id_actual,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "estado": estado
    }

    productos.append(producto)
    id_actual += 1
    print("Producto registrado correctamente.")

# 2. Mostrar todos los productos
def mostrar_productos():
    if len(productos) == 0:
        print("No hay productos registrados.")
    else:
        print("\nLISTA DE PRODUCTOS:")
        for p in productos:
            print(f"""
            ID: {p['id']}
            Nombre: {p['nombre']}
            Precio: ${p['precio']}
            Cantidad: {p['cantidad']}
            Estado: {p['estado']}
            --------------------------
            """)

#3. Buscar productos por su nombre
def buscar_producto():
    texto = input("Ingrese texto a buscar: ").lower()
    encontrado = False

    for p in productos:
        if texto in p["nombre"].lower():
            print(f"ID: {p['id']} | {p['nombre']} | Cantidad: {p['cantidad']}")
            encontrado = True

    if not encontrado:
        print("No se encontraron productos.")

# 4. Eliminar un producto
def eliminar_producto():
    id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    for p in productos:
        if p["id"] == id_eliminar:
            productos.remove(p)
            print("Producto eliminado correctamente.")
            return

    print("El ID ingresado no existe.")

# 5. Mostrar productos sin disponibilidad
def mostrar_sin_stock():
    sin_stock = False
    print("\nProductos sin disponibilidad:")

    for p in productos:
        if p["cantidad"] == 0:
            print(f"ID: {p['id']} | {p['nombre']}")
            sin_stock = True

    if not sin_stock:
        print("Todos los productos tienen stock.")

#6. Realizar una venta
def realizar_venta():
    id_venta = int(input("Ingrese el ID del producto: "))
    cantidad_vender = int(input("Cantidad a vender: "))

    for p in productos:
        if p["id"] == id_venta:
            if p["cantidad"] == 0:
                print("Producto no disponible.")
                return
            if cantidad_vender > p["cantidad"]:
                print("Cantidad supera el stock.")
                return

            total = cantidad_vender * p["precio"]
            p["cantidad"] -= cantidad_vender

            if p["cantidad"] == 0:
                p["estado"] = "No disponible"

            print(f"Venta realizada. Total a pagar: ${total}")
            return

    print("Producto no encontrado.")

    print("ESTE ES EL ARCHIVO CORRECTO")