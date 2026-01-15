#for variable in iterable:
#    codigo
#
#
#


frutas= ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la" ,fruta)

for i in range(len(frutas)):
    print(i, frutas[i])

print("================================")
#ejemplo 
for letter in "Hola":
    print(letter)
print("================================")
for i in range(10):
    print(i)
print("================================")
#mostrar los numeros imapres hasta el 13
for i in range(14):
    if i % 2 == 0:
        continue
    print(i)


# yo quiero los numeros impares desde el 20 hasta el 30
#rage(inicio,fin)
for i in range(20, 31):
    if i % 2 == 0:
        continue
    print(i)
#mostrar segun un salto entre numeros
#mostrar solo los numeros de dos en dos de 30 hasta 50
#range(inicio,fin,salto)
print("================================")   
for i in range(30, 51, 4):
    print(i)
#con el range inverso
#range(inicio,fin,-salto)
print("================================")   
for i in range(50, 30, -1):
    print(i)
else:
    print("Terminó el ciclo")


#Ejercicio pequeño
# apartir de una lista de palabras mostrar las palabras y mostrar aparte
#cada letra


print("==============EJERCICIOS==================")

palabras = ["HOLA", "Mundo", "python"]
for palabra in palabras:
    print(palabra) #HOLA
    for indice in range(len(palabra)):# HOLA => Buscar el tamaño  4  rango (0,1,2,3) => 4
        if indice != 2:
            print(palabra[indice].lower())
        else:
            print(palabra[indice].upper())
print("===================op-2=============")

for palabra in palabras:
    print(palabra) #HOLA
    for indice,letra in enumerate(palabra):
        if indice != 2:
            print(letra.lower())
        else:
            print(letra.upper())