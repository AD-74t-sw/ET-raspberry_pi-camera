from colorama import Fore, Style, init

class TerminalInterface:
    def __init__(self, username: str, hostname: str):
        init(autoreset=True)  # Inicializa colorama
        self.username = username
        self.hostname = hostname
        self.current_directory = "~"
        
    def get_prompt(self):
        """
        Genera el prompt con directorio actual
        
        Returns:
            str: El prompt formateado con colores
        """
        prompt = f"{Fore.GREEN}{self.username}@{self.hostname}{Fore.WHITE}:{Fore.BLUE}{self.current_directory}{Fore.WHITE}$ "
        return prompt
        
    def update_directory(self, new_directory: str):
        """Actualiza el directorio actual mostrado en el prompt"""
        self.current_directory = new_directory
        
    def print_success(self, message: str):
        """Imprime un mensaje de éxito con formato"""
        print(f"{Fore.GREEN}{message}")
        
    def print_error(self, message: str):
        """Imprime un mensaje de error con formato"""
        print(f"{Fore.RED}Error: {message}")
        
    def print_info(self, message: str):
        """Imprime un mensaje informativo con formato"""
        print(f"{Fore.CYAN}{message}")
