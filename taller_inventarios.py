productos = []
cantidades = []

while True:
    print("\nMENÚ CONTROL DE STOCK")
    print("1. Agregar stock")
    print("2. Listar stocks")
    print("3. Ver estadísticas")
    print("4. Eliminar (limpiar lista)")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # 1. Agregar stock
    if opcion == "1":
        producto = input("Ingrese el tipo de producto: ")
        cantidad = int(input("Ingrese la cantidad: "))

        if cantidad < 0:
            print("No se permiten valores negativos")
        else:
            productos.append(producto)
            cantidades.append(cantidad)
            print("Producto agregado correctamente")

    # 2. Listar stocks
    elif opcion == "2":
        if len(productos) == 0:
            print("No hay productos registrados")
        else:
            for i in range(len(productos)):
                print(f"{i + 1}. Producto: {productos[i]} - Cantidad: {cantidades[i]}")

    # 3. Ver estadísticas
    elif opcion == "3":
        if len(cantidades) == 0:
            print("No hay datos para estadísticas")
        else:
            total_stock = sum(cantidades)

            stock_bajo = 0
            for c in cantidades:
                if c < 10:
                    stock_bajo += 1

            print("Total de productos (suma de cantidades):", total_stock)
            print("Productos con stock bajo (<10):", stock_bajo)
            print("Cantidad total de productos registrados:", len(productos))
            print("Stock más alto registrado:", max(cantidades))

    # 4. Eliminar (limpiar lista)
    elif opcion == "4":
        productos.clear()
        cantidades.clear()
        print("Todos los productos fueron eliminados")

    # 5. Salir
    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Opción inválida")
