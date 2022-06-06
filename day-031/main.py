from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card = {}
to_learn = {}
try:
  data = pandas.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-031/data/words_to_learn.csv")
except FileNotFoundError:
  original_data = pandas.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-031/data/en_words.csv")
  to_learn = original_data.to_dict(orient="records")
else:
  to_learn = data.to_dict(orient="records")

def next_card():
  global card, flip_timer
  window.after_cancel(flip_timer)
  card = random.choice(to_learn)
  canvas.itemconfigure(title_text, text="English", fill="black")
  canvas.itemconfigure(word_text, text=card["English"], fill="black")
  canvas.itemconfig(card_background, image=card_front)
  flip_timer = window.after(3000, flip_card)

def flip_card():
  canvas.itemconfigure(title_text, text="Portuguese", fill="white")
  canvas.itemconfig(word_text, text=card["Portuguese"] , fill="white")
  canvas.itemconfig(card_background, image=card_back)

def is_known():
  to_learn.remove(card)

  data = pandas.DataFrame(to_learn)
  data.to_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-031/data/words_to_learn.csv", index=False)
  next_card()

window = Tk()
window.title("Flashyman")
window.config(bg=f"{BACKGROUND_COLOR}", padx=50, pady=50)
flip_timer = window.after(3000, flip_card)


canvas = Canvas(width=800, height=526, highlightthickness=0)

card_front = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-031/images/card_front.png")
card_back = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-031/images/card_back.png")

card_background = canvas_image = canvas.create_image(400, 263, image=card_front)

canvas.grid(column=0, row=0, columnspan=2, pady=10)
canvas.config(bg=BACKGROUND_COLOR)

title_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

wrong_image = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-031/images/wrong.png")
unknow_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
unknow_button.grid(column=0, row=1)

right_image = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-031/images/right.png")
know_button = Button(image=right_image, highlightthickness=0, command=is_known)
know_button.grid(column=1, row=1)

next_card()

window.mainloop()