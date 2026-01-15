#un diccionario es una estructura de datos que permite almacenar pares de clave-valor
#Caracteristicas:
#   - Se escribe con las llaves {}
#   - cada clave es unica
#.  -Permite acceder mas rapido a los vales y es ligero
#.  -Los valores pueden ser cualquier tipo de dato

# Ejemplo de diccionario
#. variable = {clave: valor , 
#    clave: valor
#. }
#
#
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Medellin",
    "profesion": "Ingeniero",
}
#acceder a un valor del diccionario
print(persona["nombre"])
print(persona["edad"])
print(persona["ciudad"])
print(persona["profesion"])
#print(persona["nombre_completo"]) si no existe la clave, da error
#tamben puedo modificar el valor de cualquier clave
print("modificacion valor de la clave nombre")
persona["nombre"] = "Pedro"
print(persona["nombre"])
#agregar un nuevo par clave-valor
print("agregar un nuevo par clave-valor")
persona["nombre_completo"] = "Pedro Perez"
print(persona["nombre_completo"])

#eliminar un par clave-valor
print("eliminar un par clave-valor")
del persona["nombre_completo"]
print("diccionario despues de eliminar nombre_completo")
print(persona)

for clave in persona:
    print(f"clave: {clave}")

#ver los valores
for valor in persona.values():
    print(f"valor: {valor}")

print("ver completo")

for clave, valor in persona.items():
    print(f"clave: {clave}, valor: {valor}")

print("====================DINAMICO============")
#no es obligatorio desde un inicio definir el diccionario con todas las claves
emplado = {}
print("diccionario vacio")
print(emplado)
emplado["nombre"] = input("nombre : ")
emplado["edad"] = int(input("edad : "))
emplado["ciudad"] = input("ciudad : ")
emplado["profesion"] = "Ingeniero"
print("diccionario con valores")
print(emplado)
#