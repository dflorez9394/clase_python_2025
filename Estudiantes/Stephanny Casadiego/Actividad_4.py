texto=input()
#Mostrar cada palabra del texto en una li­nea diferente.
for palabra in texto.split():
    print(palabra)
#Contar cuantas palabras tiene el texto.
print("\nEl texto tiene",len(texto.split()),"palabras")
#Contar cuÃ¡ntas veces aparece cada letra del texto usando un ciclo for y un diccionario.
contador_letras={}
for letra in texto.lower():
    if letra.isalpha():    
        if (letra not in contador_letras):
            contador_letras[letra] = 1
        else:
            contador_letras[letra] += 1
for clave, valor in contador_letras.items():
    print(clave, ":", valor)
#Contar cuantas palabras tienen mas de 5 letras.
contador_palabras = 0
for palabra in texto.split():
    if len(palabra) > 5:
        contador_palabras += 1
print("las palabras que tienen mas de 5 letras son:",contador_palabras)
#Mostrar el texto en los siguientes formatos: Title, Mayusculas , Minusculas
print("Este es el texto en title:",texto.title())
print("Este es el texto en mayuscula:",texto.upper())
print("Este es el texto en minuscula:",texto.lower())









