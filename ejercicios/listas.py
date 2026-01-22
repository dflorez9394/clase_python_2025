print("** STOCK CONTROL **")

stock = []

while True: 
    print("\n--- MENU STOCK ---")
    print("1.Agregar Stock ")
    print("2.Listar Stocks ")
    print("3.Ver Stock de estadisticas ")
    print("4.Eliminar Stock ")
    print("5.salir ")

    opcion = input("\nSeleccione una opción: ")



    if opcion == "1":
        cantidad = int(input("Ingrese la cantidad del producto: "))

        if cantidad < 0:
            print("No se permiten valores negativos ")
        else:
            stock.append(cantidad)
            print("Stock agregado correctamente ")
     
    
    elif opcion == "2":
        if not stock:
            print("No hay stocks registrados ")
        else:
            for i in range(len(stock)):
                print(f"Producto {i + 1}: {stock[i]}")
            
    
    elif opcion == "3":
        if not stock:
            print("No hay datos para mostrar estadísticas ")
        else:
            total = sum(stock)
            stock_bajo = 0

            for s in stock:
                if s < 10:
                    stock_bajo += 1

            print("Total de productos (suma): ", total)
            print("Productos con stock bajo (<10): ", stock_bajo)
            print("Cantidad de productos registrados: ", len(stock))
            print("Stock más alto:", max(stock))
      
    
    elif opcion == "4":
        stock.clear()
        print("Todos los productos fueron eliminados ")
    

    elif opcion == "5":
        print("Programa finalizado ")
        break
    
    else:
        print("Opción inválida. Intente nuevamente ")


