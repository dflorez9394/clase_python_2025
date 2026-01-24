# Programa para controlar el acceso a una zona restringida
def solicitar_edad():
    """Solicita y valida la edad del usuario."""
    while True:
        try:
            edad = input("\nIngrese su edad: ").strip()
            
            # Verificar que no esté vacío
            if not edad:
                print("Error: Debe ingresar un valor.")
                continue
            
            # Convertir a entero
            edad = int(edad)
            
            # Validar rango razonable
            if edad < 0:
                print("Error: La edad no puede ser negativa.")
                continue
            elif edad > 120:
                print("Error: Por favor ingrese una edad válida.")
                continue
            
            return edad
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


def solicitar_respuesta_si_no(pregunta):
    """Solicita y valida una respuesta Sí/No."""
    respuestas_validas_si = ["sí", "si", "s", "yes", "y"]
    respuestas_validas_no = ["no", "n"]
    respuestas_validas = respuestas_validas_si + respuestas_validas_no
    
    while True:
        respuesta = input(pregunta).strip().lower()
        
        # Verificar que no esté vacío
        if not respuesta:
            print("Error: Debe ingresar una respuesta (Sí/No).")
            continue
        
        # Verificar si es una respuesta válida
        if respuesta in respuestas_validas:
            return respuesta in respuestas_validas_si
        else:
            print("Error: Respuesta no válida. Por favor ingrese 'Sí' o 'No'.")


def evaluar_acceso(edad, tiene_permiso, es_empleado, esta_vetado):
    """Evalúa si se permite el acceso según las reglas establecidas."""
    es_mayor_edad = edad >= 18
    tiene_autorizacion = tiene_permiso or es_empleado
    puede_ingresar = not esta_vetado and es_mayor_edad and tiene_autorizacion
    
    return puede_ingresar, es_mayor_edad, tiene_autorizacion


def mostrar_resultado(puede_ingresar, esta_vetado, es_mayor_edad, tiene_autorizacion):
    """Muestra el resultado de la evaluación de acceso."""
    print("RESULTADO:")

    
    if puede_ingresar:
        print("\n✓ ACCESO PERMITIDO")
        print("Puede ingresar a la zona restringida.")
    else:
        print("\n✗ ACCESO DENEGADO")
        print("\nRazones del rechazo:")
        
        if esta_vetado:
            print("  - Está vetado")
        if not es_mayor_edad:
            print("  - No es mayor de edad (debe tener al menos 18 años)")
        if not tiene_autorizacion:
            print("  - No tiene permiso especial ni es empleado")



def main():
    """Función principal del programa."""
    print("CONTROL DE ACCESO A ZONA RESTRINGIDA")
    
    try:
        # Solicitar datos de entrada con validación
        edad = solicitar_edad()
        tiene_permiso = solicitar_respuesta_si_no("¿Tiene permiso especial? (Sí/No): ")
        es_empleado = solicitar_respuesta_si_no("¿Es empleado? (Sí/No): ")
        esta_vetado = solicitar_respuesta_si_no("¿Está vetado? (Sí/No): ")
        
        # Evaluar las condiciones de acceso
        print("\n" + "=" * 50)
        print("EVALUANDO CONDICIONES...")
        print("=" * 50)
        
        puede_ingresar, es_mayor_edad, tiene_autorizacion = evaluar_acceso(
            edad, tiene_permiso, es_empleado, esta_vetado
        )
        
        # Mostrar resultado
        mostrar_resultado(puede_ingresar, esta_vetado, es_mayor_edad, tiene_autorizacion)
        
    except KeyboardInterrupt:
        print("\n\n Programa interrumpido por el usuario.")
        print("=" * 50)
    except Exception as e:
        print(f"\n\n Error inesperado: {e}")
        print("Por favor, reinicie el programa.")
        print("=" * 50)


# Ejecutar el programa
if __name__ == "__main__":
    main()