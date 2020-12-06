# Librerie
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class gestione_linea:
    def __init__(self, driver: webdriver, tipo = 'null'):
        # Divisorio
        print('\n')

        self.driver = driver
        self.tipo_linea = tipo

    # Identifica tipo di linea
    def analizza_linea(self):


        # Se il tipo di linea non e' stato inserito lo ricerca su ONE
        if self.tipo_linea == 'null':
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[@class='ao-line-type-description']")))
            tipo_linea_raw = self.driver.find_element_by_xpath("//span[@class='ao-line-type-description']").text

            if tipo_linea_raw == 'Linea VDSL/EVDSL - FTTC TIM':
                self.tipo_linea = 'FTTC'

        print("[LINEA]Tipo linea: " + self.tipo_linea)
