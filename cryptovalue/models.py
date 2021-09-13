import requests
from . import APIKEY, URL

class APIerror(Exception):
    pass

class CryptovalueModel():
    def __init__(self):
        self.de = ""
        self.a = ""
        self.valor = 0.0

    def obtener(self):
        cabecera = {"X-CoinAPI-Key": APIKEY}
        respuesta = requests.get(URL.format(self.de, self.a), headers = cabecera)

        if respuesta.status_code == 200:
            self.valor = respuesta.json()["rate"]
        else:
            print(respuesta.json())
            raise APIerror(f"Se ha producido un error {respuesta.status_code}")