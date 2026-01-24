"""Analizador de texto"""
"""Escribe un programa en Python que le pida al usuario ingresar un texto y luego realice lo siguiente"""
"""1. Mostrar cada palabra del texto en una linea diferente"""

import string

print("=== ANALIZADOR DE TEXTO ===")
texto = input("Por favor, ingresa un texto: ")

# Eliminar signos de puntuación
texto_limpio = texto.translate(str.maketrans('', '', string.punctuation))

print("\n--- Palabras del texto (una por línea) ---")
palabras = texto_limpio.split()

for palabra in palabras:
    if palabra:  # Verifica que la palabra no esté vacía
        print(palabra)

print(f"\nNúmero total de palabras: {len(palabras)}")