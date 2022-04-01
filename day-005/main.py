import random
import string

symbols = "!@#$%¨&*()£¢¬?:><^"

print("Welcome to the PyPassword Generator!")

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = []

for letter in range(1, num_letters + 1):
  password.append(random.choice(string.ascii_letters))

for symbol in range(1, num_symbols + 1):
  password.append(random.choice(symbols))

for numbers in range(1, num_numbers + 1):
  password.append(str(random.randint(0, 9)))


random.shuffle(password)
passwordchar = ""

for char in password:
  passwordchar += char


print(f"Here is your password: {passwordchar}")