from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

class ElementState():

    def isEnabled(self):
        baseUrl = "https://www.google.com"
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.get(baseUrl)

        driver.implicitly_wait(3)

        e1 = driver.find_element(By.CSS_SELECTOR, "textarea[class = 'gLFyf']")
        e1state = e1.is_enabled() #true/false
        print("E1 state enabled? " + str(e1state))
        e1.send_keys("geeksforgeeks")

        time.sleep(5)

e = ElementState()
e.isEnabled()