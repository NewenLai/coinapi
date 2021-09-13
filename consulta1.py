import requests

url = "https://rest.coinapi.io/v1/exchangerate/{}/{}"
apikey = "4D706A89-2675-4B87-A5EA-E7514A893F7E"
cabecera = {"X-CoinAPI-Key": apikey}


seguir = "s"

while seguir == "s":
    de = input("Moneda de origen: ")
    a = input("Moneda de destino: ")
    respuesta = requests.get(url.format(de, a), headers = cabecera)

    if respuesta.status_code == 200:
        print (respuesta.json()["rate"])
    else:
        print(respuesta.status_code)
        print(respuesta.json)

    seguir = input ("Quieres seguir? (S/N) ").lower()
