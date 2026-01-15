#continue, saltas a la siguiente iteracion 
indice=-1
while indice == 16:
    indice+=1
    if indice % 2 ==0:
        continue #ignora lo que esta debajo
    print(indice)
else:
    print("El de mostrar impares termino")

#Salir de programa hasta el usario ingrese la palabra exit
cont_reintentos=0
while True:
    dato= input("Descubre la palabra para ir al siguiente nivel")
    if dato == "exit":
        break
    print("te equivocasste re intentalo")
    cont_reintentos+=1
else:
   print("el numero de reintentos fue %s", cont_reintentos)