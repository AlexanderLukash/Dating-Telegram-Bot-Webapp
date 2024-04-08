from os import environ
from typing import Final


class TgKeys:
    TOKEN: Final = environ.get('TOKEN', 'define me!')


FrontEnd_URL = "https://bc3b-194-213-120-6.ngrok-free.app"
