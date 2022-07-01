from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

events = {}

html_list = driver.find_elements(By.CSS_SELECTOR, '.event-widget .shrubbery .menu li')
index = 0

for li in html_list:
  time = li.find_element(By.TAG_NAME, "time").text
  text = li.find_element(By.TAG_NAME , 'a').text

  events[index] = {
    'time': time,
    'name': text
  }

  index += 1

print(events)

driver.quit()