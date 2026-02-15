#Es como si fuera una pokedex centralizada o punto centralizado
#importacones o agregar librerias
from json_storage import JsonStorage
from poke_api_client import PokeAPIClient
from Pokemon import Pokemon


class PokedexApp:
    def __init__(self):
        self.api = PokeAPIClient()
        self.storage = JsonStorage()
        self.favoritos:list[Pokemon]=[]   #TODO Agregar Cargar POKEMONES

    def run(self):
        while True:
            #menu
            self._menu()
            opcion = input("Selecciona una opcion: ").strip()
            if opcion == "1":
                self.atrapar()
            elif opcion == "2":
                print("listar pokemones") #TODO LISTAR POKEMONEs
            elif opcion == "3":
                print("guardar_pokemon en storage")
                self.guardar_pokemon()
            elif opcion == "4":
                print("salir")
                break # TODO CREAR METODO PARA SALIR
            else:
                print("Opcion no valida")

    def _menu(self):
        print("\n =======POKEDEX MENU ==========")
        print("1. Atrapar pokemon")
        print("2. listar pokemones")
        print("3. guardar pokemones ")
        print("4. Salir")

    def atrapar(self):
        nombre = input("Ingrese el nombre del pokemon: ")
        try:
            pokemon = self.api.get_by_name(nombre)
            print("el pokemon que se atrapo fue :")
            pokemon.show_pokemon()
            #TODO CREAR VALIDACION PARA PREGUNTAR SI LO DESEA AGREGAR
            #TODO EL POKEMON NE SE DEBERIA REPETIR
            self.favoritos.append(pokemon)
        except (ValueError, KeyError) as e:
            print("Error",e)

    ##TODO LISTAR POKEMONES
    def mostrar_pokemon(self):
            pass
    def guardar_pokemon(self):
        print("los pokemones se enviaron al centor pokemon")
        self.storage.save(self.favoritos)
    def salir(self):
        #TODO CUANDO LE DE SALIR DEBE GUARDAR LOS POKMONES EN EL STORAGE
        print("los pokemones se trsnfirieron donde el profesos super O")
        raise SystemExit