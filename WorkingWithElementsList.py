from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class WorkingWithElementsList():

    def testListOfElements(self):

        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonList = driver.find_elements(By.XPATH, "//input[contains(@type,'radio') and contains(@name,'cars')]")
        size = len(radioButtonList)
        print("size of the list: " + str(size))

        for radioButton in radioButtonList:
            isSelected = radioButton.is_selected()

            if not isSelected:
                radioButton.click()
                time.sleep(2)




ff = WorkingWithElementsList()
ff.testListOfElements()