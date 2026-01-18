#Guarda una referencia a un objeto en memoria
cantidad=10
cantidad=20
#asignaciones
total_juguetes, total_camisetas, total_libros = 10, 20, 30
print(total_juguetes,total_camisetas, total_libros)

x=y=z=total_juguetes
print(x, y, z)

#ejempli de modificar tipos de datos
x = "Nuevo valor"
print(x)

print("V*******")
a = 5
b=a
print(a)
print(b)
print(type(b))

print("modificacón de listas")
list1 = (1, 2, 3)
list2 = list1
print(list2)
list2.append(4)
print(list2)
print(list1)
list.append(5)
print(list2)
print(list1)

##inmutables- los tipos de datos simples (int, float, str, bool,) son inmutables
#mutables - las listas list direct set(*)
#tipo_dato: nombre_variable = valor;

list3:list = list1.copy()
print("modificación de listas")
list3.append(6)
print(list3)
print(list1)

#buenas practicas
#los nombres deber ser descriptivos y en minúsculas con guion bajo
#snike_case
#evitar nombres muy cortos o muy largos
#usar lenguaje neutral o unificado

estudiante = "daniel"
estudiantes = ("daniel" "juan", "maria")

 