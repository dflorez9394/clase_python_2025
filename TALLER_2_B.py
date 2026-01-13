


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad de residencia: ").lower()
frase_favorita = input("Ingrese su frase favorita: ").lower()

nombre_completo = (f"{nombre} {apellido}")
#current_year = datetime.now().year
print("Nombre completo:", nombre_completo)
print(frase_favorita.upper())
print(frase_favorita.lower())
print(frase_favorita.title())
print(len(frase_favorita))
print(f"el año en que {nombre_completo} cumplirá 100 años de edad, es: {2026 + (100 - edad)}")
print(abs(edad - 50))