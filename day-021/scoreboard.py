from turtle import Turtle

L_POSITION = (-50, 250)
R_POSITION = (50, 250)

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.l_score = 0
    self.r_score = 0
    self.update()
  
  def l_point(self):
    self.l_score += 1
    self.update()
  
  def r_point(self):
    self.r_score += 1
    self.update()

  def update(self):
    self.clear()
    self.goto(L_POSITION)
    self.write(self.l_score, align="center", font=("Courier", 32, "normal"))
    self.goto(R_POSITION)
    self.write(self.r_score, align="center", font=("Courier", 32, "normal"))