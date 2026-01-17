print("** ANALIZAR TEXTO **")

#1
texto = input("Ingrese un texto: ")

for texto in texto.split():
    print(texto)

#2 
contar = input("Ingrese un texto: ")

for contar in contar:
    print(contar)

#3
numerar = input("Ingrese un texto: ").lower()

conteo = {}

for letra in numerar:
    if letra.isalpha():          
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1

for letra, cantidad in conteo.items():
    print(f"{letra}: {cantidad}")

#4

texto = input("Ingrese un texto: ")

contador = 0

for palabra in texto.split():
    contador += 1

print(f"Cantidad de palabras: {contador} ")

#5

titulo = input("Ingrese un titulo")

print(f"El titulo es {titulo}".lower())
print(f"Mi frase es {titulo}".upper())
print(titulo.title())







