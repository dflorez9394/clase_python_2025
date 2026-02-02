# Registro de usuario 

# Entrada de datos
nombre_completo = input("Ingrese su nombre completo: ").strip()
edad = int(input("Ingrese su edad: "))
pais = input("Ingrese su país de residencia: ").strip().title()
doc_identidad = input("¿Tiene documento de identidad? (s/n): ").strip().lower()
terminos = input("¿Acepta los términos y condiciones? (s/n): ").strip().lower()

# Lista de países permitidos
paises_permitidos = ["Colombia", "México", "Argentina", "España"]

print("\n--- RESULTADO DEL REGISTRO ---")
if (
    edad >= 18
    and pais in paises_permitidos
    and doc_identidad == "s"
    and terminos == "s"
):
    print(f"Registro exitoso. Bienvenido/a, {nombre_completo} 🎉")
else:
    print("Registro rechazado: no cumple con todos los requisitos.")
