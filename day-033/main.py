import smtplib
import requests
from datetime import datetime
import time

MY_LAT = -3.682910 # Your latitude
MY_LONG = -40.350891 # Your longitude
MY_EMAIL = ""
MY_PASS = ""

def is_visible():
  response = requests.get(url="http://api.open-notify.org/iss-now.json")
  response.raise_for_status()
  data = response.json()

  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])

  if ((MY_LAT - 5 <= iss_latitude  <= MY_LAT + 5 ) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5)):
    return True
  
  return False  

def is_night():
  parameters = {
      "lat": MY_LAT,
      "lng": MY_LONG,
      "formatted": 0,
  }

  response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()
  data = response.json() 
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  time_now = datetime.now()
  time_now = time_now.hour

  return time_now >= sunset or time_now <= sunrise


while True:
  time.sleep(60)
  if is_visible() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
      connection.starttls()
      connection.login(email=MY_EMAIL, password=MY_PASS)

      connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="eugeniofrcarvalho@gmail.com",
        msg="Subject:ISS Position\n\nOlha pra riba, desgraça!"
      )