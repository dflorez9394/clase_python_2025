def agregar_sueldo():
    sueldo =float(input("Ingrese el sueldo: "))
    return sueldo
def mostrar_sueldos(sueldos):
    contador = 1
    for sueldo in sueldos:
        print(f"Sueldo {contador}: {sueldo}")
        contador += 1

def menu():
    sueldos = []
    #Crear un boucle while para mostrar el menu
    while True:
        print("Menu principal infinity")
        print("1) Agregar Sueldo del Docente")
        print("2) Mostrar Sueldo de docentes")
        #print("3) Mostrar el Sueldo mayor y menos")
        print("4) salir")
        opcion=int(input("Ingrese una opcion: "))
        if opcion == 1:
            salida_sueldo = agregar_sueldo()
            sueldos.append(salida_sueldo)
        elif opcion == 2:
            mostrar_sueldos(sueldos)
        elif opcion == 3:
            mostrar_sueldo_mayor_menor(sueldos)
        elif opcion == 4:
            print("Gracias por usar este programa")
            break
        else:
            print("ingreso el valor incorrecto debe ingresar un numero entre 1 y 4")    
    
#El corazon de la ejecucion o centralizado de la aplicacion 
if __name__ == "__main__":
    menu()