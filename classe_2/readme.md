
¿Quenes la funcion input?

input es una funcion integrada en Python que permite leer datos desde la entrada estándar (teclado).
1. Se sugiere mostrar un mensaje claro al usuario para indicar qué se espera ingresar.
2. El sistema entra en un modo espera hasta que el usuario ingrese datos y presione Enter.
3. input por default siempre nos va retornar un string.


#Code Example
```python
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print(f"Hola {nombre}, tienes {edad} años.")
```


Casting

Es el proceso de convertir un tipo de dato a otro. En el caso de `input`, siempre retorna un string, pero podemos convertirlo a otro tipo usando funciones como `int()`, `float()`, etc.


Conversion  | funcion  | descripción
|------------|----------|------------|
| Texto -> Entero     | int() | `int("123")` |
|Texto -> Flotante (Decimal)  | float() | `float("123.45")` |
|Texto -> Booleano   | bool() | `bool("True")` |
|Texto -> Lista      | split | `"1,2,3".split(",")` |
|Entero -> Texto     | str() | `str(123)` |


[Header 1] Casting Explicito

Escribimos el tipo de variable que queremos obtener

ejmplo => list("hola")

[Header 1] Casting Implicito

es el que se obtiene por default por el interprete de Python

Ejemplo
2.5 => es un número de tipo float

# Flujo básico de un programa
1. Recibir datos del usuario
2. Procesar los datos (logica). <= infiere internamente aprender a aplicar la logia
3. Mostrar resultados (salida)

# End 
Por defecto print realiza un salto de línea, con el parámetro `end` podemos controlar ese comportamiento.

Por ejemplo:
```python
print("Hola", end=" ")
print("Mundo")
# Salida: Hola Mundo (misma línea)
```


# Separador sep

El parámetro `sep` en `print()` permite especificar el separador entre los argumentos.

Por ejemplo:
```python
print("Hola", "Mundo", sep=" - ")
# Salida: Hola - Mundo
```

También se puede combinar `sep` con `end`:
```python
print("Hola", "Mundo", sep=" - ", end="!\n")
# Salida: Hola - Mundo!
```

# La logica booleana

La lógica booleana es un sistema de lógica basado en dos valores: verdadero (True) y falso (False). Se utiliza para tomar decisiones en los programas.

## Operadores lógicos

- **and**: Devuelve True si ambas condiciones son verdaderas
- **or**: Devuelve True si al menos una condición es verdadera  
- **not**: Invierte el valor lógico

## Ejemplos

```python
a = True
b = False
```

Operaciones que se realizan para una validacion

| Operación | significado | Ejemplo |Resultado|
|-----------|-------------|---------|---------|
| == | Igual a | 5 == 5 | True|
| != | Diferente de | 3 != 3 | False|
| > | Mayor que | 5 > 3 | True|
| < | Menor que | 3 < 5 | True|
| >= | Mayor o igual que | 5 >= 5 | True|
| <= | Menor o igual que | 3 <= 5 | True|


Ejercicios de práctica:

Ejercicios de práctica:s
|expresion|resultado|
|10>5| TRUE|
|4==4| TRUE|
|7<3|FALSE|
|10!=9|TRUE|
|100>=100|TRUE|
|1000>1000|FALSE|




Ejercicio
Enunciado

Crear un programa que controle el acceso a una zona restringida.

Datos de entrada

El usuario debe ingresar la siguiente información:

Edad

¿Tiene permiso especial? (Sí / No)

¿Es empleado? (Sí / No)

¿Está vetado? (Sí / No)

Reglas de acceso

El usuario puede ingresar a la zona restringida solo si se cumplen todas las siguientes condiciones:

No está vetado, y

Es mayor de edad, y

Tiene un permiso especial o es empleado.

Si alguna de estas condiciones no se cumple, el acceso debe ser denegado.
