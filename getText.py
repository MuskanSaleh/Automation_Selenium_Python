import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class getText():

    def test(self):

        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        openTabElement = driver.find_element(By.ID, "opentab")
        #property to get the text of an element
        elementText = openTabElement.text

        print("Text on element is : " + elementText)
        time.sleep(1)
        driver.quit()

ff = getText()
ff.test()