from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_generator():
  characters = "qwertyuiopçlkjhgfdaszxcvbnm"
  characters += characters.upper()
  characters += "12345678901567892340"
  characters += "!@#$%&*^?()#$^%&*(!@?)"
  pass_genereted = ""

  for _ in range(16):
    pass_genereted += random.choice(characters)

  password_entry.delete(0, END)
  password_entry.insert(END, pass_genereted)
  pyperclip.copy(pass_genereted)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
  website = website_entry.get()
  username = username_entry.get()
  password = password_entry.get()
  new_data = {website: {
    "email": username,
    "password": password
  }}
  
  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Warning!", message="You forgot some field blank!")
  else:
    try:
      with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-029/data.json", "r") as file:
        data = json.load(file)
    except FileNotFoundError:
      with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-029/data.json", "w") as file:
        json.dump(new_data, file, indent=2)
    else:
      data.update(new_data)
    
      with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-029/data.json", "w") as file:
        json.dump(data, file, indent=2)
    finally:
      website_entry.delete(0, END)
      password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
  try:
    with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-029/data.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
    messagebox.showinfo(title="warning", message="Any password storaged!")
  else:
    website = website_entry.get()
    try:
      password_entry.delete(0, END)
      password_entry.insert(END, data[website]["password"])
    except KeyError:
      messagebox.showinfo(title="Not Found", message="Account not found!")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Managerman")
window.config(padx=50, pady=50, bg="white")

canva = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-029/logo.png")
canva.create_image(100, 100, image=lock_img)
canva.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=19, justify="left")
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

search_button = Button(text="Search", command=search, width=13)
search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:",bg="white")
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.insert(END, string="emailman@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3, sticky="EW")

generator_pass_button = Button(text="Generator Password", command=pass_generator)
generator_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=40, command=save_file)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()