class Country:
    def __init__(self, name, capital, currency, region, population):
        self.name = name
        self.capital = capital
        self.currency = currency
        self.region = region
        self.population = population

    def to_csv_row(self):
        return [
            self.name,
            self.capital,
            self.currency,
            self.region,
            str(self.population)
        ]

    @classmethod
    def from_csv_row(cls, row):
        return cls(
            name=row[0],
            capital=row[1],
            currency=row[2],
            region=row[3],
            population=row[4]
        )

    def __str__(self):
        return (
            f"\nPaís: {self.name}\n"
            f"Capital: {self.capital}\n"
            f"Moneda: {self.currency}\n"
            f"Región: {self.region}\n"
            f"Población: {self.population}\n"
        )
