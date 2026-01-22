print("** PRODUCT STOCK **")

stocks = []

while True:
    print("\n--- MENÚ ---")
    print("1. Agregar stock")
    print("2. Listar stocks")
    print("3. Ver estadísticas")
    print("4. Eliminar (limpiar lista)")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

  
    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad del producto: "))

        if cantidad < 0:
            print("No se permiten valores negativos.")
        else:
            stocks.append(cantidad)
            print("Stock agregado correctamente.")

   
    elif opcion == "2":
        if not stocks:
            print("No hay stocks registrados.")
        else:
            for i in range(len(stocks)):
                print(f"Producto {i + 1}: {stocks[i]}")

    
    elif opcion == "3":
        if not stocks:
            print("No hay datos para mostrar estadísticas.")
        else:
            total = sum(stocks)
            stock_bajo = 0

            for s in stocks:
                if s < 10:
                    stock_bajo += 1

            print("Total de productos (suma):", total)
            print("Productos con stock bajo (<10):", stock_bajo)
            print("Cantidad de productos registrados:", len(stocks))
            print("Stock más alto:", max(stocks))

   
    elif opcion == "4":
        stocks.clear()
        print("Todos los productos fueron eliminados.")

    # 5. Salir
    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.\n Intente nuevamente.")
