import csv
import os
from country import Country


class CountryRepository:
    def __init__(self, filename="countries.csv"):
        self.filename = filename

    def load_countries(self):
        countries = []

        if not os.path.exists(self.filename):
            return countries

        with open(self.filename, newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter="|")
            for row in reader:
                countries.append(Country.from_csv_row(row))

        return countries

    def save_country(self, country):
        countries = self.load_countries()

        # Evitar duplicados
        if any(c.name.lower() == country.name.lower() for c in countries):
            print("El país ya está guardado en el CSV.")
            return

        with open(self.filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter="|")
            writer.writerow(country.to_csv_row())

        print("País guardado correctamente.")
