def validar_sueldos(sueldos):
    if len(sueldos) == 0:
        print("No hay sueldos registrados")
        return False#si sueldos es vacio o no tiene sueldos retorna un FALSE
    return True#Si tiene sueldos retorna un true
def agregar_sueldo():
    sueldo =float(input("Ingrese el sueldo: "))
    return sueldo
def mostrar_sueldos(sueldos):
    flagValidarSueldo = validar_sueldos(sueldos)
    print(f"Flag validar sueldo: {flagValidarSueldo}")
    if flagValidarSueldo:
        contador = 1
        for sueldo in sueldos:
            print(f"Sueldo {contador}: {sueldo}")
            contador += 1
        
def mostrar_sueldo_mayor_menor(sueldos):
    if len(sueldos) == 0:
        print("No hay sueldos registrados")
    else:
        print(f"Sueldo mayor: {max(sueldos)}")
        print(f"Sueldo menor: {min(sueldos)}")

def menu():
    sueldos = []
    #Crear un boucle while para mostrar el menu
    while True:
        print("Menu principal infinity")
        print("1) Agregar Sueldo del Docente")
        print("2) Mostrar Sueldo de docentes")
        print("3) Mostrar el Sueldo mayor y menor")
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