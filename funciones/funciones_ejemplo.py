def sumar(valor1,valor2):
    return valor1+valor2

def calcular_precio_final(precio,iva):
    pago_iva= precio*iva
    return sumar(precio,pago_iva)
    
def saludar_usuario(name):
    print(f"Hola {name}")


def unificar_info_persona(nombre,apellido,edad,segundoNombre=""):
    return  f"Hola {nombre} {segundoNombre} {apellido} tu edad es {edad}"

print(unificar_info_persona(edad=30,apellido="Perez",nombre="Juan"))


def sumar_n_numeros(*precios):
   total=0
   for precio in precios:
       total+=precio
   return total

print(sumar_n_numeros(1,2,3,4,5,123,123,123,123,123,123,123,21,321))

#** kwargs => keyword permite recibir un numero indeterminado de argumentos qe son en forma de diccionario o clave valor

def mostrar_info(**diccuinario):
    for clave,valor in diccuinario.items():
        print(f"{clave}: {valor}")
        if(clave=="edad" and valor>18):
            print("es mayor de edad")
        else:
            print("enor de edad")

mostrar_info(nombre="Juan",apellido="Perez",edad=30)


#Cree un metodo que se encargue de sumar n numeros que indique el usuario sin utilizar las listas


#for i in range(3):
#    saludar_usuario("Juan")
#    precio = float(input("Ingrese el precio: "))
#    precio_final = calcular_precio_final(precio,0.19)
#    print("El precio final es: ", precio_final)

#crear un metodo que se encargue de unificar un correo electronico
def unificar_correo(**datos):
    return datos

print(unificar_correo(nombre="Juan",email="@gmail.com",status=True))
print("****")
perfil = unificar_correo(nombre="Juan",email="@gmail.com",status=True)
print(perfil)

#crear un metodo que se encargue de unificar un correo electronico
def registrar_usuario(nombre,*telefonos,**datos):
    print(nombre)
    print(telefonos)
    print(datos)

registrar_usuario("Juan",123456789,123456789,email="@gmail.com",status=True)

