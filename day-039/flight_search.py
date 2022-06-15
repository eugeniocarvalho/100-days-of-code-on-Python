import requests
import os
from dotenv import load_dotenv

load_dotenv()

headers = {
  'Authorization': os.getenv('SHEETY_AUTH')
}

class FlightSearch:
  def __init__(self, city):
    url = f"https://api.sheety.co/09ce695de0902f26460a4e0de71ffea7/flightDeals/prices/{city['id']}"
    
    flight_params = {
      "term": city["city"],
    }
    
    header = {
      "apikey": os.getenv('TEQUILA_API_KEY'),
    }
    
    flight_url = "https://tequila-api.kiwi.com/locations/query"
    
    response = requests.get(url=flight_url, params=flight_params, headers=header)
    
    iata_code = response.json()["locations"][:1][0]["code"]
    
    body = {
      "price": {
        'iataCode': iata_code
      }
    }
    
    requests.put(url=url, json=body, headers=headers)
    