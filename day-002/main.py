print("Welcome to the tip calculator.")
total = float(input("What was the total bill $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
how_many_people = int(input("How many people to split the bill? "))

total += total * (percentage / 100) 

rounded_bill = "{:.2f}".format(round(total / how_many_people, 2))

print(f"Each person should pay: ${rounded_bill}")