import os
import dotenv

from services.ssh_connection import SSHConnectionServices


dotenv.load_dotenv()

def main():

    hostname = os.getenv("RASPBERRY_PI_HOST", "localhost")
    port = int(os.getenv("RASPBERRY_PI_PORT", 22))
    username = os.getenv("RASPBERRY_PI_USER", "username")
    password = os.getenv("RASPBERRY_PI_PASSWORD", "password")

    ssh_service = SSHConnectionServices(hostname=hostname, port=port, username=username, password=password)
    
    try:
        ssh_client = ssh_service.ssh_connect()
        print(f"Connected to {hostname}:{port} as {username}")
        
        stdin, stdout, stderr = ssh_client.exec_command("ls -l")
        print("Command output:")
        print(stdout.read().decode())
        
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