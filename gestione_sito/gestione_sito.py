# Librerie
import time
from selenium import webdriver


# Preparazione apertura finestra web
driver = webdriver.Chrome()
url = "https://one.tim.it"

# Apertura finestra
driver.get(url)

utenza = {"x1019428":"Cars.2020"}
def login(username, passworld):
    driver.find_element_by_placeholder("username").send_keys(username)
    driver.find_element_by_placeholder("passworld").send_keys(passworld)
    driver.find_element_by_type("submit").click()

login("x1019428","Cars.2020")

time.sleep(5)

