# Librerie
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# Librerie locali
from gestione_linea import gestione_linea

# Classe principale atta alla gestione della navigazione nel sito internet
class gestione_sito:
    # Funzione di setup classe
    def __init__(self, driver: webdriver.Chrome, url):
        self.driver = driver
        self.url = url

        self.driver.get(self.url)

    # Funzione per accedere al sito
    def login(self, username, passworld, tempo_massimo = 10):
        print("[SITO]Tentativo di login: " + self.url)
        print("[SITO]Nome: " + username + " Pass: " + passworld)

        # Inserisci credenziali
        try:
            self.driver.find_element_by_name("user").send_keys(username)
            self.driver.find_element_by_name("pwd").send_keys(passworld)
            self.driver.find_element_by_xpath("//input[@type='submit']").click()
        except:
            print("[SITO]ERRORE: credenziali errate")

        # Accetta il disclaimer del sito
        try:
            # Aspetta che il sito sia pronto
            WebDriverWait(self.driver, tempo_massimo).until(EC.presence_of_element_located((By.CLASS_NAME, "ao-menu-box")))
            time.sleep(0.5)

            # Accetta le condizioni del sito
            self.driver.find_element_by_class_name("ao-menu-box").click()

        # In caso l'atttesa del sito duri troppo
        except TimeoutException:
            print("[SITO]ERRORE TIMEOUT: Attesa disclaimer troppo lunga")

    # Funzione di ricerca linea
    def cerca_linea(self, numero_linea):
        print('[SITO]Ricerca linea: ' + numero_linea)

        # Inserisce il numero e inizia la ricerca
        try:
            # Aspetta che il sito sia pronto
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'ao_line_number')))

            # Inserisce il numero nella barra di ricerca
            self.driver.find_element_by_id('ao_line_number').clear()
            self.driver.find_element_by_id('ao_line_number').send_keys(numero_linea)

            # Invia la ricerca
            self.driver.find_element_by_id('ao_line_number_submit').click()

        # In caso l'atttesa del sito duri troppo
        except TimeoutException:
            print("[SITO]ERRORE TIMEOUT: Attesa ricerca linea troppo lunga")

        except:
            print("[SITO]ERRORE: errore durante la ricerca della linea")

        # Identifica Linea
        self.linea = gestione_linea(self.driver)
        self.linea.analizza_linea()