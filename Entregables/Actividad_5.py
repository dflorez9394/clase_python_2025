#Crea un programa en Python que permita gestionar el stock de productos usando una lista y un menú de opciones.

stocks = []

while True:
    print("1. Agregar stock")
    print("2. Listar stocks")
    print("3. Ver estadísticas")
    print("4. Eliminar (limpiar lista)")
    print("5. Salir")

    opcion = input("Seleccione un producto: ")

    # 1. Agregar stock
    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad de producto: "))

        if cantidad < 0:
            print("No se permiten valores negativos.")
        else:
            stocks.append(cantidad)
            print("Stock agregado correctamente.")

    # 2. Listar stocks
    elif opcion == "2":
        if len(stocks) == 0:
            print("No hay stocks registrados.")
        else:
            print("\n Lista de stocks:")
            for i in range(len(stocks)):
                print(f"Producto {i + 1}: {stocks[i]} unidades")

    # 3. Ver estadísticas
    elif opcion == "3":
        if len(stocks) == 0:
            print("No hay datos para mostrar estadísticas.")
        else:
            total_stock = sum(stocks)
            stock_bajo = 0

            for s in stocks:
                if s < 10:
                    stock_bajo += 1

            print("\n Estadísticas:")
            print("Total de productos en stock:", total_stock)
            print("Cantidad de productos con stock bajo (<10):", stock_bajo)
            print("Cantidad total de productos registrados:", len(stocks))
            print("Stock más alto registrado:", max(stocks))

    # 4. Eliminar (limpiar lista)
    elif opcion == "4":
        stocks.clear()
        print("Todos los productos han sido eliminados.")

    # 5. Salir
    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")





