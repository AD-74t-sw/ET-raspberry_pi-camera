# [Eye Tracker] controller Raspberry Pi camera source code

## Descripción

Este proyecto permite controlar la cámara de una Raspberry Pi de forma remota desde tu PC usando SSH. Puedes tomar fotos con diferentes resoluciones y delays, y descargar automáticamente las imágenes a tu máquina local.

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
# Prompt
RASP_PROMPT="|et=> "

# Raspberry Pi connection details
RASPBERRY_PI_HOST="raspberrypi-et.local"
RASPBERRY_PI_USER="raspberry-et"
RASPBERRY_PI_PASSWORD="12345678345"
RASPBERRY_PI_PORT=22

# Images storage paths
RASPBERRY_PI_IMAGES_PATH="/home/raspberry-et/Pictures"
LOCAL_IMAGES_PATH="./images/"
```

## Ejecución

```powershell
python -m main
```

## Uso

Al ejecutar el programa, tendrás un prompt interactivo. Además de los comandos especiales, puedes escribir cualquier comando de consola de la Raspberry Pi como si estuvieras conectado por SSH, y verás la salida directamente aquí. Puedes usar los siguientes comandos:

### Comandos disponibles

- `tp [FILENAME] [RESOLUCIÓN] [DELAY]`  
  Toma una foto usando la cámara conectada al Raspberry Pi.
  - **FILENAME**: (opcional) Nombre del archivo de imagen. Por defecto es un nombre con timestamp.
  - **RESOLUCIÓN**: (opcional) Formato WIDTHxHEIGHT (ejemplo: 640x480). Por defecto 640x480.
  - **DELAY**: (opcional) Segundos de espera antes de tomar la foto. Por defecto 5 segundos.
  - **Ejemplo**:  
    ```
    tp mi_foto.jpg 800x600 3
    ```

- `.exit` o `.quit`  
  Sale de la aplicación.

- `--help`  
  Muestra la ayuda de comandos.

## Ejemplo de sesión

```
|et=> tp
Toma una foto con nombre automático y la descarga a ./images/

|et=> tp foto1.jpg 1280x720 2
Toma una foto llamada foto1.jpg con resolución 1280x720 y 2 segundos de delay.

|et=> --help
Muestra la ayuda de comandos.
```

## Estructura del proyecto

```
.
├── main.py
├── requirements.txt
├── .env
├── images/
│   └── (imágenes descargadas)
└── services/
    ├── __init__.py
    ├── command_recognition.py
    ├── helper.py
    └── ssh_connection.py
```

## Troubleshooting

- **No se conecta al Raspberry Pi:**  
  Verifica que los datos en `.env` sean correctos y que la Raspberry Pi esté accesible por red.

- **No se descarga la imagen:**  
  Asegúrate de que la ruta `RASPBERRY_PI_IMAGES_PATH` exista en la Raspberry Pi y que la cámara esté correctamente conectada.

- **Permisos denegados:**  
  Verifica los permisos de usuario tanto en la Raspberry Pi como en tu máquina local para las carpetas de imágenes.

## Créditos

Desarrollado por:
- Isaías M. Neira Insulsa - imneira@miuandes.cl - @IMneira
- Benjamin A. Tapia Arana - batapia1@miuandes.cl - @AD-74t-sw