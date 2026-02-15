from repository import CountryRepository
from api import CountryAPI
from email_service import EmailService

class CountryFinderApp:
    def __init__(self):
        self.repo = CountryRepository()
        self.api = CountryAPI()
        self.email_service = EmailService('jdff0512@gmail.com', 'miakvuhwmwtsbfma') # Reemplazar con el correo y contraseña de doble verificación, no funciona con passwrd regular"

    def menu(self):
        while True:
            print("\n--- Country Finder ---")
            print("1. Buscar país")
            print("2. Mostrar todos los países guardados")
            print("3. Enviar país por correo")
            print("4. Salir")
            choice = input("Opción: ")
            
            if choice == '1':
                self.buscar_pais()
            elif choice == '2':
                self.mostrar_paises()
            elif choice == '3':
                self.enviar_pais()
            elif choice == '4':
                break
            else:
                print("Opción inválida.")

    def buscar_pais(self):
        name = input("Ingrese el nombre del país: ")
        country = self.repo.find_by_name(name)
        if country:
            print("✅ País encontrado en local:")
            print(country)
        else:
            print("🌐 Consultando API...")
            country = self.api.get_country_by_name(name)
            if country:
                print("✅ País encontrado en API:")
                print(country)
                self.repo.add_country(country)
            else:
                print("❌ País no encontrado.")

    def mostrar_paises(self):
        if not self.repo.countries:
            print("No hay países guardados.")
        else:
            for c in self.repo.countries:
                print(c)
                print("-"*30)

    def enviar_pais(self):
        name = input("Ingrese el nombre del país a enviar: ")
        country = self.repo.find_by_name(name)
        if country:
            recipient = input("Correo destinatario: ")
            self.email_service.send_country_info(recipient, country)
        else:
            print("País no encontrado en registros locales.")

if __name__ == "__main__":
    app = CountryFinderApp()
    app.menu()

