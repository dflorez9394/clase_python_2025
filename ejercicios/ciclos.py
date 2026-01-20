#1
frase = input("Ingresa una frase")
edad = input("Ingresa una edad")
anio = input("Ingresa tu fecha de nacimiento")

print(f"Frase en título: {frase.title()}")
print(f"Cantidad de caracteres: {len(frase)}")
print(f"Año en que cumplirá 100 años: {anio + (100 - edad)}")
print(f"Diferencia con 50: {abs(edad - 50)}")



#2
texto = "Me gusta aprender Python"

for palabra in texto.split():
    print(palabra)



#3
texto = input("Ingrese un texto: ").lower()

conteo = {}

for letra in texto:
    if letra.isalpha():          
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1

for letra, cantidad in conteo.items():
    print(f"{letra}: {cantidad}")



#4

texto = input("Ingrese un texto: ")

cantidad_palabras = len(texto.split())

print(f"Cantidad de palabras: {cantidad_palabras}")


#5
texto = input("Ingrese un texto: ")

contador = 0

for palabra in texto.split():
    contador += 1

print(f"Cantidad de palabras: {contador}")