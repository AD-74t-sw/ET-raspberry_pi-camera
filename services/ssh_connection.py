import os
import paramiko

class SSHConnectionServices:
    def __init__(self, hostname: str, username: str, password: str, port: int = 22):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.port = port
        self.ssh = None

    def ssh_connect(self) -> paramiko.SSHClient:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(
            hostname=self.hostname,
            port=self.port,
            username=self.username,
            password=self.password
        )
        self.ssh = ssh
        return ssh
    
    def ssh_send_command(self, command: str) -> tuple:
        if self.ssh:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            return stdin, stdout, stderr
        else:
            raise Exception("SSH connection not established. Please connect first.")
    
    def shh_disconnect(self) -> None:
        if self.ssh:
            self.ssh.close()
            self.ssh = None
            return 0
        else:
            return 1
        
    def get_file(self, filename: str, rasp_dir: str, local_dir: str) -> str:
        remote_file = f"{rasp_dir}/{filename}"
        local_file  = os.path.join(local_dir, filename)

        if self.ssh is not None:
            try:
                sftp = self.ssh.open_sftp()
                os.makedirs(local_dir, exist_ok=True)
                sftp.get(remote_file, local_file)
                sftp.close()
                return f"Archivo '{filename}' descargado a '{local_file}'"
            except Exception as e:
                return f"Error al descargar archivo [{remote_file}]: {e}"
    
    def get_current_directory(self) -> str:
        if self.ssh:
            try:
                stdin, stdout, stderr = self.ssh.exec_command("pwd")
                current_dir = stdout.read().decode().strip()
                return current_dir if current_dir else "~"
            except Exception:
                return "~"
        return "~"
    
