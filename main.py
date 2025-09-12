import os
import time
import dotenv

from services.ssh_connection import SSHConnectionServices
from services.command_recognition import CommandRecognitionService


dotenv.load_dotenv()

def main():

    hostname    = os.getenv("RASPBERRY_PI_HOST", "localhost")
    port    = int(os.getenv("RASPBERRY_PI_PORT", 22))
    username    = os.getenv("RASPBERRY_PI_USER", "username")
    password    = os.getenv("RASPBERRY_PI_PASSWORD", "password")
    rasp_prompt = os.getenv("RASP_PROMPT", "|et=> ")
    remote_path = os.environ.get("RASPBERRY_PI_IMAGES_PATH", "/home/raspberry-et/Pictures")
    local_path  = os.environ.get("LOCAL_IMAGES_PATH", "./images")

    ssh_service = SSHConnectionServices(hostname=hostname, port=port, username=username, password=password)
    
    try:
        ssh_client = ssh_service.ssh_connect()
        print(f"Connected to {hostname}:{port} as {username}")
        
        stdin, stdout, stderr = ssh_client.exec_command("ls")
        print(f"\n{rasp_prompt}ls")
        print(stdout.read().decode())

        print("Intenta --help para obtener ayuda sobre comandos\n")

        while True:
            filename = None
            command = input(f"{rasp_prompt}")
            if command.lower() in ['.exit', '.quit']:
                print("Exiting...")
                break
            command, filename = CommandRecognitionService.recognize_and_transform(command, ssh_service)
            stdin, stdout, stderr = ssh_service.ssh_send_command(command)
            print(stdout.read().decode())
            err = stderr.read().decode()

            time.sleep(5)
            if filename:
                print(ssh_service.get_file(filename, remote_path, local_path))
            if err:
                print(f"Error: {err}")

    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        disconnect_status = ssh_service.shh_disconnect()
        if disconnect_status == 0:
            print("Disconnected successfully.")
        else:
            print("No active connection to disconnect.")

if __name__ == "__main__":
    main()