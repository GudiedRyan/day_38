from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os
import time

CHROME_DRIVER_PATH = "D:\development\chromedriver.exe"
INSTA_EMAIL = "yesmanvong@gmail.com"
INSTA_PASS = os.environ["yesmanvongpass"]
FOLLOWED_ACCOUNT = "aoc"

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.login()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(INSTA_EMAIL)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTA_PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        self.driver.maximize_window()
    
    def find_followers(self):
        self.driver.get("https://www.instagram.com/aoc/")
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(1)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(1)
    def follow(self):
        follow_buttons = self.driver.find_elements_by_xpath('//button[text()="Follow"]')
        for button in follow_buttons:
            button.click()
            time.sleep(1)

insta = InstaFollower()
insta.find_followers()
insta.follow()