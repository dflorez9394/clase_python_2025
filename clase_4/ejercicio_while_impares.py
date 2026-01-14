#continue, saltas a la siguiente iteracion 
indice=-1
while indice <16:
    indice+=1
    if indice % 2 ==0:
        continue #ignora lo que esta debajo
    print(indice)