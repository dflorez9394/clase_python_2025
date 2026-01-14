# Pedir al usuario si esta suscrito a un servicio premium de netlix
# Si no esta suscrito , mostramos un mensaje indicando que debe suscribirse o invindolos a la version gratuita
#Si , No ,  12312 ,$#"!$!"$%
suscrito = input("¿Estás suscrito? (s/n): ").strip().lower()

if not (suscrito == "s"):
    print("No estás suscrito. ¿Deseas unirte?")
else:
    print("Gracias por tu suscripción.")

print("************************")
if suscrito == "s":
    print("Gracias por tu suscripción.")
elif suscrito == "n":
    print("No estás suscrito. ¿Deseas unirte?  nuestro canal")
else:
    print("entrada no valida , debe ser (s/n)")

#Buenas practicas
# Tener encuenta la identacion de nuestro programa
#cuando comparamos cadenas no olvidar usar  las comillas cuando se requieran
color="rojo"
if color == "rojo":
    print("El color es rojo")

# solo podemos usar un else por bloque de validacion

if color == "rojo":
    print("El color es rojo")
else:
    print("El color no es rojo")