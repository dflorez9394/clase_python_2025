class Country:
    def __init__(self, name, capital, region, population, currencies):
        self.name = name
        self.capital = capital
        self.region = region
        self.population = population
        self.currencies = currencies

    def to_csv_row(self):
        return [self.name, self.capital, self.region, str(self.population), ','.join(self.currencies)]

    @staticmethod
    def from_csv_row(row):
        name, capital, region, population, currencies = row
        return Country(name, capital, region, int(population), currencies.split(','))

    def __str__(self):
        return f"Nombre: {self.name}\nCapital: {self.capital}\nRegión: {self.region}\nPoblación: {self.population}\nMonedas: {', '.join(self.currencies)}"
