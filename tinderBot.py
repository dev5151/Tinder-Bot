from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from secrets import username, password,mob

driver=webdriver.Chrome(executable_path=r'C:\webdrivers\chromedriver.exe')

def check_exists_by_xpath():
    try:
        driver.find_element_by_xpath('//span[text()="Log in with Facebook"]')
            
    except NoSuchElementException:
        return False
    return True


class TinderBot():
    def _init_(self):
        self.driver=webdriver.Chrome()

    def login(self):
        driver.get('https://tinder.com')
        time.sleep(10)

        if(check_exists_by_xpath())==True:
            fb_btn=driver.find_element_by_xpath('//span[text()="Log in with Facebook"]')
            fb_btn.click()
        else:
            more_options_btn=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/button')
            more_options_btn.click()
            time.sleep(10)
            fb_btn=driver.find_element_by_xpath('//span[text()="Log in with Facebook"]')
            fb_btn.click()
   
        base_window=driver.window_handles[0]
        driver.switch_to_window(driver.window_handles[1])

        email_in = driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn =driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        driver.switch_to_window(base_window)

        time.sleep(10)

    
        phone_in=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        phone_in.send_keys(mob)

        continue_btn=driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        continue_btn.click()

        popup_1 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_1.click()

        popup_2 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup_2.click()

    def like(self):
        like_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            time.sleep(2)
            try:
                self.like()
            except Exception:
                try:
                   self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup =driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()