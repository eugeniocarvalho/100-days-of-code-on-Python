from datetime import datetime
import requests
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
API_KEY = os.getenv('NUTRITIONIX_API_KEY')
GENDER = "male"
WEIGHT_KG = 65
HEIGHT_CM = 175
AGE = 24

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

params = {
  "x-app-id": APP_ID ,
  "x-app-key": API_KEY
}

query = input("diga o exercicio ")

content = {
  "query": query,
  "gender": GENDER,
  "weight_kg": WEIGHT_KG,
  "height_cm": HEIGHT_CM,
  "age": AGE
}

response = requests.post(url=url, json=content, params=params)

exercise_data = response.json()

# print(response.status_code)
# print(response.json())

url = "https://api.sheety.co/09ce695de0902f26460a4e0de71ffea7/myWorkouts/workouts"
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

sheety_auth = {
  "Authorization": SHEETY_AUTH
}
response = requests.get(url=url, headers=sheety_auth)


url = "https://api.sheety.co/09ce695de0902f26460a4e0de71ffea7/myWorkouts/workouts"

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

exercise = exercise_data["exercises"][0]["name"]
duration = exercise_data["exercises"][0]["duration_min"]
calories = exercise_data["exercises"][0]["nf_calories"]

content = {
  "workout": {
    "date": today,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories,
  }
}

response = requests.post(url=url, json=content, headers=sheety_auth)