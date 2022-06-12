import requests
from datetime import datetime, timedelta
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK_API_KEY = ""

parameters = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK,
  "apikey": STOCK_API_KEY
}

day1 = datetime.now() - timedelta(days=1)
day2 = datetime.now() - timedelta(days=2)
day1 = day1.strftime("%Y-%m-%d")
day2 = day2.strftime("%Y-%m-%d")

OWN_endpoint = "https://www.alphavantage.co/query"
response = requests.get(OWN_endpoint, params=parameters)

prices = response.json()["Time Series (Daily)"]

value_day1 = float(prices[f"{day1}"]["4. close"])
value_day2 = float(prices[f"{day2}"]["4. close"])
calc = abs(value_day1 - value_day2)
percentage = (calc / value_day1) * 100


NEWS_API_KEY = ""

parameters = {
  "q": COMPANY_NAME,
  "from": day1,
  "sortBy": "publishedAt",
  "language": "en",
  "apikey": NEWS_API_KEY
}

if percentage < -5 or percentage > 5:
  # proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
  OWN_API_KEY=""
  account_sid = "AC5f9076d806979eb0b1c9ccceecc51de2"
  AUTH_TOKEN_KEY=""

  client = Client(account_sid, AUTH_TOKEN_KEY)
  # client = Client(account_sid, AUTH_TOKEN_KEY, http_client=proxy_client)

  response = requests.get("https://newsapi.org/v2/everything", params=parameters)

  news = response.json()["articles"][:3]

  if percentage > 0:
    icon = "🔺"
  else:
    icon = "🔻"

  new_formated = f"{STOCK}: {icon}{round(percentage, 2)}%\n"

  for new in news:
    new_formated += f"Headline: {new['title']}.\nBrief: {new['description']}\n\n"

  message = client.messages \
      .create(
        body=new_formated,
        from_="",
        to=""
      )

  print(message.status)