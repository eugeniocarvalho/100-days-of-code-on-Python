import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = "ede3eaoeoksi9octn7eb1mnb4u8as"
USERNAME = "eugeniocarvalho"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": GRAPH_ID,
  "name": "Reading Graph",
  "unit": "pages",
  "type": "int",
  "timezone": "America/Sao_Paulo",
  "color": "sora"
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# CREATE A GRAPH ps: change the graph_ID
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# CREATE PIXEL
graph_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2022, month=6, day=10)

pixel_config = {
  "date": today.strftime("%Y%m%d"),
  "quantity": input("How many pages did you read today? ")
}

response = requests.post(url=graph_pixel, json=pixel_config, headers=headers)
print(response.text)


# UPDATE A PIXEL
# pixel_day = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20220611"

# pixel_update = {
#   "quantity": "30"
# }
# response = requests.put(url=pixel_day, json=pixel_update, headers=headers)

# print(response.text)


#DELETE A PIXEL

# response = requests.delete(url=pixel_day, headers=headers)
# print(response.text)