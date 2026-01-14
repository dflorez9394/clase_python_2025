from calendar import prmonth


contador = 0
while contador < 10:
    print(contador)
    contador += 1


#incorrecta
#contador = 0
#while contador < 10:
#    print(contador)
print("**************")
#ejemplos , necesitamos que el usuario no pueda avanzar hasta que la contraseña sea correcta
password = ""

while password != "infinity": # la contraseña para ingresar es infinity
    password = input("ingresa la contraseña: ")
print("Bienvenido")
# crear condiciones logicas agrupadas o complejas

nota=int(input("ingresa la nota: "))
while nota < 0 or nota > 5:
    nota=int(input("ingresa la nota: "))


#Salir del ciclo por medio de un break

while True:
    password = input("ingreasa salir: ")
    if password == "salir":
        break
print("Bienvenido")



#Ccontinue

