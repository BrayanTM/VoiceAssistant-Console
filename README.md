# Asistente de Voz Virtual con Python
Este proyecto es un asistente de voz virtual desarrollado en Python que puede realizar diversas tareas mediante comandos de voz. Utiliza bibliotecas como `speech_recognition` para el reconocimiento de voz, `pyttsx3` para la síntesis de voz, y `webbrowser` para abrir sitios web.

## Características
- Reconocimiento de voz para interpretar comandos hablados.
- Síntesis de voz para responder a los comandos.
- Capacidad para abrir sitios web específicos.
- Fácil de personalizar y expandir con nuevas funcionalidades.
- Interfaz de línea de comandos simple.
- Compatibilidad con múltiples plataformas (Windows, macOS, Linux).
- Soporte para comandos personalizados.

## Requisitos
- Python 3.6 ⬆️
- Bibliotecas de Python:
  - speech_recognition
  - pyttsx3
  - webbrowser
  - pyaudio (para reconocimiento de voz en tiempo real)
  - pywhatkit (para reproducir videos en YouTube)
  - wikipedia (para buscar información en Wikipedia)
  - datetime (para obtener la hora actual)
  - yfinance (para obtener información financiera)
  - pyjokes (para contar chistes)

## Comandos Soportados
- `abrir youtube`: Abre YouTube en el navegador.
- `abrir navegador`: Abre Google en el navegador.
- `qué día es hoy`: Informa el día de la semana.
- `qué hora es`: Informa la hora actual.
- `busca en wikipedia [tema]`: Busca un resumen del tema en Wikipedia y lo lee.
- `busca en internet [consulta]`: Realiza una búsqueda en Google.
- `reproduce [canción/video]`: Reproduce el contenido en YouTube.
- `dime un chiste`: Cuenta un chiste.
- `precio de las acciones de [empresa]`: Informa el precio de la acción de la empresa (Apple, Amazon, Google, Microsoft, Facebook).
- `adiós` / `hasta luego` / `nos vemos`: Finaliza el asistente.
