import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

word = random.choice(words)
number_lifes = 7
number_errors = 0
blank_spaces = len(word)
answer = []

for i in range(blank_spaces):
  answer.append("_ ")


while number_lifes and blank_spaces:
  for i in range(len(answer)):
    print(answer[i], end='')
  

  player_answer = input("\n\nGuess a Letter:\n")

  if player_answer in word:
    for i in range(len(word)):
      if word[i] == player_answer:
        blank_spaces -= 1
        answer[i] = player_answer
  else:
    print(f"You gassed {player_answer}, that's not in the word. You lose a life.")
    print(HANGMANPICS[number_errors])
    number_errors += 1
    print()
    number_lifes -= 1

if number_lifes == 0:
  print("\nYou died. Try again in the next life.")
else:
  print(f"\n{word}\n")
  print("You guessed it. Congratulations")