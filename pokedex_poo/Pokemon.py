class Pokemon:
    #constructor pokemon
    def __init__(self,pokemon_id: int, name: str,types: list[str]):
        self.id = pokemon_id
        self.name = name
        self.types = types

    def show_pokemon(self):
        print("--------POKEMON-------")
        print(f"ID del pokemon: {self.id}")
        print(f"Nombre: {self.name}")
        print(f"Tipo -->>: {self.types}")
        print(f"Tipo ----->:  {','.join(self.types)}")
    #metodo para convertir el objeto o la salida en formado JSON dict
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "types": self.types,
        }

    # @classmethod => una anotacion  @funcionalidadPython
    @classmethod
    def from_dict(cls,data: dict):
        return cls(
            pokemon_id=data["id"],#mapea le id del diccionario
            name=data["name"],#mape ale nombre
            types=data.get("type",[])#mapea los tipos
        )