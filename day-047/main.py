import smtplib
from urllib import response
from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

response = requests.get("https://www.amazon.com.br/Berserk-Deluxe-1-Kentaro-Miura/dp/1506711987/ref=sr_1_1?crid=1BAK6GPAP5WOD&keywords=berserk+deluxe+1")

soup = BeautifulSoup(response.text, 'html.parser')

current_price = soup.select_one(".a-color-base .a-size-base").text

current_price = current_price.replace("R$", "")
current_price = current_price.replace(",", ".")
current_price = float(current_price)

product_name = soup.select_one("#productTitle").text.strip()

lowest_price = 240

if current_price < lowest_price:
  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)

    message = f"{product_name} is now R$ {current_price}. Buy it! Or not :)"

    connection.sendmail(
      from_addr=EMAIL,
      to_addrs="@gmail.com",
      msg=f"Subject: Amazon Price tracker\n\n{message}"
    )

print(message)