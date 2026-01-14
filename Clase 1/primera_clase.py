#print es una función de salida
# Sirve para mostrar información en la consola
#Todo lo que este dentr de " " es un string (texto)
from re import A


print("Hola Mundo")
print("Bienvenidos a Python")
# 1 . Escribo mi archivo .py
# 2 . Lo ejecuto con python3
# 3 . Convierte el codigo a bytecode
# 4 . Ejecuta el bytecode en la maquina virtual de Python
# 5 . El bytecode es independiente del sistema operativo
# 6 .timpo real

# una variable => es algo que tiene un valor  
# es un caracteristica, es algo que almacena informacion
# Una viariable es como caja que puede almacenar  algo y le damos un nombre

#estructura de una variable en python
#nombre_variable = valor
nombre= "Juan" # string
edad = 23 # integer
altura = 1.75 # float
es_estudiante = True # boolean

#Reglas para nombrar variables:
# 0. Debe comenzar con una letra o un guion bajo
# 1. Solo pueden contener letras, números y guiones bajos
# 2. No pueden comenzar con un número
# 3. No pueden contener espacios
# 4. No pueden ser palabras reservadas de Python (como if, for, while, def, class, etc.)
# 5.* las variables se recomeinda que sean en minuscula y contenga guion bajo para separar palabras
#Ejemplo

nombre_completo = "Juan Pérez"
_daniel = "Daniel"
#diferenciar las variables y no con mayusculas


#tipos de datos en Python
# int -> enteros 10 
# float -> decimales 10.5
# str -> cadenas de texto "Hola"
# bool -> booleanos (True o False) featureFlags Experimentos
# list -> listas [1, 2, 3] 
# tuplas -> ("Daniel", "florez", 50, "Medellin", true)
# dict -> diccionarios {"nombre": "Daniel", "edad": 50}

#Guarda una referencia a un objeto en memoria
cantidad=10
cantidad=20
#Asgnaicones

total_juguetes, total_camisetas, total_libros = 10, 20, 30
print(total_juguetes, total_camisetas, total_libros)


x=y=z=total_juguetes
print(x, y, z)

#ejemplo de modificar tipos de datos
x = "Nuevo valor"
print(x)

print("V******")
a = 5
b=a
print(a)
print(b)
print(type(b))
b= x;
print(b)
print(type(b))

print("Modificación de listas:")
list1 = [1, 2, 3]
list2 = list1
print(list2)
list2.append(4)
print(list2)
print(list1)
list1.append(5)
print(list2)
print(list1)

#inmutables - los tipos de datos simples (int, float, str, bool,) son inmutables
# mutables - las listas list dict set(*)
#  nombre_variable:tipo_dato = valor;
list3:list  = list1.copy()
print("Modificación de listas:")
list3.append(6)
print(list3)
print(list1)

#buenas practicas
# los nombre deben ser descriptivos y en minúsculas con guion bajo
# snike_case
# evitar nombres muy cortos o muy largos
#usar un lenguaje neutral o unificado

estudiante = "daniel"
estudiantes = ["daniel", "juan", "maria"]

#cuando yo uso matusculas  , solamente cuando son constantes
PI = 3.1416
MAX_SIZE = 100
