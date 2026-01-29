Clase y Objetos


Clase: La plantilla o template que consolida los elementos para crear un objeto , define las caracteristicas y comportamientos que tendra el objeto.
Atributos: Son las variables que almacen la informacion del objeto
Metodos: Son las funciones que definen el comportamiento del objeto
Contructor:es un metodo *especial* que se ejecuta al crear un objeto y se utiliza para inizializar los atributos del objeto


Estructura de una clase es :

class NombreClase:
    *Atributos
    atributo1
    atributo2
    atributo3
    
    *Constructos
    def __init__(self):
        pass
    
    *Metodos
    def metodo1(self):
        pass


Objeto: Es un elemento que tiene atributos(Caracteristicas) , metodos(accion) => comportamientos,
Un objeto es una instancia de una clase*
Un objeto es una agrupacion de datos y comportamientos relacionados.
Daots => atributos  
Acciones => metodos

En la vida real un objeto es como si fuera una "cosa" que conocemos.
Ejemplo: Un carro, una persona, un animal, etc.

Carro- Auto
Caracteristicas: COLOR , MARCA, MODELO, MOTOR,PUERTAS, tipo de combustible(Hibrido, Electrico, Gasolina)=>Atributos
Acciones ENCENDER, APAGAR, ACELERAR, FRENAR, pitar,=>Funciones o metodos

Persona 
Caracteristicas: NOMBRE, APELLIDO, EDAD, ALTURA, PESO
Acciones: CAMINAR, CORRER, SALTAR, AGACHARSE, LEVANTARSE, COMER, DORMIR,




self: es una palabra reservada de python
representa la instancia del objeto

para que sirve self?
- Para acceder a los atributos y metodos de la instancia
- Para retornar el objeto actual de una clase
- Sirve para modificar los atributos de la instancia
