from colorama import Fore

class HelperServices:

    @staticmethod
    def main_help():
        help_text = f"""
{Fore.CYAN}Comandos disponibles:

{Fore.GREEN}tp {Fore.YELLOW}[FILENAME] [RESOLUCIÓN] [DELAY]{Fore.WHITE}
    Toma una foto usando la cámara conectada al Raspberry Pi.
    - FILENAME: (opcional) Nombre del archivo de imagen. Por defecto es un nombre con timestamp.
    - RESOLUCIÓN: (opcional) Formato WIDTHxHEIGHT (ejemplo: 640x480). Por defecto 640x480.
    - DELAY: (opcional) Segundos de espera antes de tomar la foto. Por defecto 5 segundos.
    Ejemplo: tp mi_foto.jpg 800x600 3

{Fore.GREEN}.exit {Fore.WHITE}o {Fore.GREEN}.quit{Fore.WHITE}
    Sale de la aplicación.

{Fore.GREEN}--help{Fore.WHITE}
    Muestra esta ayuda.
"""
        print(help_text)