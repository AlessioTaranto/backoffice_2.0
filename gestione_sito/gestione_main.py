# Librerie
from selenium import webdriver

# Classi locali
from gestione_sito import gestione_sito



driver = webdriver.Chrome()
url = "https://one.tim.it"

sessione = gestione_sito(driver, url)
sessione.login("x1034732", "Nican.20")
sessione.cerca_linea('057383193')