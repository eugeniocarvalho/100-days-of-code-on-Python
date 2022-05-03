import random
import time
from turtle import Screen, Turtle
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The SnakeMan")
screen.tracer(0)

food = Turtle()
game_is_on = True

snake = Snake()

while game_is_on:
  screen.update()
  time.sleep(0.15)

  screen.onkey(snake.up, "w")
  screen.onkey(snake.left, "a")
  screen.onkey(snake.right, "d")
  screen.onkey(snake.down, "s")

  snake.move()
  screen.listen()

screen.exitonclick()
