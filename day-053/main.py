from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/condo,apartment_duplex_type/paymenta_sort/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.63417331103516%2C%22east%22%3A-122.23248568896484%2C%22south%22%3A37.66204454350355%2C%22north%22%3A37.88836615784793%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A666853%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"

FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSe_DqRmlZgZ2RcF-3_Yo4NvYxF9igyJ31-F7Hh1-HrzmFMNkg/viewform"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}

response = requests.get(ZILLOW_URL, headers=headers)

zillow_web_page = response.text

soup = BeautifulSoup(zillow_web_page, 'html.parser')

properties = soup.find_all(class_="list-card-info")

property_address = []
property_price_per_month = []
property_link_to = []

print(len(properties))
for property in properties:
  try:
    property_address.append(property.select_one(".list-card-addr").text)
    property_price_per_month.append(property.select_one(".list-card-price").text)
    property_link_to.append(property.select_one(".list-card-link")['href'])
  except AttributeError:
    pass


chrome_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_path)
driver.get(FORM_LINK)

sleep(2)

for i in range(len(properties)):
  address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
  month_price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
  property_link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

  form_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

  address_input.send_keys(property_address[i])
  
  sleep(0.5)
  
  month_price_input.send_keys(property_price_per_month[i])
  
  sleep(0.5)

  property_link_input.send_keys(property_link_to[i])

  sleep(0.5)

  form_button.click()

  sleep(0.5)

  driver.get(FORM_LINK)


  sleep(1)


driver.quit()