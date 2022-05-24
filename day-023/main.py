import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossman")
screen.tracer(0)

player = Player()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

cars = []

for _ in range(25):
  car = CarManager()
  cars.append(car)

game_is_on = True

while game_is_on:
  for car in cars:
    car.move()

    if player.distance(car) < 10:
      score_board.game_over()
      game_is_on = False
    
    if player.is_finished_line():
      player.reset()

      for speed in cars:
        speed.increase_speed()
      
      score_board.increase_level()
  
  time.sleep(0.1)
  screen.update()

screen.exitonclick()