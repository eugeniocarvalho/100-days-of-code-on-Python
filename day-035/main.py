import requests
from twilio.rest import Client

api_key = "8edb66c7ef72fbdc0780c0a3e125830d"
OWN_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
  "lat": -2.997450,
  "lon": -47.353451,
  "exclude": "current,minutely,daily,alerts",
  "appid": api_key,
}

account_sid = "AC5f9076d806979eb0b1c9ccceecc51de2"
auth_token  = "3a8f92f9c5e53b78f846bd9d985fd23a"


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
      from_="+14698138513",
      to="+5588996214707"
  )

  print(message.status)