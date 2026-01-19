"""Vamos a crear un programa que trabaje con datos de texto y números.
El programa debe pedir al usuario:
Nombre
Apellido
Edad
Ciudad
Frase favorita
Luego debe mostrar lo siguiente:
El nombre completo usando f-strings
La frase favorita:
en mayúsculas
en minúsculas
en formato título
La cantidad de caracteres que tiene la frase
El año en el que la persona cumplirá 100 años
La diferencia entre su edad y 50 usando la función abs()"""

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")
frase_favorita = input("Ingresa tu frase favorita: ")

anio_actual = 2026

anio_100 = anio_actual + (100 - edad)
diferencia_50 = abs(edad - 50)

print(f"Nombre completo: {nombre} {apellido}")

print(f"Frase en mayusculas: {frase_favorita.upper()}")
print(f"Frase en minusculas: {frase_favorita.lower()}")
print(f"Frase en formato titulo: {frase_favorita.title()}")
print(f"Cantidad de caracteres: {len(frase_favorita)}")

print(f"Tendras 100 años en el año: {anio_100}")
print(f"Diferencia entre tu edad y 50 años: {diferencia_50}")