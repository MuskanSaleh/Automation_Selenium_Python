import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utilities.handy_wrappers import HandyWrappers


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class UsingWrappers:

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)
        driver.get(baseUrl)

        textField1 = hw.getElement("enabled-example-input", "id")
        if textField1:
            textField1.send_keys("Test")


        time.sleep(2)

        textField2 = hw.getElement("//input[@id='enabled-example-input']", "xpath")
        if textField2:
            textField2.clear()

        driver.quit()


ff = UsingWrappers()
ff.test()
