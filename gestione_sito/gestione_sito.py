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
        print("Login riuscito")
    except:
        print("ERRORE: credenziali errate")

    # Accetta il disclaimer del sito
    try:
        # Aspetta che il sito sia pronto
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ao-menu-box")))
        time.sleep(0.5)

        # Accetta le condizioni del sito
        driver.find_element_by_class_name("ao-menu-box").click()

    # In caso l'atttesa del sito duri troppo
    except TimeoutException:
        print("ERRORE TIMEOUT: Attesa disclaimer troppo lunga")


# Funzione di ricerca linea
def cerca_linea(numero_linea):
    print('\nRicerca linea: ' + numero_linea)

    # Inserisce il numero e inizia la ricerca
    try:
        # Aspetta che il sito sia pronto
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'ao_line_number')))

        # Inserisce il numero nella barra di ricerca
        driver.find_element_by_id('ao_line_number').clear()
        driver.find_element_by_id('ao_line_number').send_keys(numero_linea)

        # Invia la ricerca
        driver.find_element_by_id('ao_line_number_submit').click()

        print("Ricerca riuscita")

    # In caso l'atttesa del sito duri troppo
    except TimeoutException:
        print("ERRORE TIMEOUT: Attesa ricerca linea troppo lunga")

    except:
        print("ERRORE: errore durante la ricerca della linea")


login("x1019428","Cars.2020")
cerca_linea("057383193")