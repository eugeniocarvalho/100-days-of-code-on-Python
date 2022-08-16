import os

alphabet = {
  'a': '• —',
  'b': '— • • •',
  'c': '— • — •',
  'd': '— • •',
  'e': '•',
  'f': '• • — •',
  'g': '— — •',
  'h': '• • • •',
  'i': '• •',
  'j': '• — — —',
  'k': '— • —',
  'l': '• — • •',
  'm': '— —',
  'n': '— •',
  'o': '— — —',
  'p': '• — — •',
  'q': '— — • —',
  'r': '• — •',
  's': '• • •',
  't': '—',
  'u': '• • —',
  'v': '• • • —',
  'w': '• — —',
  'x': '— • • —',
  'y': '— • — —',
  'z': '— — • •',
}

run = True


while run:
  word_to_morse = input('Word to morse code: ').lower()
  word_converted = ""

  for i in word_to_morse:
    word_converted += alphabet[i] + "  "
  
  print(word_converted)

  answer = input("Convert another word?\n1. Yes   2. No: ")

  if answer == '2':
    break
  elif answer != '1':
    print('Error. Answer incorrect.')
    break

  os.system('clear')
