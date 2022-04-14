import random
import data
import art

def check_answer(answer, A, B):
  if answer == 'A' or answer == 'a':
    if A['follower_count'] > B['follower_count']:
      return True
  elif answer == 'B' or answer == 'b':
    if B['follower_count'] > A['follower_count']:
      return True
  return False

question1 = random.choice(data.data)
question2 = random.choice(data.data)
isCorrect = True
score = 0

while question1 == question2:
  question2 = random.choice(data.data)

print(art.LOGO)

while isCorrect:
  print(f"Compare A: {question1['name']}, a {question1['description']}, from {question1['country']}.")
  print(art.VS)
  print(f"Compare B: {question2['name']}, a {question2['description']}, from {question2['country']}.\n")
  answer = input("Who has more followers? Type 'A' or 'B': ")

  isCorrect = check_answer(answer, question1, question2)

  if isCorrect:
    score += 1
    print(f"\nYou're right! Current score: {score}\n")

    question1 = question2
    question2 = random.choice(data.data)

    while question1 == question2:
      question2 = random.choice(data.data)

print(f"Sorry, that's wrong. Final score: {score}")