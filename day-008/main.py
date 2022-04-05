import string

flag = True
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_length = len(alphabet) - 1

while flag:
  encrypt_message = ""
  decrypt_message = ""
  answer = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")

  if answer == 'encode':
    message = input("Type your message:\n")
    number = int(input("Type the shift number:\n"))

    for i in range(len(message)):
      shift_number = (alphabet.index(message[i]) + number)

      if shift_number > alphabet_length:
        shift_number = (alphabet.index(message[i]) + number) - alphabet_length - 1

      encrypt_message += alphabet[shift_number]
    
    print(encrypt_message)
  elif answer == 'decode':
    message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))

    for i in range(len(message)):
      
      shift_number = (alphabet.index(message[i]) - number)
      
      decrypt_message += alphabet[shift_number]
      print(decrypt_message)
  else:
    break
