#Estructura de datos que almacena información
#Caracteristicas
#Se escribe con llaves
#cada clave es unica
#permite acceder mas rapido a los valores y es ligero


#ejemplo de diccionario
#. variable ={clave, valor,
#     clave: valot
#. }

#acceder al valor del diccionario

persona ={
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "medellin",
    "profesion": "ingemiero"
}

print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
print(persona["profesion"])
#prin(personal["nombre_completo"]) si no existr la clave da error
#tambien puedo mofdificar el valor de cualquier clave
print("modificacion valor de la clave nombre")
persona["nombre"]= "Pedro"
print(persona["nombre"])
#agregar un nuevo par clave-valor
print("agregar un par clave-valor")
persona["nombre_completo"] = "Pedro Perez"
print(persona["nombre_completo"])

#eliminar clave-valor
print("eliminar clave-valor")
print(persona)

for clave in persona:
    print(f"clave: {clave}")

#ver los valores
for valor in persona.values():
    print(f"valor:{valor}")

print("ver completo")

for clave, valor in persona.items():
    print(f"clave: {clave}, valor: {valor}")

#no es obligatorio desde un inicio definir el diccionario con todas las claves

empleado = {}
print("diccionario vacio")
print(empleado)
empleado("nombre") = input("nombre :")
