nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su país de residencia: ").lower()
documento = input("¿Tiene documento de identidad? (si/no): ").lower()
terminos = input("¿Acepta los términos y condiciones? (si/no): ").lower()

paises_permitidos = ["colombia", "méxico", "argentina", "españa"]

if edad < 18:
    print("No puede registrarse porque es menor de edad.")
elif pais not in paises_permitidos:
    print("No puede registrarse porque su país no está permitido.")
elif documento != "si":
    print("No puede registrarse porque no tiene documento de identidad.")
elif terminos != "si":
    print("No puede registrarse porque no aceptó los términos y condiciones.")
else:
    print("Registro exitoso. ¡Bienvenido,", nombre + "!")
