from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')

class TinderBot():
    def _init_(self):
        self.driver=webdriver.Chrome()

    def login(self):
        driver.get('https://tinder.com')