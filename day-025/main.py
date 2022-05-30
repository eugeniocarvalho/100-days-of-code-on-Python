import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S States GameMan")
image = "/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-025/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_text = turtle.Turtle()
state_text.penup()
state_text.hideturtle()
guessed_states = []
missing_states = []

style = ('Arial', 14, 'italic')

data = pd.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-025/50_states.csv")
score = 0

while len(guessed_states) < 50:
  answer = screen.textinput(title=f"Guess the state{score}/50", prompt="What's another state's name?")
  answer = answer.title()
  state = data[data.state == answer]

  if answer == 'Exit':
    break

  if not state.empty:
    score += 1
    state_text.goto(int(state.x), int(state.y))
    guessed_states.append(state.iloc[0]['state'])
    state_text.write(f"{state.iloc[0]['state']}", font=style, align='center')



states = data.state.tolist()

# for state in states:new 
#   if state not in guessed_states:
#     missing_states.append(state)

missing_states = [state for state in states if state not in guessed_states]
new_data = pd.DataFrame(missing_states)
new_data.to_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-025/states_to_learn.csv")