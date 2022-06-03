from tkinter import *
import random
from tkinter import messagebox
import pyperclip

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
  
  if len(website) == 0 or len(password) == 0:
    messagebox.showinfo(title="Warning!", message="You forgot some field blank!")
  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the detail entered: \nUsername: {username}\n\nPassword: {password}\n")

    if is_ok:
      with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-029/data.txt", mode="a") as file:
        my_pass = f"{website} | {username} | {password}"
        file.write(f"{my_pass}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

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

website_entry = Entry(width=35, justify="left")
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
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