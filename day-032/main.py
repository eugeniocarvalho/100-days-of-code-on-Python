import datetime as dt
import random
import smtplib
import pandas

EMAIL = "eugenio9008@gmail.com"
PASSWORD = "wrazxgaodcsebwln"

data = pandas.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-032/birthdays.csv")
data = data.to_dict(orient="records")
letters = []
persons = []

with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-032/letter_templates/letter_1.txt") as file:
  text1 = file.readlines()

with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-032/letter_templates/letter_2.txt") as file:
  text2 = file.readlines()

with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-032/letter_templates/letter_3.txt") as file:
  text3 = file.readlines()

texts = [text1, text2, text3]

for text in texts:
  words = ""

  for word in text:
    words += word
  
  letters.append(words)

now = dt.datetime.now()
day = now.day
month = now.month

for person in data:
  if person["day"] == day and person["month"] == month:
    persons.append(person)

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
  connection.starttls()
  connection.login(user=EMAIL, password=PASSWORD)
  
  for person in persons:
    message = random.choice(letters)
    person_email = person["email"]
    message = message.replace("[NAME]", person["name"])

    connection.sendmail(
      from_addr=EMAIL,
      to_addrs=f"{person_email}",
      msg=f"Subject:Happy Birthday!\n\n{message}"
      )
