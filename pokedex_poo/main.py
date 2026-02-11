import requests as rq# una libreria que nos trae funcionalidades a nuestro codigo

from pokedex_app import PokedexApp


def main():
    app = PokedexApp()
    app.run()
if __name__ == '__main__':
    main()