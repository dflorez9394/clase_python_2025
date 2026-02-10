import requests

from Pokemon import Pokemon


class PokeAPIClient:


    def get_by_name(self,name: str):
        name = name.strip().lower()#normalizar el name
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.status_code != 200:
            print("error del servicio")
        data = response.json()
        #Debemos sacar los nombres de la lista
        for type in data["types"]:
            habilidad = type["type"]["name"]
            print(f"Pokemon {type}")
            print(f"hanilidad {habilidad}")
        return Pokemon(
            pokemon_id=data["id"],
            name=data["name"],
            types=data["types"]["type"]["name"],#['ground' , 'rock']
        )