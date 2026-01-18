# Vamos a crear un programa que trabaje con datos de texto y números
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")
frase_favorita = input("Ingrese su frase favorita: ")

#año actual
from datetime import datetime

#1. nombre completo con f-string
print(f"Nombre completo: {nombre} {apellido}")

#2. Frase favorita
print("Frase favorita en mayúsculas:", frase_favorita.upper())
print("Frase favorita en minúsculas:", frase_favorita.lower())
print("Frase favorita en formato título:", frase_favorita.title())

#3. Cantidad de caracteres en frase favorita
print("Cantidad de caracteres de la frase:", len(frase_favorita))

#4. Año en el que cumplira 100 años
anio_actual = datetime.now().year
anio_cien = anio_actual + (100 - edad)
print(f"Cumplirá 100 años en el año: {anio_cien}")

#5. La diferencia entre su edad y 50 usando la función abs()
diferencia = abs(edad - 50)
print(f"Diferencia entre su edad y 50: {diferencia}")





