import random
from art import img

COMPUTER_NUMBER = random.randint(1, 100)

print(img)

def guess_number():
  player_number = int(input("Make a guess: "))

  if player_number == COMPUTER_NUMBER:
    return True

  if player_number > COMPUTER_NUMBER:
    print("Too high")
  else:
    print("Too low")
    
    
  

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
  game_mode = input("Choose a dificulty. Type 'easy' or 'hard'. ")

  if game_mode == 'easy':
    print("You have 10 attempts remaining to guess the number.")

    for i in range(10, 0, -1):
      found_number = guess_number()

      if found_number:
        print("You found!")
        break
      print(f"You have {i-1} attempts reamaining to guess the number")
    else:
      print("You Lose")
      print(f"I thought about the number {COMPUTER_NUMBER}")
    
    break
  else:
    print("You have 5 attempts remaining to guess the number.")

    for i in range(5, 0, -1):
      found_number = guess_number()

      if found_number:
        print("You found!")
        break
      
      print(f"You have {i-1} attempts reamaining to guess the number")
    else:
      print("You Lose")
      print(f"I thought about the number {COMPUTER_NUMBER}")
    
    break