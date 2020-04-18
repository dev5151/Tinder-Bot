from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\webdrivers')

class TinderBot():
    def _init_(self):
        self.driver=driver

