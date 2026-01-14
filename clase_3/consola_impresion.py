# impresion por conosla utilizando el f-strings
name = "daniel"
edad = 100

print(f"Hola ñ{name} , tienes {edad} años.")

#.format 
print("Hola {} , tienes {} años.".format(name,edad))
print("Hola {1} , tienes {0} años.".format(name,edad))

print("Hola {name} , tienes {edad} años.".format(name="daniel",edad=25))


#usando el operador %
print("Hola %s , tienes %d años." % (name,edad))