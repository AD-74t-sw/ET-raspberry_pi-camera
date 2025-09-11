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
    
    def shh_disconnect(self) -> None:
        if self.ssh:
            self.ssh.close()
            self.ssh = None
            return 0
        else:
            return 1
    
