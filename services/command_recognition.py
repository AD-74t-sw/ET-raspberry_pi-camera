import os

from datetime import datetime
from services.helper import HelperServices


class CommandRecognitionService:

    @staticmethod
    def _take_photo(command: str) -> tuple[str, str]:
        command_parts = command.split(" ")
        command_length = len(command_parts)

        if command_length >= 2: # filename provided (or --help)
            if command_parts[1] == "--help":
                help_text = (
                    "Usage: tp [FILENAME] [RESOLUTION] [DELAY]\n"
                    " FILENAME: Optional. Name of the image file to save. Default is timestamped name.\n"
                    " RESOLUTION: Optional. Format WIDTHxHEIGHT (e.g., 640x480). Default is 640x480.\n"
                    " DELAY: Optional. Seconds to wait before taking the picture. Default is 7 seconds.\n"
                    " Example: tp myimage.jpg 800x600 5\n"
                )
                return help_text
            filename = command_parts[1]
        else:
            now = datetime.now()
            filename = now.strftime("image_%Y%m%d_%H%M%S.jpg")

        if command_length >= 3: # resolution provided
            resolution = f"-r {command_parts[2]}"
        else:
            resolution = "-r 640x480"

        if command_length >= 4: # delay provided
            delay = f"-S {command_parts[3]}"
        else:
            delay = "-S 5"

        rasp_dir = os.environ.get("RASPBERRY_PI_IMAGES_PATH", "/home/raspberry-et/Pictures")
        full_command = f"fswebcam {resolution} {delay} --no-banner --jpeg 100 {rasp_dir}/{filename}"

        return full_command, filename

    @staticmethod
    def recognize_and_transform(command: str, ssh_client=None) -> tuple[str, str | None]:
        if command.split(" ")[0] == "tp":
            final_command, filename = CommandRecognitionService._take_photo(command)
            return final_command, filename
        elif command == "--help":
            HelperServices.main_help()
            return "", None
        else:
            return command, None