# Creaar un sistema de calificacion automatico
# el usuario debe ingresar el nombre del estudiante y la nota final
# si el estudinante tiene una nota entree 90 y 100 es excelente
# si el estudinante tiene una nota entree 80 y 89 es muy bien
# si el estudinante tiene una nota entree 70 y 79 es bien
# si el estudinante tiene una nota entree 60 y 69 es regular
# si el estudinante tiene una nota entree 50 y 0 es reprueba
# Constantes de mensajes
EXCELENTE = "excelente!"
MUY_BIEN = "muy bien"
BIEN = "bien"
REGULAR = "regular"
REPRUEBA = "reprueba"

nombre = input("Ingresa el nombre del estudiante: ")
while True:
    try:
        nota = int(input("Ingresa tu nota (0-100): "))
        if 0 <= nota <= 100:
            break
        else:
            print("Error: la nota debe estar entre 0 y 100")
    except ValueError:
        print("Error: debes ingresar un número entero entre 0 y 100")

if nota >= 90:
    resultado = EXCELENTE
elif nota >= 80:
    resultado = MUY_BIEN
elif nota >= 70:
    resultado = BIEN
elif nota >= 60:
    resultado = REGULAR
else:
    resultado = REPRUEBA

print(f"{nombre} tiene una nota de {nota} y es {resultado}")

