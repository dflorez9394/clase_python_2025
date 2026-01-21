print("****** CONTROL DE STOCK ******")

stock = []

while True:
    print("\n--- MENU DE CONTROL DE STOCK ---")
    print("1. Agregar stock")
    print("2. Listar stock")
    print("3. Ver estadísticas")
    print("4. Eliminar (limpiar lista)")
    print("5. Salir")

    opcion = input("Escoja una opción del menú: ")

    # OPCIÓN 1 - Agregar stock
    if opcion == "1":
        try:
            cant_producto = int(input("Ingrese la cantidad de producto: "))
            while cant_producto <= 0:
                print("La cantidad debe ser mayor a cero")
                cant_producto = int(input("Ingrese la cantidad de producto: "))

            stock.append(cant_producto)
            print("Cantidad agregada correctamente al stock")

        except ValueError:
            print("Debe ingresar un número entero positivo")

    # OPCIÓN 2 - Listar stock
    elif opcion == "2":
        if not stock:
            print("La lista de stock está vacía")
        else:
            print("\n--- STOCK ---")
            for i, s in enumerate(stock, start=1):
                print(f"Producto {i}: {s}")

    # OPCIÓN 3 - Ver estadísticas
    elif opcion == "3":
        if not stock:
            print("No hay stock de producto disponible")
        else:
            total_unidades = sum(stock)
            productos_bajo_stock = sum(1 for s in stock if s < 10)
            cantidad_productos = len(stock)
            stock_maximo = max(stock)

            print("\n--- ESTADÍSTICAS ---")
            print(f"Total de unidades: {total_unidades}")
            print(f"Productos con bajo stock (<10): {productos_bajo_stock}")
            print(f"Cantidad de productos registrados: {cantidad_productos}")
            print(f"Stock más alto: {stock_maximo}")

    # OPCIÓN 4 - Limpiar stock
    elif opcion == "4":
        if not stock:
            print("El stock ya está vacío")
        else:
            stock.clear()
            print("El stock ha sido eliminado correctamente")

    # OPCIÓN 5 - Salir
    elif opcion == "5":
        print("Programa finalizado")
        break

    else:
        print("Ingrese una opción válida")