import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

AUTH = os.getenv('SHEETY_AUTH')

headers = {
  'Authorization': AUTH
}

url = "https://api.sheety.co/09ce695de0902f26460a4e0de71ffea7/flightDeals/prices"

class DataManager:
  def __init__(self):
    response = requests.get(url=url, headers=headers)

    self.sheet_data = response.json()["prices"]
  
  
  def get__data(self):
    return self.sheet_data
