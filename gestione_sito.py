# Collegamento al sito
import requests
url = "https://one.tim.it/one/One"
cafile = 'cacert.pem' # http://curl.haxx.se/ca/cacert.pem
r = requests.get(url, verify = False)

if r == '<Response [200]>':
    print("Collegamento riuscito")
else:
    print("Collegamento non riuscito")


# Dati login
dati_login = {"x1019428":"Cars.2020"}
ret = requests.post(url, dati_login, verify = False)

