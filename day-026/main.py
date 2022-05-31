import pandas

data = pandas.read_csv("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-026/nato_phonetic_alphabet.csv") 
dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

name = input("Enter a word:")
name = [letter for letter in name]

nato = [dictionary[letter.upper()] for letter in name ]

print(nato)