class Telefono:
    #atributos
    marca="Sony"
    modelo="Xperia 1 IV"
    color="Plateado majenta"
    precio=100
    bateria=100

    def encender(self):
        print("Encendiendo...")
    def llamar(self, numero):
        if  len(numero) == 10:
        #if len(str(numero)) == 10:
            print(f"Llamando al {numero}...")
        else:
            print("Debe ingresar un numero de telefono")
    def estado_bateria(self):
        return self.bateria

    def ajustar_bateria(self,bateria):
        self.bateria = bateria



ios = Telefono()
print("Estado inicial de la bateria:")
print(ios.bateria)

print("**************** EStado nuevo d ela bateria *")
ios.ajustar_bateria(20)
print(ios.bateria)
print("*****************")
print(ios.estado_bateria())
ios.encender()
ios.llamar("3102039485")



samsung = Telefono()
print(samsung.estado_bateria())
samsung.llamar("231231")

oppo = Telefono()
print(oppo.estado_bateria())
oppo.llamar("123123123")
