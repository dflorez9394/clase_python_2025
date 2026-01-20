"""Ejercicio de práctica
Vamos a crear un programa que simule un registro de usuario, como los que se usan en muchas páginas web.
El programa debe pedirle al usuario los siguientes datos:
Nombre completo
Edad
País de residencia
Si tiene documento de identidad (responder s o n)
Si acepta los términos y condiciones (responder s o n)
Después de pedir los datos, el programa debe usar if, elif y else, junto con operadores lógicos como and, para decidir si el usuario puede registrarse o no.
Reglas para permitir el registro:
Debe tener 18 años o más
Debe vivir en uno de estos países: Colombia, México, Argentina o España
Debe tener documento de identidad
Debe aceptar los términos y condiciones
Si el usuario no cumple alguna de estas condiciones, el programa debe mostrar un mensaje explicando por qué no puede registrarse.
"""

print("REGISTRO DE USUARIO")

nombre_completo = input("Ingresa tu nombre completo: ").lower().strip()
edad = int(input("Ingresa tu edad: ").lower().strip())
pais_residencia = input("Ingresa tu pais de residencia: ").lower().strip()
documento_identidad = ""
terminos_condiciones = ""

while edad < 0:
    edad = int(input("Ingrese su edad (no se aceptan valores negativos): "))
    break

while documento_identidad not in ("s","n"):
    documento_identidad = input("Indique si tiene documento de identidad (s/n): ").lower().strip()

while terminos_condiciones not in ("s","n"):
    terminos_condiciones = input("Indique si aceptas los terminos y condiciones (s/n): ").lower().strip()

if not edad >= 18 and pais_residencia not in ("colombia", "méxico", "argentina","españa") and documento_identidad == "n" and terminos_condiciones == "n":
    print("No puede proceder con el registro ya que es menor de edad, no reside en los paises permitidos para registro, no posee documento de identidad y tampoco aceptó los terminos y condiciones")
elif not edad >= 18 and pais_residencia not in ("colombia", "méxico", "argentina","españa") and documento_identidad == "n":
    print("No puede proceder con el registro ya que es menor de edad, no reside en los paises autorizados para proceder con el registro tales como Colombia, México, Argentina o España, y no posee documento de identidad")
elif not edad >= 18 and pais_residencia not in ("colombia", "méxico", "argentina","españa"):
    print("No puedo proceder con el registro, ya que es menor de edad y no reside en los paises autorizados")
elif not edad >= 18:
    print("No puede proceder con el registro ya que el usuario es menor de edad")
elif pais_residencia not in ("colombia", "méxico", "argentina","españa"):
    print("No puede proceder con el registro al no residir en alguno de los paises autorizados")
elif documento_identidad == "n":
    print("No puede proceder con el registro ya que el usuario no tiene documento de identidad")
elif terminos_condiciones == "n":
    print("No puede proceder con el registro, ya que no aceptó terminos y condiciones")
else:
    print("Puede proceder con el registro")
    print(f"El usuario {nombre_completo.title()} con {edad} años de edad, puede proceder con el registro")
