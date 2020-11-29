# Librerie
import time
from selenium import webdriver

# Preparazione apertura finestra web
driver = webdriver.Chrome()
url = "https://one.tim.it"
utenza = {"x1019428":"Cars.2020"}

# Apertura finestra
driver.get(url)

def login(username, passworld):
    print("Tentativo di login: " + url)
    print("Nome: " + username + " Pass: " + passworld + '\n')
    try:
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pwd").send_keys(passworld)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        print("Login riuscito")
    except:
        print("Login fallito")

login("x1019428","Cars.2020")

time.sleep(5)

