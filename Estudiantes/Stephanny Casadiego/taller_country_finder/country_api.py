import requests
from country import Country


class CountryAPI:
    BASE_URL = "https://restcountries.com/v3.1/name/"

    def get_country(self, name):
        response = requests.get(f"{self.BASE_URL}{name}")

        if response.status_code != 200:
            return None

        data = response.json()[0]

        return Country(
            name=data["name"]["common"],
            capital=data.get("capital", ["N/A"])[0],
            currency=list(data.get("currencies", {}).keys())[0]
            if data.get("currencies") else "N/A",
            region=data.get("region", "N/A"),
            population=data.get("population", "N/A")
        )
