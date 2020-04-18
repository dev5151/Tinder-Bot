from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')

class TinderBot():
    def _init_(self):
        self.driver=webdriver.Chrome()

    def login(self):
        driver.get('https://tinder.com')
        time.sleep(10)
        more_options_btn=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
        more_options_btn.click()
        time.sleep(10)
        fb_btn=driver.find_element_by_xpath('//span[text()="Log in with Facebook"]')
        fb_btn.click()