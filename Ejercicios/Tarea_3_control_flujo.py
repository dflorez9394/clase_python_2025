from datetime import datetime

# Ingreso de datos
nombre = input("Ingresa tu nombre: ").strip()
apellido = input("Ingresa tu apellido: ").strip()
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ").strip()
frase_favorita = input("Ingresa tu frase favorita: ").strip()

# Procesamiento 
anio_actual = datetime.now().year
anio_100 = anio_actual + (100 - edad)
diferencia_50 = abs(edad - 50)

# Salida 
print("\n--- RESULTADOS ---")

# Nombre completo
print(f"Nombre completo: {nombre} {apellido}")

# Frase favorita en distintos formatos
print("\nFrase favorita:")
print(f"Mayúsculas: {frase_favorita.upper()}")
print(f"Minúsculas: {frase_favorita.lower()}")
print(f"Título: {frase_favorita.title()}")

# Cantidad de caracteres
print(f"\nCantidad de caracteres de la frase: {len(frase_favorita)}")

# Año en que cumplirá 100 años
print(f"Año en que cumplirá 100 años: {anio_100}")

# Diferencia entre edad y 50
print(f"Diferencia entre su edad y 50: {diferencia_50}")
