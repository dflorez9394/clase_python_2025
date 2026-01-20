edad = int(input("Ingrese su edad: "))

permiso = input("¿Tiene permiso especial? (Si/No): ").lower() == "si"
empleado = input("¿Es empleado? (Si/No): ").lower() == "si"
denegado = input("¿Tiene acceso denegado? (Si/No): ").lower() == "si"

if edad >= 18 and not denegado and (permiso or empleado):
    print("¡ACCESO PERMITIDO! Bienvenido")
else:
    print("¡ACCESO DENEGADO!")
