import os
from img import logo

def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def div(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}

while True:
  print(logo)

  number1 = float(input("What's the first number?\n"))
  result = 0
  while True:
    operator = input("Pick an operator\n+  -  *  /\n")
    number2 = float(input("What's the next number?\n"))

    number1 = operations[operator](number1, number2)

    print(f"{number1} {operator} {number2} = {number1}")
    isContinue = input(f"Type 'y' to continue calculating with {number1}, or type 'n' to start a new calculation: ")

    if isContinue == 'n':
      os.system('clear')
      break
