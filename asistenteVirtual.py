import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar el microfono y devolver el texto
def escuchar_microfono():
    # Almacenar el recognizer en una variable
    r = sr.Recognizer()
    # Configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.8
        # Informar que comenzo la grabacion
        print("Ya puedes hablar")
        # Guardar el audio en una variable
        audio = r.listen(origen)
        try:
            # Buscar en google lo que se ha escuchado
            pedido = r.recognize_google(audio, language="es-ES")
            # Prueba de que se reconoce el audio
            print("Dijiste: " + pedido)
            # Devolver el texto
            return pedido
        # En caso de que no comprenda el audio
        except sr.UnknownValueError:
            print("No te he entendido")
            return "No te he entendido"
        # En caso de no resolver el pedido
        except sr.RequestError:
            print("No hay servicio")
            return "No hay servicio"
        # En caso de cualquier otro error
        except:
            print("Error")
            return "Error"


# Funcion para que el asistente hable
def hablar(mensaje):
    # Encender el motor
    engine = pyttsx3.init()
    # Configurar las propiedades del motor
    engine.setProperty("voice", 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_ES-ES_HELENA_11.0)')
    #engine.setProperty("rate", 150)
    # Decir el mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Probando las voces del asistente
# engine = pyttsx3.init()
# for voz in engine.getProperty('voices'):
#     print(voz)


# Funcion para informar el dia de la semana
def pedir_dia():
    # Crear una variable con datos de hoy
    dia = datetime.date.today()
    # Crear una variable para el dia de la semana
    dia_semana = dia.weekday()
    # Diccionario con los dias de la semana
    calendario = {0: 'Lunes', 1: 'Martes', 2: 'Miércoles', 3: 'Jueves', 4: 'Viernes', 5: 'Sábado', 6: 'Domingo'}
    # Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')


# Funcion para informar la hora
def pedir_hora():
    # Crear una variable con datos de hoy
    hora = datetime.datetime.now()
    # Decir la hora
    hablar(f'En este momento son las {hora.hour} horas con {hora.minute} minutos')


# Saludo inicial
def saludo_inicial():
    # Crear una variable con datos de hoy
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "Buenas tardes"
    # Decir el saludo
    hablar(f'{momento}, soy Helena, tu asistente personal. Por favor, dime en qué te puedo ayudar')



# Funcion principal del asistente
def pedir_cosas():
    # Activar el saludo inicial
    saludo_inicial()
    # Variable para controlar el bucle
    comenzar = True
    # Bucle para que el asistente este activo
    while comenzar:
        # Activar el microfono y guardar el pedido en una variable
        pedido = escuchar_microfono().lower()

        if "abrir youtube" in pedido:
            hablar("Abriendo YouTube")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "abrir navegador" in pedido:
            hablar("Abriendo navegador")
            webbrowser.open("https://www.google.com")
            continue

        elif "qué día es hoy" in pedido:
            pedir_dia()
            continue

        elif "qué hora es" in pedido:
            pedir_hora()
            continue

        elif "busca en wikipedia" in pedido:
            hablar("Buscando en Wikipedia")
            pedido = pedido.replace("wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar("Según Wikipedia")
            print(resultado)
            hablar(resultado)
            continue

        elif "busca en internet" in pedido:
            hablar("Buscando en Internet")
            pedido = pedido.replace("busca en internet", "")
            webbrowser.open(f"https://www.google.com/search?q={pedido}")
            hablar("Esto es lo que he encontrado")
            continue

        elif "reproduce" in pedido:
            hablar("Reproduciendo en YouTube")
            pedido = pedido.replace("reproduce", "")
            pywhatkit.playonyt(pedido)
            continue

        elif "dime un chiste" in pedido:
            hablar("Voy a contarte un chiste")
            chiste = pyjokes.get_joke("es", "all")
            print(chiste)
            hablar(chiste)
            continue

        elif "precio de las acciones de" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple": "AAPL", "amazon": "AMZN", "google": "GOOGL", "microsoft": "MSFT", "facebook": "META"}
            try:
                ticker = cartera[accion]
                accion_info = yf.Ticker(ticker)
                precio = accion_info.info["regularMarketPrice"]
                hablar(f'El precio de {accion} es {precio} dólares')
                print(f'El precio de {accion} es {precio} dólares')
            except KeyError:
                hablar(f'Lo siento, no tengo información sobre {accion}')
            continue
        elif "adiós" in pedido or "hasta luego" in pedido or "nos vemos" in pedido:
            hablar("Me voy a descansar, hasta luego")
            comenzar = False

pedir_cosas()