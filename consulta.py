import requests

url = "https://rest.coinapi.io/v1/exchangerate/BTC/EUR"
apikey = "4D706A89-2675-4B87-A5EA-E7514A893F7E"

cabecera = {"X-CoinAPI-Key": apikey}

respuesta = requests.get(url, headers = cabecera)


print(respuesta.status_code)
print (respuesta.json()["rate"])
