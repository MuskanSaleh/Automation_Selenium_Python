from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        base_url = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()

        #first maximize window
        driver.maximize_window()

        #then open the provided webpage or website
        driver.get(base_url)

        #this will be applicable to all the elements on webpage, it will wait before failing the code
        driver.implicitly_wait(10)

        # click on signin link
        loginLink = driver.find_element(By.XPATH, "//div[@id = 'page']//a[@href = '/login']")
        loginLink.click()

        #send input for email field
        emailField = driver.find_element(By.XPATH,"//input[@placeholder = 'Email Address']")
        emailField.send_keys("test")

        #send input for password field
        passField = driver.find_element(By.ID, "login-password")
        passField.send_keys("test")

        time.sleep(3)

        #to clear the email field
        emailField.clear()

        time.sleep(3)

        #sending again keys to email field
        emailField.send_keys("test")


ff = ClickAndSendKeys()
ff.test()