THEME_COLOR = "#375362"

import time
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
  def __init__(self, quiz_brain: QuizBrain):
    self.quiz = quiz_brain

    self.window = Tk()
    self.window.title("QuizzlerMan")
    self.window.config(bg=THEME_COLOR, padx=20, pady=20)

    self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 16, "normal"))
    self.score.grid(column=1, row=0, pady=20)

    self.canvas = Canvas(width=300, height=250, bg="white")
    self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

    self.question = Label(text="",bg="white", fg="black", font=("Arial", 20, "italic"), wraplength=280)
    self.question.grid(column=0, row=1, columnspan=2)

    true_button_image = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-034/images/true.png")
    self.true_button = Button(image=true_button_image, highlightthickness=0, command=self.true_answer)
    self.true_button.grid(column=0, row=2, padx=30, pady=40)

    false_button_image = PhotoImage(file="/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-034/images/false.png")
    self.false__button = Button(image=false_button_image, highlightthickness=0, command=self.false_answer)
    self.false__button.grid(column=1, row=2, padx=30, pady=40)

    self.get_next_question()

    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg="white")
    self.question.config(bg="white")

    if self.quiz.still_has_questions():
      q_text = self.quiz.next_question()
      self.question.config(text=q_text)
    else:
      q_text = "The end."
      self.question.config(text=q_text)
      self.true_button.config(state="disabled")
      self.false__button.config(state="disabled")

  def get_score(self):
    score = self.quiz.score
    self.score.config(text=f"Score: {score}/10")

  def true_answer(self):
    self.give_feedback(self.quiz.check_answer("True"))

  def false_answer(self):
    self.give_feedback(self.quiz.check_answer("False"))
  
  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg="#4dc274")
      self.question.config(bg="#4dc274")
    else:
      self.canvas.config(bg="#f76045")
      self.question.config(bg="#f76045")
    
    self.get_score()
    self.window.after(1000, self.get_next_question)
