# Sistema de calificación 
try:
    nombre = input("Ingrese el nombre del estudiante: ").strip().lower()
    
    # Validar que se ingresó un nombre
    if not nombre:
        print("Error: Debe ingresar un nombre.")
    else:
        nota = float(input("Ingrese la nota final del estudiante (0-100): "))
        
        # Determinar la calificación según la nota
        if 90 <= nota <= 100:
            calificacion = "Excelente"
        elif 80 <= nota <= 89:
            calificacion = "Muy bien"
        elif 70 <= nota <= 79:
            calificacion = "Bien"
        elif 60 <= nota <= 69:
            calificacion = "Regular"
        elif 0 <= nota <= 59:
            calificacion = "Reprueba"
        else:
            calificacion = "Nota inválida (debe estar entre 0 y 100)"
        
        # Mostrar el resultado
        print(f"\n=== RESULTADO ===")
        print(f"Estudiante: {nombre}")
        print(f"Nota: {nota}")
        print(f"Calificación: {calificacion}")

except ValueError:
    print("Error: La nota debe ser un número válido.")