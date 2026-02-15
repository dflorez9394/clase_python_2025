# ============================================================
#  TALLER POO PYTHON - "Country Finder"
#  Descripción: App de consola para buscar países usando API,
#               guardar en CSV y enviar por correo Gmail.
# ============================================================

# --- LIBRERÍAS (que vamos a usar) 
import requests      # Para hacer peticiones HTTP a la API de países
import csv           # Para leer y escribir archivos CSV
import os            # Para verificar si el archivo CSV ya existe
import smtplib       # Para conectarnos al servidor de correo Gmail
from email.message import EmailMessage  # Para construir el correo
from email.mime.multipart import MIMEMultipart  # Para correo con adjuntos
from email.mime.text import MIMEText             # Para el cuerpo del correo
from email.mime.base import MIMEBase             # Para el archivo adjunto
from email import encoders                        # Para codificar el adjunto


# ============================================================
# CLASE 1: Pais
# Representa un país con sus datos principales.
# En POO, una CLASE es como un molde para crear objetos.
# ============================================================
class Pais:  #---->  Clase:Es un molde/plantilla. No es un objeto real — es la definición de cómo será ese objeto
    # ----> No tenemos atributos de clase (compartidos por todos), solo de instancia (cada país tiene sus propios datos)
    def __init__(self, nombre, capital, moneda, poblacion, region): # ---->  __init__ es el CONSTRUCTOR:  inicializar atributos del objeto
        # 'self' representa el objeto que estamos creando
        # ----> Atributos de instancia porque cada país tendrá sus propios valores
        self.nombre    = nombre     # Nombre del país (ej: "Colombia")
        self.capital   = capital    # Capital del país (ej: "Bogotá")
        self.moneda    = moneda     # Moneda oficial (ej: "Peso colombiano")
        self.poblacion = poblacion  # Número de habitantes
        self.region    = region     # Continente o región (ej: "Americas")

    # Método para mostrar los datos del país en consola de forma bonita, con iconos etc
    def mostrar(self):
        print("\n" + "="*45)
        print(f"  🌍 PAÍS       : {self.nombre}")
        print(f"  🏙️  Capital    : {self.capital}")
        print(f"  💰 Moneda     : {self.moneda}")
        print(f"  👥 Población  : {self.poblacion:,}")  # :, pone separadores de miles
        print(f"  🌎 Región     : {self.region}")
        print("="*45)

    # Método para convertir el objeto a una fila del CSV (lista de valores)
    def a_fila_csv(self):
        # Retorna una lista con los datos del país en orden
        return [self.nombre, self.capital, self.moneda, self.poblacion, self.region]


