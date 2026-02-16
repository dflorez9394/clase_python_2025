from country_api import CountryAPI
from repository import CountryRepository
from email_service import EmailService


def main():
    repo = CountryRepository()
    api = CountryAPI()

    name = input("Ingrese el nombre del país: (en ingles) ").strip()

    # Buscar primero en CSV
    countries = repo.load_countries()
    country = next(
        (c for c in countries if c.name.lower() == name.lower()),
        None
    )

    if country:
        print("País encontrado en archivo local.")
    else:
        print("Buscando pais en la API...")
        country = api.get_country(name)

        if not country:
            print("País no encontrado.")
            return

        repo.save_country(country)

    print(country)

    send = input("¿Desea enviar esta información por correo? (si/no): ").lower()

    if send == "si":
        email_service = EmailService(
            sender_email="stephannycasadiego@gmail.com",
            app_password="pmgzqfvfxycexhwg"
        )

        email_service.send_country(
            "daniel.florez@aulamatriz.edu.co",
            country
        )


if __name__ == "__main__":
    main()
