import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The PongMan")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    ball.bounce_x()

  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()


  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()