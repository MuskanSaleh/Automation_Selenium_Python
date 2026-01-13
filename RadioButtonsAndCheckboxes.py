from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class RadioButtonsAndCheckboxes():

    def test(self):

        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadiobtn = driver.find_element(By.ID, "bmwradio")
        bmwRadiobtn.click()

        time.sleep(2)

        benzRadiobtn = driver.find_element(By.ID, "benzradio")
        benzRadiobtn.click()

        time.sleep(2)

        bmwCheckbox = driver.find_element(By.ID, "bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)

        benzCheckbox = driver.find_element(By.ID, "benzcheck")
        benzCheckbox.click()

        print("BMW Radio Button is selected? " + str(bmwRadiobtn.is_selected())) #true/false if selected or not
        print("Benz Radio Button is selected? " + str(benzRadiobtn.is_selected()))
        print("BMW Checkbox is selected? " + str(bmwCheckbox.is_selected()))
        print("Benz Checkbox is selected? " + str(benzCheckbox.is_selected()))

ff = RadioButtonsAndCheckboxes()
ff.test()





