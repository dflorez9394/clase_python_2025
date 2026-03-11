import csv, os
from country import Country

class CountryRepository:
    def __init__(self, csv_file='countries.csv'):
        self.csv_file = csv_file
        self.countries = []
        self.load_from_csv()

    def load_from_csv(self):
        if os.path.exists(self.csv_file):
            with open(self.csv_file, newline='', encoding='utf-8') as f:
                reader = csv.reader(f, delimiter='|')
                self.countries = [Country.from_csv_row(row) for row in reader]
        else:
            self.countries = []

    def save_to_csv(self):
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            for country in self.countries:
                writer.writerow(country.to_csv_row())

    def add_country(self, country):
        if not any(c.name.lower() == country.name.lower() for c in self.countries):
            self.countries.append(country)
            self.save_to_csv()
            return True
        return False

    def find_by_name(self, name):
        for country in self.countries:
            if country.name.lower() == name.lower():
                return country
        return None
