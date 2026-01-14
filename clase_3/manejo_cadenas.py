from pydoc import text


texto = "     hola, soy. daniel xD      "
print(texto[0])
print(texto[3])
##print(texto[100]) si buscamos una posicion que no existe, nos dara error

print(texto[-1])
print(texto[-2])
#trabajar con las subcadenas
#[INICIA:TERMINA]
print(texto[0:3])
print(texto[4:5])
print(texto[6:])
print(texto[:6])

print("******")

print(texto.upper()) #pasar todo mayusculas 
print(texto.lower()) #pasar todo minusculas
print(texto.capitalize()) #pasar la primera letra en mayuscula
print(texto.title()) #pasar la primera letra de cada palabra en mayuscula
print(texto.strip()) #quitar los espacios en blanco al inicio y al final
print(texto.lstrip()) #quitar los espacios en blanco al inicio y al final
print(texto.rstrip()) #quitar los espacios en blanco al inicio y al final
print(texto.replace(' ','*'))
#daniel;florez;lopez;celular
formato = "07;enero;2025"
print(formato.split(";"))
fehca = formato.split(";")
#unir cadenas de texto que tengan entre ellas un separar
print(";".join(fehca))
#validaciones en python str
print(texto.startswith(" "))
print(texto.endswith(" "))
#busqueda
print(texto.find("soy"))

#imprimir por consola 
