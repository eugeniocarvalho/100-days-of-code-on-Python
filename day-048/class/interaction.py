from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

# number.click()
print(number)

search = driver.find_element(By.NAME, 'search')
search.send_keys("Python", Keys.ENTER)
# driver.quit()