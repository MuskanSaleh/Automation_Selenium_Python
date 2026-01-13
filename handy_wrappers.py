#making it modular and useable
from selenium.webdriver.common.by import By
class HandyWrappers:

    def __init__(self, driver):
        self.driver = driver

    #utility methods
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        if locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not supported")

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found")
        except:
            print("Element not found")
        return element

#one way to find elements
    def isElementPresent(self, locator,byType):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element found")
                return True
            else:
                return False
        except:
            print("Element not found")
            return False

    def elementPresentCheck(self,locator,byType ):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                print("Element found")
                return True
            else:
                return False
        except:
            print("Element not found")
            return False

