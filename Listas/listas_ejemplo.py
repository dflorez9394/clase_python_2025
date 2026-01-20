frutas = ["manzana", "banana", "naranja",]
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[-1])

frutas[1]="Roabanos"
print(frutas)



abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#en dos lineas imprimir el contenido de la lista
for ab in abc:
    print(ab)
    
print("***************************")

# Ejercicio notas
notas = [5, 3, 2, 1]

suma_notas = sum(notas)
promedio_notas = suma_notas / len(notas)
cantidad_notas = len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print("Notas:", notas)
print("Suma total:", suma_notas)
print("Promedio:", promedio_notas)
print("Cantidad de notas:", cantidad_notas)
print("Nota máxima:", nota_maxima)
print("Nota mínima:", nota_minima)



print("*****Lista carros appnets")

listCar=[]

#Agregar un nuevo valor a mi lista append
listCar.append("Toyota")
listCar.append("Cupra")
listCar.append("BYD")
listCar.append(20)
print(listCar)

#Agregar un valor en una posicion espesifica
listCar.insert(3, "Ferrari")
listCar.insert(0, "Ferrari")
listCar.insert(20, "Ferrari")
print(listCar)
#Remover valores
listCar.remove("Ferrari")
print(listCar)
print("Removiendo valor 0")
listCar.pop(0)#cuando el pop tiene un dindice borra el valor del indice
listCar.pop()#cuando el pop no tiene indice borra el ultimo valor

print("Order listas")
numeros = [5, 2, 9, 1]
print(listCar)
numeros.sort()
print(numeros)

listCar.remove(20)
print(listCar)

listCar.sort()
print(listCar)
#
listCar.sort(reverse=True)
print(listCar)
#lista
marcas_telefono = ["IPHONE", "SAMSUNG", "IPHONE", "OPPO", "HUAWEI"]
marcas_telefono.reverse()
print(marcas_telefono)
print(marcas_telefono.count("IPHONE"))


marcas_telefono.sort()
print(marcas_telefono)
marcas_telefono.sort(reverse=True)
print(marcas_telefono)

print("CELAN*****")
marcas_telefono.clear()
print(marcas_telefono)
#


numeros = ["2", 2 , "9.2" ,"1" , 10,100,"-10"]
numeros.sort()