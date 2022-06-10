import requests
from twilio.rest import Client

api_key = ""
OWN_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
  "lat": -2.997450,
  "lon": -47.353451,
  "exclude": "current,minutely,daily,alerts",
  "appid": api_key,
}

account_sid = ""
auth_token  = ""


response = requests.get(OWN_endpoint, params=parameters)
weather_data = response.json()["hourly"]

weather_slice = weather_data[:12]

will_rain = False

for hour_data in weather_slice:
  condition_code = hour_data["weather"][0]["id"]

  if int(condition_code) <= 700:
    will_rain = True

if will_rain:
  client = Client(account_sid, auth_token)
  message = client.messages \
    .create(
      body="Vai cair toró hoje viu!☔☔",
      from_="",
      to=""
  )

  print(message.status)