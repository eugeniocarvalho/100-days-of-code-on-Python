import random
from sre_constants import OP_IGNORE
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=400)


color = screen.textinput("Choose a color", "Escolhe uma cor ae")

def moveTurtleStart(turtle, angle__vertical, distance):
  turtle.setheading(angle__vertical)
  turtle.forward(distance)
  turtle.setheading(180)
  turtle.forward(270)
  turtle.setheading(0)

def run(turtle):
  turtle.forward(random.randint(5, 15))
  return turtle.pos()[0]

purple = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
orange = Turtle()
red = Turtle()

purple.shape("turtle")
blue.shape("turtle")
green.shape("turtle")
yellow.shape("turtle")
orange.shape("turtle")
red.shape("turtle")

purple.color("purple")
blue.color("blue")
green.color("green")
yellow.color("yellow")
orange.color("orange")
red.color("red")

purple.penup()
blue.penup()
green.penup()
yellow.penup()
orange.penup()
red.penup()

moveTurtleStart(purple, 90, 60)
moveTurtleStart(blue, 90, 30)
moveTurtleStart(green, 180, 0)
moveTurtleStart(yellow, 270, 30)
moveTurtleStart(orange, 270, 60)
moveTurtleStart(red, 270, 90)

onScreen = True
win_turtle = ""

while onScreen:
  turtle_pos = run(purple)

  if turtle_pos > 270:
    win_turtle = 'purple'
    break

  turtle_pos = run(blue)

  if turtle_pos > 270:
    win_turtle = 'blue'
    break

  turtle_pos = run(green)
  
  if turtle_pos > 270:
    win_turtle = 'green'
    break

  turtle_pos = run(yellow)
  
  if turtle_pos > 270:
    win_turtle = 'yellow'
    break

  turtle_pos = run(orange)
  
  if turtle_pos > 270:
    win_turtle = 'orange'
    break

  turtle_pos = run(red)
  
  if turtle_pos > 270:
    win_turtle = 'red'
    break

  
if color == win_turtle:
  print("You win")
else:
  print(f"You lose, the {win_turtle} turtle won")
screen.exitonclick()