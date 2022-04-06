import string

def ceaser(message, number, answer):
  text = ""

  for letter in message:
    if letter == ' ':
      text += ' '
    else:
      if alphabet.index(letter) + number > alphabet_length:
        shift_number = (alphabet.index(letter) + number) % alphabet_length - 1
      else:
        shift_number = (alphabet.index(letter) + number) % alphabet_length
      
      if answer == 'decode':
        if alphabet.index(letter) - number < 0:
          shift_number = alphabet.index(letter) - number -1

        shift_number = alphabet.index(letter) - number

      text += alphabet[shift_number]
  
  print(f"The {answer} text is: {text}")

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet) - 1

while True:
  answer = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")

  message = input("Type your message:\n")
  number = int(input("Type the shift number:\n"))

  ceaser(message, number, answer)

  isBreak = input("Type 'yes' to continue. 'no'\n")

  if isBreak == 'no':
    break
