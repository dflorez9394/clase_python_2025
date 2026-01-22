"""Analizador de texto"""
"""Escribe un programa en Python que le pida al usuario ingresar un texto y luego realice lo siguiente"""
"""1. Mostrar cada palabra del texto en una linea diferente"""

texto = input("Ingrese un texto para analizar: ")

palabras = texto.split()

for palabra in palabras:
    print(palabra)

print(f"La cantidad de palabras en el texto es: {len(palabras)}")

texto_min = texto.lower()
letras_conteo = {}

for caracter in texto_min:
    if 'a' <= caracter <= 'z':
        if caracter in letras_conteo:
            letras_conteo[caracter] += 1
        else:
            letras_conteo[caracter] = 1


print("Conteo de letras")
for letra, cantidad in letras_conteo.items():
    print(f"{letra}: {cantidad}")


contador_palabras_largas = 0

for palabra in palabras:
    if len(palabra) > 5:
        contador_palabras_largas += 1

print(f"Palabras largas de mas de 5 letras: {contador_palabras_largas}")

print(f"texto en title: {texto.title()}")
print(f"texto en mayusculas: {texto.upper()}")
print(f"texto en minusculas: {texto.lower()}")
