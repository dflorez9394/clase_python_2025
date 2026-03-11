import requests
from country import Country

class CountryAPI:
    BASE_URL = "https://restcountries.com/v3.1/name/"

    @staticmethod
    def get_country_by_name(name):
        try:
            response = requests.get(f"{CountryAPI.BASE_URL}{name}")
            response.raise_for_status()
            data = response.json()[0]
            currencies = list(data.get('currencies', {}).keys())
            capital = data.get('capital', ['Desconocida'])[0]
            region = data.get('region', 'Desconocida')
            population = data.get('population', 0)
            return Country(data['name']['common'], capital, region, population, currencies)
        except (requests.RequestException, IndexError, KeyError):
            return None
