import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color(random.choice(COLORS))
    self.shape("square")
    self.shapesize(1, 2)
    self.speed = STARTING_MOVE_DISTANCE
    self.goto(random.randint(310, 1000), random.randint(-230, 280))
  
  def move(self):
    if self.xcor() < -310:
      self.reset()
    else:
      self.backward(self.speed)

  def reset(self):
    self.goto(random.randint(310, 800), random.randint(-230, 280))
  
  def increase_speed(self):
    if self.speed <= 10:
      self.speed += STARTING_MOVE_DISTANCE / 2