print(" ** PAGINA WED **")

nombre = input("Ingrese su nombre completo: ")
edad= int(input("Ingrese su edad: "))
pais = input("Ingrese su pais de residencia: ")
documento = input("Usted tiene documento de Identidad (Si/No): ").lower
condiciones = input("Usted acepta las condiciones (Si/No): ").lower 


if edad <= 18:
    print("No puede registrarse porque es menor de edad.")

elif pais not in ["Colombia", "España", "Mexico", "Argentina"]:
    print("No puede registrarse porque su país no está permitido.")

elif documento == "si" :
    print("No puede registrarse porque no tiene documento de identidad.")

elif condiciones == "si":
    print("No puede registrarse porque no aceptó los términos y condiciones.")

else:
    print(f"¡Registro exitoso {nombre}! Bienvenido.")


