from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color("white")
    self.goto((0, 260))
    self.hideturtle()
    self.score = 0
    self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))
  
  def updateScore(self):
    self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

  def increaseScore(self):
    self.clear()
    self.score += 1
    self.updateScore()

  def game_over(self):
    screen = Turtle()
    screen.color("white")
    screen.penup()
    screen.hideturtle()
    screen.write("Game over.", align=ALIGNMENT, font=FONT)
