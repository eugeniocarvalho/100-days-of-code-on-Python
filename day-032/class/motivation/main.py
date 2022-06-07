import random
import smtplib
import datetime as dt

my_email = ""
password = ""

now = dt.datetime.now()
weekday = now.weekday()

date_of_birth = dt.datetime(year=1997, month=7, day=8)



if (weekday == 0): 
  with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-032/quotes.txt", "r") as file:
    data = file.readlines()
    phrase = random.choice(data)
  
  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
      from_addr=my_email, 
      to_addrs="eugeniofrcarvalho@gmail.com", 
      msg=f"Subject:Monday Motivation\n\n{phrase}"
      )

