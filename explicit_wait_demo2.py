from selenium import webdriver
from selenium.webdriver.common.by import By
from wait_types.explicit_wait_generic_framework import ExplicitWaitType
import time

class ExplicitWaitDemo2:

    def test(self):
        base_url = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)

        wait = ExplicitWaitType(driver)
        element = wait.waitForElement(locator="//div[@id = 'page']//a[@href = '/login']", locatorType="xpath")
        element.click()


        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo2()
ff.test()

