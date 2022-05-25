#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = []
names_converted = []

with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-024/Input/Names/invited_names.txt") as name:
  names = name.readlines()

for name in names:
  names_converted.append(name.strip())


for name in names_converted:
  with open("/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-024/Input/Letters/starting_letter.txt") as file:
    with open(f"/home/eugenio/Projetos/Udemy/100-days-of-code-on-Python/day-024/Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter:
      x = file.read()
      x = x.replace("[name]", name)
      letter.write(x + "\n")