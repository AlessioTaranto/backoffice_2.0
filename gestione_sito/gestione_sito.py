# Librerie
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# Preparazione apertura finestra web
driver = webdriver.Chrome()
url = "https://one.tim.it"
utenza = {"x1019428":"Cars.2020"}

# Apertura finestra
driver.get(url)

# Funzione per accedere al sito
def login(username, passworld):
    print("Tentativo di login: " + url)
    print("Nome: " + username + " Pass: " + passworld)

    # Inserisci credenziali
    try:
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pwd").send_keys(passworld)
        driver.find_element_by_xpath("//input[@type='submit']").click()
    except:
        print("ERRORE: credenziali errate")

    # Accetta pagina disclaimer
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ao-menu-box")))
        driver.find_element_by_class_name("ao-menu-box").click()
    except TimeoutException:
        print("ERRORE TIMEOUT: Attesa disclaimer troppo lunga")


# Funzione di ricerca linea
def cerca_linea(numero_linea):
    pass



login("x1019428","Cars.2020")
cerca_linea("057383193")

time.sleep(5)

