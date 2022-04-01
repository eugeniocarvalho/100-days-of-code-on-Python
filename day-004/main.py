import random

computer = random.randint(0, 2)

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if player == 0 and computer == 0:
  print("A tie")
elif player == 0 and computer == 1:
  print(f"Computer played:\n{paper}\n")
  print(f"Player played:\n{rock}\n")
  print("Computer win")
elif player == 0 and computer == 2:
  print(f"Computer played:\n{scissors}\n")
  print(f"Player played:\n{rock}\n")
  print("Player win")
elif player == 1 and computer == 0:
  print(f"Computer played:\n{rock}\n")
  print(f"Player played:\n{paper}\n")
  print("PLayer win")
elif player == 1 and computer == 1:
  print(f"Computer played:\n{paper}\n")
  print(f"Player played:\n{paper}\n")
  print("A tie")
elif player == 1 and computer == 2:
  print(f"Computer played:\n{scissors}\n")
  print(f"Player played:\n{paper}\n")
  print("PLayer win")
elif player == 2 and computer == 0:
  print(f"Computer played:\n{rock}\n")
  print(f"Player played:\n{scissors}\n")
  print("Computer win")
elif player == 2 and computer == 1:
  print(f"Computer played:\n{paper}\n")
  print(f"Player played:\n{scissors}\n")
  print(scissors)
  print("Player win")
elif player == 2 and computer == 2:
  print(f"Computer played:\n{scissors}\n")
  print(f"Player played:\n{scissors}\n")
  print("A tie")