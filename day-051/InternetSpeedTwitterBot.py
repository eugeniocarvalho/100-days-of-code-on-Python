from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''

class InternetSpeedTwitterBot:
  def __init__(self):
    self.up = ''
    self.down = ''
    self.ping = ''

  def get_internet_speed(self):
    driver.get('https://www.speedtest.net/pt')
    
    sleep(3)

    start_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
    start_button.click()

    flag = True
    while flag:
      if driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').get_attribute('data-upload-status-value') == "0.04":
        flag = False

      self.down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
      self.up = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
      self.ping = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span').text

      sleep(2)

  def tweet_at_provider(self):
    driver.get('https://twitter.com/i/flow/login')
    
    sleep(3)
    
    email = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    password = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
    
    email.send_keys(TWITTER_EMAIL)
    
    sleep(1)
    
    password.send_keys(TWITTER_PASSWORD)

    password.send_keys(Keys.ENTER)
    
    sleep(6)

    tweet_compose = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

    tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up with ping {self.ping} when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    tweet_compose.send_keys(tweet)
    
    sleep(3)

    tweet_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')

    tweet_button.click()
    
    sleep(2)
    
    driver.quit()
    