# ============================================================
# CLASE 2: GestorCSV
# Se encarga de LEER y ESCRIBIR el archivo CSV.
# El CSV es como una tabla guardada en un archivo de texto.
# ============================================================
class GestorCSV:
    # El constructor recibe la ruta donde estará el archivo CSV
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo  # Ej: "paises.csv"
        self.cabeceras = ["nombre", "capital", "moneda", "poblacion", "region"]
        # Si el archivo NO existe, lo creamos con las cabeceras (encabezados)
        if not os.path.exists(self.ruta_archivo):
            self._crear_archivo()  # Llamamos al método privado para crearlo

    # Método PRIVADO (el _ al inicio indica que es solo para uso interno)
    # Crea el archivo CSV con los encabezados de columnas
    def _crear_archivo(self):
        with open(self.ruta_archivo, mode='w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter='|')  # Usamos | como separador
            escritor.writerow(self.cabeceras)         # Escribe la primera fila (cabeceras)
        print(f"  ✅ Archivo '{self.ruta_archivo}' creado automáticamente.")

    # Carga todos los países del CSV y los retorna como lista de objetos Pais
    def cargar_paises(self):
        paises = []  # Lista vacía donde iremos guardando los países
        with open(self.ruta_archivo, mode='r', encoding='utf-8') as f:
            lector = csv.DictReader(f, delimiter='|')  # DictReader lee cada fila como diccionario
            for fila in lector:
                # Creamos un objeto Pais con los datos de cada fila
                pais = Pais(
                    nombre    = fila["nombre"],
                    capital   = fila["capital"],
                    moneda    = fila["moneda"],
                    poblacion = int(fila["poblacion"]),  # Lo convertimos a número entero
                    region    = fila["region"]
                )
                paises.append(pais)  # Añadimos el objeto a la lista
        return paises  # Retornamos la lista completa

    # Guarda UN país en el CSV (agrega una nueva fila al final)
    def guardar_pais(self, pais):
        with open(self.ruta_archivo, mode='a', newline='', encoding='utf-8') as f:
            # mode='a' significa APPEND (agregar al final, no sobreescribir)
            escritor = csv.writer(f, delimiter='|')
            escritor.writerow(pais.a_fila_csv())  # Escribe la fila del país
        print(f"  💾 '{pais.nombre}' guardado en el CSV.")


# ============================================================
# CLASE 3: ClienteAPI
# Se encarga de comunicarse con la API de REST Countries.
# Una API es como un servicio web que nos da datos.
# ============================================================
class ClienteAPI:
    # URL base de la API (el {name} se reemplaza con el nombre del país)
    BASE_URL = "https://restcountries.com/v3.1/name/{name}"

    # Busca un país en la API y retorna un objeto Pais (o None si no se encuentra)
    def buscar(self, nombre_pais):
        # Armamos la URL completa reemplazando {name} con el nombre del país
        url = self.BASE_URL.format(name=nombre_pais)
        print(f"  🌐 Consultando API: {url}")

        try:
            # Hacemos la petición GET a la API (como abrir una URL en el navegador)
            respuesta = requests.get(url, timeout=10)  # timeout=10 espera máximo 10 segundos

            # Si el servidor respondió con error (ej: 404 = no encontrado)
            if respuesta.status_code == 404:
                print("  ❌ País no encontrado en la API.")
                return None  # Retornamos None para indicar que no hubo resultado

            # Convertimos la respuesta JSON a un diccionario de Python
            datos = respuesta.json()

            # La API retorna una LISTA; tomamos el primer resultado [0]
            pais_data = datos[0]

            # Extraemos el nombre común del país
            nombre    = pais_data["name"]["common"]

            # La capital es una lista; tomamos la primera con [0]
            capital   = pais_data.get("capital", ["Desconocida"])[0]

            # Las monedas son un diccionario; tomamos el primer valor
            monedas   = pais_data.get("currencies", {})
            if monedas:
                # next(iter(...)) obtiene el primer valor del diccionario
                moneda = next(iter(monedas.values()))["name"]
            else:
                moneda = "Desconocida"

            # Población del país
            poblacion = pais_data.get("population", 0)

            # Región geográfica
            region    = pais_data.get("region", "Desconocida")

            # Creamos y retornamos el objeto Pais con los datos extraídos
            return Pais(nombre, capital, moneda, poblacion, region)

        except requests.exceptions.ConnectionError:
            # Error de conexión (sin internet)
            print("  ❌ Error: No hay conexión a internet.")
            return None
        except requests.exceptions.Timeout:
            # La API tardó demasiado en responder
            print("  ❌ Error: La API tardó demasiado en responder.")
            return None
        except Exception as e:
            # Cualquier otro error inesperado
            print(f"  ❌ Error inesperado: {e}")
            return None


# ============================================================
# CLASE 4: EnviadorCorreo
# Se encarga de enviar el CSV por correo usando Gmail.
# IMPORTANTE: Necesitas habilitar contraseña de aplicación en Gmail.
# ============================================================
class EnviadorCorreo:
    # El constructor recibe las credenciales del remitente
    def __init__(self, correo_remitente, contrasena_app):
        self.correo_remitente = correo_remitente  # Tu correo Gmail
        self.contrasena_app   = contrasena_app    # Contraseña de aplicación (no la normal)

    # Envía el archivo CSV como adjunto al destinatario
    def enviar(self, correo_destinatario, ruta_csv):
        # Creamos el objeto del mensaje de correo
        mensaje = MIMEMultipart()
        mensaje["From"]    = self.correo_remitente   # Remitente
        mensaje["To"]      = correo_destinatario      # Destinatario
        mensaje["Subject"] = "📊 Country Finder - Lista de países consultados"  # Asunto

        # Cuerpo del correo (texto plano)
        cuerpo = (
            "Hola Daniel"
            "Adjunto encontrarás el archivo CSV con los países consultados "
            "desde la aplicación Country Finder.\n\n"
            "Saludos."
        )
        # Adjuntamos el cuerpo como texto plano al mensaje
        mensaje.attach(MIMEText(cuerpo, "plain"))

        # Abrimos el archivo CSV para adjuntarlo al correo
        with open(ruta_csv, "rb") as adjunto:  # "rb" = leer en modo binario
            parte = MIMEBase("application", "octet-stream")  # Tipo de archivo genérico
            parte.set_payload(adjunto.read())  # Leemos el contenido del archivo
            encoders.encode_base64(parte)       # Lo codificamos en base64 para enviarlo
            # Indicamos el nombre que tendrá el adjunto en el correo
            parte.add_header("Content-Disposition", f"attachment; filename=paises.csv")
            mensaje.attach(parte)  # Adjuntamos al mensaje

        try:
            # Nos conectamos al servidor SMTP de Gmail (puerto 587 con TLS)
            with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
                servidor.ehlo()           # Iniciamos la comunicación con el servidor
                servidor.starttls()       # Activamos el cifrado TLS (seguridad)
                servidor.ehlo()           # Nos volvemos a presentar tras el cifrado
                # Iniciamos sesión con el correo y la contraseña de aplicación
                servidor.login(self.correo_remitente, self.contrasena_app)
                # Enviamos el correo
                servidor.sendmail(self.correo_remitente, correo_destinatario, mensaje.as_string())
            print(f"  ✅ Correo enviado exitosamente a {correo_destinatario}")
        except smtplib.SMTPAuthenticationError:
            # Error si las credenciales son incorrectas
            print("  ❌ Error de autenticación. Verifica tu correo y contraseña de aplicación.")
        except Exception as e:
            # Cualquier otro error al enviar
            print(f"  ❌ Error al enviar correo: {e}")


# ============================================================
# CLASE 5: Aplicacion
# Es el CONTROLADOR principal: une todas las clases anteriores
# y maneja el menú de la aplicación.
# ============================================================
class Aplicacion:
    # El constructor crea instancias de todas las clases necesarias
    def __init__(self):
        self.gestor_csv  = GestorCSV("paises.csv")       # Gestor del archivo CSV
        self.cliente_api = ClienteAPI()                   # Cliente para la API
        self.paises      = self.gestor_csv.cargar_paises()  # Cargamos países del CSV al iniciar
        print(f"\n  📂 {len(self.paises)} país(es) cargado(s) desde el CSV.")

    # Busca si un país ya existe en la lista local (en memoria)
    def _buscar_local(self, nombre):
        for pais in self.paises:
            # Comparamos en minúsculas para ignorar mayúsculas/minúsculas
            if pais.nombre.lower() == nombre.lower():
                return pais  # Lo encontramos, lo retornamos
        return None  # No está en la lista local

    # Verifica si un país ya está en el CSV (para evitar duplicados)
    def _existe_en_csv(self, nombre):
        return self._buscar_local(nombre) is not None  # True si existe, False si no

    # --- OPCIÓN 1 del menú: Buscar un país ---
    def buscar_pais(self):
        nombre = input("\n  🔍 Ingresa el nombre del país: ").strip()  # strip() quita espacios extras

        # PASO 1: Buscamos primero en la lista local (CSV cargado en memoria)
        pais = self._buscar_local(nombre)

        if pais:
            # Lo encontramos localmente
            print("  📁 País encontrado en registros locales:")
            pais.mostrar()
        else:
            # No está localmente, vamos a la API
            print("  🌐 No está en registros locales. Consultando la API...")
            pais = self.cliente_api.buscar(nombre)

            if pais:
                # Lo encontramos en la API
                pais.mostrar()

                # Preguntamos si quiere guardarlo en el CSV
                guardar = input("\n  ¿Deseas guardar este país en el CSV? (s/n): ").strip().lower()
                if guardar == 's':
                    # Verificamos que no exista ya (doble verificación)
                    if not self._existe_en_csv(pais.nombre):
                        self.gestor_csv.guardar_pais(pais)  # Guardamos en el archivo
                        self.paises.append(pais)            # También lo agregamos en memoria
                    else:
                        print(f"  ⚠️  '{pais.nombre}' ya existe en el CSV. No se guardó.")

    # --- OPCIÓN 2 del menú: Mostrar todos los países guardados ---
    def mostrar_todos(self):
        if not self.paises:  # Si la lista está vacía
            print("\n  ℹ️  No hay países guardados aún.")
            return
        print(f"\n  📋 Países guardados ({len(self.paises)} en total):")
        for pais in self.paises:  # Iteramos sobre cada país de la lista
            pais.mostrar()        # Mostramos sus datos

    # --- OPCIÓN 3 del menú: Enviar CSV por correo ---
    def enviar_correo(self):
        # Verificamos que haya países guardados
        if not self.paises:
            print("\n  ⚠️  No hay países guardados. Busca al menos uno primero.")
            return

        print("\n  📧 CONFIGURACIÓN DE CORREO")
        print("  ⚠️  Necesitas una 'contraseña de aplicación' de Gmail.")
        print("  ℹ️  Guía: https://myaccount.google.com/apppasswords\n")

        # Pedimos las credenciales del remitente
        remitente = input("  Tu correo Gmail (remitente): ").strip()  #--> mi correo
        contrasena = input("  Contraseña de aplicación (16 caracteres): ").strip()

        # Correo del destinatario (ya definido en el taller)
        destinatario = "daniel.florez@aulamatriz.edu.co"

        # Creamos el enviador y mandamos el correo
        enviador = EnviadorCorreo(remitente, contrasena)
        print(f"\n  📤 Enviando correo a {destinatario}...")
        enviador.enviar(destinatario, "paises.csv")

    # --- MENÚ PRINCIPAL ---
    def ejecutar(self):
        print("\n" + "="*45)
        print("   🌍  COUNTRY FINDER - Taller POO Python")
        print("="*45)

        while True:  # Bucle infinito que mantiene el menú activo
            # Mostramos las opciones del menú
            print("\n  ¿Qué deseas hacer?")
            print("  [1] 🔍 Buscar un país")
            print("  [2] 📋 Ver todos los países guardados")
            print("  [3] 📧 Enviar CSV por correo")
            print("  [4] 🚪 Salir")

            opcion = input("\n  Elige una opción (1-4): ").strip()  # Leemos la opción del usuario

            if opcion == "1":
                self.buscar_pais()        # Llamamos al método de búsqueda
            elif opcion == "2":
                self.mostrar_todos()      # Llamamos al método para mostrar todos
            elif opcion == "3":
                self.enviar_correo()      # Llamamos al método de correo
            elif opcion == "4":
                print("\n  👋 ¡Hasta luego!\n")
                break  # 'break' sale del bucle while y termina el programa
            else:
                print("  ❌ Opción inválida. Elige entre 1 y 4.")


# ============================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# Este bloque se ejecuta cuando corremos el archivo directamente.
# Es la "puerta de entrada" de la aplicación.
# ============================================================
if __name__ == "__main__":
    app = Aplicacion()  # Creamos la aplicación (esto carga el CSV automáticamente)
    app.ejecutar()      # Iniciamos el menú principal