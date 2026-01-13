import self
from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()

        #window maximize
        driver.maximize_window()

        #open the url
        driver.get(baseUrl)

        #get title
        title = driver.title
        print("Title of the webpage is : " + title)

        #get current url
        currentUrl = driver.current_url
        print("The Current URL of the webpage is : " + currentUrl)

        #browser refresh
        driver.refresh()
        print("Browser refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        #open another url
        driver.get("https://www.geeksforgeeks.org/")
        currentUrl = driver.current_url
        print("The Current URL of the webpage is : " + currentUrl)

        #Browser back
        driver.back()
        print("Go one step back in browser history")
        currentUrl = driver.current_url
        print("The Current URL of the webpage is : " + currentUrl)

        #browser forward
        driver.forward()
        print("Go one step forward in browser history")
        currentUrl = driver.current_url
        print("The Current URL of the webpage is : " + currentUrl)

        #get page source
        pagesource = driver.page_source
        print()

        #browser Close/Quit
        driver.close()
        driver.quit()

ff = BrowserInteractions()
ff.test()

