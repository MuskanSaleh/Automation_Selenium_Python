from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo:

    def test(self):
        base_url = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get(base_url)
        driver.execute_script("window.location = 'https://www.letskodeit.com/';")
        # click on signin link
        #driver.find_element(By.XPATH, "//div[@id = 'page']//a[@href = '/login']").click()

        wait = WebDriverWait(driver, 10, poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])

        element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id = 'page']//a[@href = '/login']")))
        element.click()

        time.sleep(2)
        driver.quit()

ff = ExplicitWaitDemo()
ff.test()

