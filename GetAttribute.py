import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class GetAttribute():

    def test(self):

        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        element = driver.find_element(By.ID, "name")
        #property to get the value of an attribute
        result = element.get_attribute("class")

        print("value of an attribute is : " + result)
        time.sleep(1)
        driver.quit()

ff = GetAttribute()
ff.test()