from cgitb import text
import math
from time import sleep
from tkinter import *
from ttkthemes import ThemedTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_time():
  global reps
  reps = 0

  window.after_cancel(timer)
  canvas.itemconfigure(time_text, text="00:00")
  check_marks.config(text="")
  title_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
  global reps
  reps += 1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if reps % 8 == 0:
    countdown_time(long_break_sec)
    title_label.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    countdown_time(short_break_sec)
    title_label.config(text="Break", fg=PINK)
  else:
    countdown_time(work_sec)
    title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown_time(count):
  global reps
  global timer 

  if count >= 0:
    mins, secs = divmod(count, 60)
    canvas.itemconfigure(time_text, text=f"{mins:02d}:{secs:02d}")
    timer = window.after(1000, countdown_time, count - 1)
  else:
    start_timer()
    marks = ""
    mark_number = math.floor(reps / 2)
    for _ in range(mark_number):
      marks += "✓"

    check_marks.config(text=marks)
  
# ---------------------------- UI SETUP ------------------------------- #

window = ThemedTk(themebg=True)
# window.set_theme("plastik")
window.title("PomodoroMan")
window.config(padx=100, pady=100, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 62, "normal"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-028/tomato.png")
canvas.create_image(100, 112, image=tomato_img)

time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 42, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0, font=(FONT_NAME, 18, "normal"))
start_button.grid(column=0, row=2)

check_marks = Label(text="", font=(FONT_NAME, 42, "bold"), bg=YELLOW)
check_marks.grid(column=1, row=2)
check_marks.config(fg=GREEN, pady=10)

reset_button = Button(text="Reset", command=reset_time, highlightthickness=0, font=(FONT_NAME, 18, "normal"))
reset_button.grid(column=2, row=2)
window.mainloop()