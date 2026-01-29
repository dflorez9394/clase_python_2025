class Persona:
    ##atributos
    empelado=False
    #Constructor
    #__init__
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        print("Se creo un objeto")
    
    def __del__(self):
        print("Se destruyo un objeto")
        #Terminr la conexion con una base de datos
        #Cerrar archivos
        #Cerrar conexiones

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

daniel = Persona("Daniel", "Florez")
print(daniel.nombre)
print(daniel.apellido)
print(daniel)