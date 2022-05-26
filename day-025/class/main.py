from numpy import average
import pandas

# data = pandas.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-025/weather_data.csv")

# print(data["temp"])

# temp_list = data["temp"].tolist()

# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# temp = int(monday.temp)
# temp = (9/5) * temp + 32

# print(temp)

# data_dict = {
#   "students": ["Amy", "James", "Angela"],
#   "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-025/new_file.csv")

data = pandas.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-025/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"].unique()
fur_color_gray = len(data[data["Primary Fur Color"]  == "Gray"])
fur_color_red = len(data[data["Primary Fur Color"]  == "Cinnamon"])
fur_color_black = len(data[data["Primary Fur Color"]  == "Black"])

print(fur_color[1:])
print(fur_color_gray)
print(fur_color_red)
print(fur_color_black)

data_dict = {
  "Fur Color": fur_color[1:].tolist(),
  "Count": [fur_color_gray, fur_color_red, fur_color_black]
}

data = pandas.DataFrame(data_dict)
data.to_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-025/squirrel_count.csv")