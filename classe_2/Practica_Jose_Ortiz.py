'''
Ejercicio Enunciado
Crear un programa que controle el acceso a una zona restringida.
Datos de entrada
El usuario debe ingresar la siguiente información:
Edad
¿Tiene permiso especial? (Sí / No)
¿Es empleado? (Sí / No)
¿Está vetado? (Sí / No)
Reglas de acceso
El usuario puede ingresar a la zona restringida solo si se cumplen todas las siguientes condiciones:
No está vetado, y
Es mayor de edad, y
Tiene un permiso especial o es empleado.
Si alguna de estas condiciones no se cumple, el acceso debe ser denegado.'''

print("Control de Acceso a Zona Restringida")
print("\tFavor ingresar los siguientes datos al formulario")

#variables de entrada
nombre_empleado = input("Ingrese su nombre de empleado: ")
edad = int(input("Ingrese su edad: ").strip())
permiso_especial = ""
es_empleado = ""
es_vetado = ""

while edad < 0:
    try:
        edad = int(input("Ingrese su edad: ").strip())
        break
    except ValueError:
        print("Digita una edad valida")

while permiso_especial not in ("s", "n"):
    permiso_especial = input("Cuenta con permiso especial (s/n)?: ").strip().lower()

while es_empleado not in ("s", "n"):
    es_empleado = input("Es empleado de Skynet (s/n)?: ").strip().lower()

while es_vetado not in ("s", "n"):
    es_vetado = input("Tiene algun tipo de veto (s/n)?: ").strip().lower()

#condiciones para validación de acceso a zona restringida
if es_vetado == 's' and edad >= 18 and (permiso_especial == 's' or es_empleado == 's'):
    print(f"Hola {nombre_empleado} usted cuenta con autorización para ingresar a zona", end = "... ")
else: 
    print(f"Hola {nombre_empleado} usted no cuenta con autorización para ingresar a la zona. Acceso denegado", end = "... ")

print("Proceso de verificación finalizado")