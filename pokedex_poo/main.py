import requests as rq# una libreria que nos trae funcionalidades a nuestro codigo

from Pokemon import Pokemon
from poke_api_client import PokeAPIClient


def main():
    nombre_pokemon = input("Ingrese el nombre del pokemon: ").strip().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = rq.get(url)
    if response.status_code != 200:
        print("El nombre del pokemon no existe")
        return
    data = response.json()
    print("Nombre del pokemon es: ", data["name"])
    print("ID del pokemon es: ", data["id"])
if __name__ == '__main__':
    pokemon = input("Ingrese el nombre del pokemon: ")
    pokemon_list =  PokeAPIClient().get_by_name(pokemon)
    pokemon_list.show_pokemon()
   # main()

#main => le corazon del proyecto que va ejecutar cada clase o metodo para solucionar el problema