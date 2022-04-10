from img import logo as art
import random, os

cards = {
  "1": 11,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "Q": 10,
  "K": 10,
  "J": 10
}

def get_cards(n):
  cards_generated = []

  for i in range(n):
    cards_generated.append(random.choice(list(cards.values())))

  return cards_generated

def get_score_cards(cards):
  score_sum = 0

  for i in cards:
    score_sum += i
    
  return score_sum

while True:
  wantToContinue = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

  if wantToContinue == 'n':
    break
  else:
    os.system('clear')
    print(art)
    player_cards = get_cards(2)
    player_score = get_score_cards(player_cards)
    computer_cards = get_cards(2)
    computer_score = get_score_cards(computer_cards)

    if player_score > 21:
      print("\nYou lose!\n")
      break

    print(f"Your cards: {player_cards}, current score {player_score}")
    print(f"Computer's first card {computer_cards[0]}")

    anotherCard = input("Type 'y' to get another card, 'n' to pass: ")

    while anotherCard == 'y':
      card = get_cards(1)
      is_value_1 = 0

      if card[0] == 11:
        is_value_1 = int(input("You have a A, would like 1 or 11? Type '1' or '11'\n"))

      if is_value_1 == 1:
        card[0] = 1
      
      player_cards.append(card[0])
      player_score = get_score_cards(player_cards)
      computer_choice = random.randint(0, 1)

    
      if computer_choice == 1:
        computer_cards += get_cards(1)
        computer_score = get_score_cards(computer_cards)

      if player_score > 21:
        print("\nYou lose!\n")
        break
      
      print(f"Your cards: {player_cards}, current score {player_score}")
      print(f"Computer's first card {computer_cards[0]}")

      anotherCard = input("Type 'y' to get another card, 'n' to pass: ")
    
    if ((player_score > computer_score) and player_score <= 21) or (computer_score > 21):
      print("\nYou win!\n")
    elif (player_score == computer_score) and player_score == 21:
      print("A draw")
        
    
    print(f"Your cards: {player_cards}, final score {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}\n")


    

      



