#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

sheet_data = DataManager()
sheet_data = sheet_data.get__data()

print(sheet_data[0])

for city in sheet_data:
  try:
    len(city["iataCode"]) == 0
  except:
    FlightSearch(city)
  else:
    if len(city["iataCode"]) == 0:
      FlightSearch(city)
      
