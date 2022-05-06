from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.penup()
    self.color("white")
    self.shape("square")
    self.shapesize(6,1)
    self.goto(position)

  def up(self):
    if self.ycor() <= 210:
      self.goto(self.xcor(), self.ycor() + 25)

  
  def down(self):
    if self.ycor() >= -210:
      self.goto(self.xcor(), self.ycor() - 25)

