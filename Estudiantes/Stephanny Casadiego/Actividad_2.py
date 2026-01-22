#Crear un programa que ssimule el regitro de usuario como las que usan muchas paginas web
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
pais_de_residencia = input("Ingrese su pais de residencia: ").lower().strip().capitalize()
paises_validos = ("Colombia", "Mexico", "Argentina", "España")
documento = input("¿Tiene documento de identidad? (si / no): ").lower().strip()
terminos_y_condiciones = input("¿Acepta los terminos y condiciones? (si / no): ").lower().strip()

if (edad >= 18) and pais_de_residencia in paises_validos and documento == "si" and terminos_y_condiciones =="si": 
    print(f"Registro exitoso. ¡Bienvenido/a, {nombre}")
elif edad < 18:
    print("No puede registrarse porque es menor de edad.")
elif pais_de_residencia not in paises_validos:
    print("No puede registrarse porque su país no está permitido")
elif documento != "si":
    print("o puede registrarse porque no tiene documento de identidad")
elif terminos_y_condiciones != "si":
     print("No puede registrarse porque no acepta los términos y condiciones.")
else:
    print("No se puede realizar el registro ya que no cumple con las condiciones")
