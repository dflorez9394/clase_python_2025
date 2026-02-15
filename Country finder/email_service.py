import smtplib, os
import csv
from email.message import EmailMessage
from country import Country

class EmailService:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_country_info(self, recipient_email, country: Country):
        msg = EmailMessage()
        msg['Subject'] = f"Información de país: {country.name}"
        msg['From'] = self.sender_email
        msg['To'] = recipient_email
        msg.set_content(f"Adjunto información de {country.name}")

        temp_file = f"{country.name}.csv"
        with open(temp_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter='|')
            writer.writerow(['Nombre', 'Capital', 'Región', 'Población', 'Monedas'])
            writer.writerow(country.to_csv_row())

        with open(temp_file, 'rb') as f:
            msg.add_attachment(f.read(), maintype='text', subtype='csv', filename=temp_file)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.sender_email, self.sender_password)
                smtp.send_message(msg)
            print(f"Correo enviado a {recipient_email} con la info de {country.name}")
        except Exception as e:
            print(f"No se pudo enviar el correo: {e}")
        finally:
            os.remove(temp_file)
