numeros = ["2", 2 , "9.2" ,"1" , 10,100,"-10"]

lista_numeros = []
for n in numeros:
    lista_numeros.append(float(n))

lista_numeros.sort()
print(lista_numeros)