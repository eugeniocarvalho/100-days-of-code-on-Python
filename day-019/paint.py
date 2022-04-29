import turtle as t

timmy = t.Turtle()
screen = t.Screen()
timmy.pensize(5)

def up():
  timmy.forward(10)

def left():
  angle = timmy.heading() + 10
  timmy.setheading(angle)
  # timmy.forward(10)

def right():
  angle = timmy.heading() - 10
  timmy.setheading(angle)
  # timmy.forward(10)

def clear():
  timmy.penup()
  timmy.clear()
  timmy.home()
  timmy.pendown()


screen.onkeypress(up, "w")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")
screen.onkeypress(clear, "c")
screen.listen()

screen.exitonclick()