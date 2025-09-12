class HelperServices:

    @staticmethod
    def main_help():
        print("""
Comandos disponibles:

tp [FILENAME] [RESOLUCIÓN] [DELAY]
    Toma una foto usando la cámara conectada al Raspberry Pi.
    - FILENAME: (opcional) Nombre del archivo de imagen. Por defecto es un nombre con timestamp.
    - RESOLUCIÓN: (opcional) Formato WIDTHxHEIGHT (ejemplo: 640x480). Por defecto 640x480.
    - DELAY: (opcional) Segundos de espera antes de tomar la foto. Por defecto 5 segundos.
    Ejemplo: tp mi_foto.jpg 800x600 3

.exit o .quit
    Sale de la aplicación.

--help
    Muestra esta ayuda.
""")