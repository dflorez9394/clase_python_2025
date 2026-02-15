import requests

from Pokemon import Pokemon


class PokeAPIClient:
    #CONSTANTES
    BASE_URL = "https://pokeapi.co/api/v2"


    def get_by_name(self,name: str):
        name = name.strip().lower()#normalizar el name
        url = f"{self.BASE_URL}/pokemon/{name}"
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise ValueError(f"El nombre del pokemon no existe: {name}")
            data = response.json()
            # Debemos sacar los nombres de la lista
            # forma 1
            types_pokemon = []
            # for type in data["types"]:
            #    types_pokemon.append(type["type"]["name"])
            # forma 2
            # types_pokemon= [t["type"]["name"] for t in data["types"]]
            return Pokemon(
                pokemon_id=data["id"],
                name=data["name"],
                # types=types_pokemon
                # types=data["types"]["type"]["name"],#['ground' , 'rock']
                types=[t["type"]["name"] for t in data["types"]],
            )
        except requests.exceptions.RequestException as e:
           raise ConnectionError(f"Error al conectarse a el API {self.BASE_URL}")
        finally:
            print("Se ejecuto el metodo get_by_name")