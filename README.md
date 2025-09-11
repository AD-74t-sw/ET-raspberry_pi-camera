# [Eye Tracker] controller Raspberry Pi camera source code

## Requisitos

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [paramiko](https://pypi.org/project/paramiko/)

## Configuración del entorno virtual

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## Instalación de dependencias

```powershell
pip install -r requirements.txt
```

Si no tienes un `requirements.txt`, instala manualmente:

```powershell
pip install python-dotenv paramiko
```

## Archivo `.env`

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (ajusta los valores según tu configuración):

```
# SSH connections

RASPBERRY_PI_HOST=raspberrypi-et.local
RASPBERRY_PI_PORT=22
RASPBERRY_PI_USER=raspberry-et
RASPBERRY_PI_PASSWORD=12345678345


# Images directories

RASPBERRY_PI_IMAGES_PATH="/home/raspberry-et/images"
LOCAL_IMAGES_PATH="./images"
```

## Ejecución

```powershell
python -m main
```