import os
import time
import dotenv
from colorama import init

from services.ssh_connection import SSHConnectionServices
from services.command_recognition import CommandRecognitionService
from services.terminal_interface import TerminalInterface
from services.helper import HelperServices


dotenv.load_dotenv()

def main():

    hostname    = os.getenv("RASPBERRY_PI_HOST", "localhost")
    port    = int(os.getenv("RASPBERRY_PI_PORT", 22))
    username    = os.getenv("RASPBERRY_PI_USER", "username")
    password    = os.getenv("RASPBERRY_PI_PASSWORD", "password")
    remote_path = os.environ.get("RASPBERRY_PI_IMAGES_PATH", "/home/raspberry-et/Pictures")
    local_path  = os.environ.get("LOCAL_IMAGES_PATH", "./images")

    terminal = TerminalInterface(username, hostname)

    ssh_service = SSHConnectionServices(hostname=hostname, port=port, username=username, password=password)
    
    try:
        ssh_client = ssh_service.ssh_connect()
        terminal.print_success(f"Connected to {hostname}:{port} as {username}")
        
        current_dir = ssh_service.get_current_directory()
        terminal.update_directory(current_dir)
        
        stdin, stdout, stderr = ssh_client.exec_command("ls")
        print(stdout.read().decode())

        terminal.print_info("Intenta --help para obtener ayuda sobre comandos\n")

        while True:
            filename = None
            command = input(terminal.get_prompt())
            
            if command.lower() in ['.exit', '.quit']:
                terminal.print_info("Exiting...")
                break
                
            if command.lower() == "--help":
                HelperServices.main_help()
                continue
            
            if command.strip():
                command, filename = CommandRecognitionService.recognize_and_transform(command, ssh_service)
                stdin, stdout, stderr = ssh_service.ssh_send_command(command)
                
                output = stdout.read().decode()
                error = stderr.read().decode()
                
                print(output)
            
                if command.strip().startswith('cd'):
                    time.sleep(0.5)
                    current_dir = ssh_service.get_current_directory()
                    terminal.update_directory(current_dir)

                if filename:
                    time.sleep(5)
                    download_result = ssh_service.get_file(filename, remote_path, local_path)
                    terminal.print_success(download_result)
                    
                if error:
                    terminal.print_error(error)

    except Exception as e:
        terminal.print_error(f"An error occurred: {e}")
    
    finally:
        disconnect_status = ssh_service.shh_disconnect()
        if disconnect_status == 0:
            terminal.print_success("Disconnected successfully.")
        else:
            terminal.print_info("No active connection to disconnect.")

if __name__ == "__main__":
    main()