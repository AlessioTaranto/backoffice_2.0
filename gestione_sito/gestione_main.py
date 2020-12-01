# Librerie
from selenium import webdriver

# Classi locali
from gestione_sito import gestione_sito



driver = webdriver.Chrome()
url = "https://one.tim.it"
utenza = {"x1019428":"Cars.2020"}

sessione = gestione_sito(driver, url)
sessione.login("x1019428", "Cars.2020")
sessione.cerca_linea('057383193')