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

    with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-020/data.txt") as data:
      self.high_score = int(data.read())

    self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))
  
  def updateScore(self):
    self.clear()
    self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

  def increaseScore(self):
    self.score += 1
    self.updateScore()
  
  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score

      with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-020/data.txt", mode="w") as data:
        data.write(str(self.high_score))
    
    self.score = 0
    self.updateScore()
