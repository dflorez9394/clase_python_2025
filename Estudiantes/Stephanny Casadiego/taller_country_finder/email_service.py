import smtplib
from email.message import EmailMessage


class EmailService:
    def __init__(self, sender_email, app_password):
        self.sender_email = sender_email
        self.app_password = app_password

    def send_country(self, receiver_email, country):
        msg = EmailMessage()
        msg["Subject"] = f"Información del país: {country.name}"
        msg["From"] = self.sender_email
        msg["To"] = receiver_email

        content = str(country)

        msg.set_content("Encuentre adjunto la información del país.")

        filename = "country_info.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        with open(filename, "rb") as file:
            msg.add_attachment(
                file.read(),
                maintype="text",
                subtype="plain",
                filename=filename
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.sender_email, self.app_password)
            smtp.send_message(msg)

        print("Correo enviado correctamente.")
