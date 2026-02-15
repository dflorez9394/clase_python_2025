import json
from Pokemon import Pokemon


class JsonStorage:
    def __init__(self, filename:str = "favoritos.json"):
        self.filename = filename

    #Guardar
    def save(self, listPokemon: list[Pokemon])->None:
        data =   [pokemon.to_dict() for pokemon in listPokemon]
        with open(self.filename, "w" , encoding="utf-8") as file:
            json.dump(data,file, indent=2,ensure_ascii=False)
    #consultar CARGAR POKEMONES TODO PARA HACER EN CASA