from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DynamicXPathFormat:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        #login -> lecture "How to click and type on a web element"
        driver.find_element(By.XPATH, "//div[@id = 'page']//a[@href = '/login']").click()
        email = driver.find_element(By.XPATH, "//input[@placeholder = 'Email Address']")
        email.send_keys("test@email.com")
        password= driver.find_element(By.ID, "login-password")
        password.send_keys("abcabc")
        driver.find_element(By.XPATH, "//button[@id = 'login']").click()
        time.sleep(5)

        #search for courses
        searchbox = driver.find_element(By.ID, "search-courses")
        searchbox.send_keys("Java")

        #select courses
        _course = "//div[contains(text(),'{0}')]"
        #replace 0 by this course name
        _courseLocator = _course.format("Javascript for beginners")

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()

ff = DynamicXPathFormat()
ff.test()