print(" **TEXTO NUMERICO** ")

nombre = input("Ingrese su nombre: ")
apellido= input("Ingrese su apellido: ")
edad = int(input("Ingrese su Edad: "))
ciudad = input("Ingrese su ciudad: ")
frase = input("Ingrese su frase favorita: ")
anio = int(input("Ingrese el año "))

print(f"el nombre completo es {nombre} {apellido}")
print(f"Mi frase es {frase}".lower())
print(f"Mi frase es {frase}".upper())
print(frase.title())
print(f"Cantidad de caracteres: {len(frase)}")
print(f"Año en que cumplirá 100 años: {anio + (100 - edad)}")
print(f"Diferencia con 50: {abs(edad - 50)}")



