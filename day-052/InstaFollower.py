from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.getenv('INSTA_USER')
PASSWORD = os.getenv('INSTA_PASS')

chrome_driver_path = "/usr/bin/chromedriver"

class InstaFollower:
  def __init__(self):
    self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
    self.driver.get("https://www.instagram.com/")
    self.username_input = ''
    self.password_input = ''
  
  def login(self):
    sleep(1)
    self.username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    self.password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    
    self.username_input.send_keys(USERNAME)
    sleep(0.5)
    self.password_input.send_keys(PASSWORD)

    sleep(0.5)
    login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')

    login_button.click()
    sleep(5)

  def find_followers(self):
    self.driver.get("https://www.instagram.com/lofihiphop.fm/")
  
    sleep(3)

    followers = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_MB"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a')
    followers.click()

  def follow(self):
    all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
    for button in all_buttons:
      try:
        button.click()
        sleep(1)
      except ElementClickInterceptedException:
        cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
        cancel_button.click()