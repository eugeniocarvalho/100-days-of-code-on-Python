from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("The SnakeMan")
screen.tracer(0)

food = Food()
game_is_on = True
snake = Snake()
scoreboard = Scoreboard()

while game_is_on:
  screen.update()
  time.sleep(0.10)
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.increaseSnake()
    scoreboard.increaseScore()

  if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
    snake.reset()
    scoreboard.reset()
  
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 15:
      snake.reset()
      scoreboard.reset()

  screen.onkey(snake.up, "w")
  screen.onkey(snake.left, "a")
  screen.onkey(snake.right, "d")
  screen.onkey(snake.down, "s")

  snake.move()
  screen.listen()

screen.exitonclick()