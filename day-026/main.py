import pandas

data = pandas.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-026/nato_phonetic_alphabet.csv") 
dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

def generator_nato():
  name = input("Enter a word:").upper()
  try:
    nato = [dictionary[letter] for letter in name ]
  except KeyError:
    print("Sorry, only letters in the alphabet please")
    generator_nato()
  else:
    print(nato)

generator_nato()