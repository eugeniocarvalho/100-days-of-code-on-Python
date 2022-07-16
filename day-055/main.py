from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)

@app.route('/')
def home():
  return "<h1>Guess a number between 0 and 9</h1><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:number>')
def guess_number(number):
  text = ''

  if random_number == number:
    return "<h1 style='color: ForestGreen;'>You found me!</h1><img src='https://media4.giphy.com/media/yoJC2GnSClbPOkV0eA/giphy.gif?cid=ecf05e47llg5bpnwokyklxeuknzvslo0899cfdgva148bqeh&rid=giphy.gif&ct=g'>"
  
  if random_number < number:
    text = 'Too high'
  else:
    text = 'Too low'

  return f"<h1 style='color: red;'>{text}, try again!</h1><img src='https://media0.giphy.com/media/d2lcHJTG5Tscg/giphy.gif?cid=ecf05e471qptc0ht4f0zfdxiz8kpapsu60rojz6nscp23m0x&rid=giphy.gif&ct=g'>"



if __name__ == '__main__':
  app.run(debug=True)

