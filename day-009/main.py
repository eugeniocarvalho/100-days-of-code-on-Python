import os
bidders = []

while True:
  name = input("What is your name? ")
  bid = int(input("What is your bid: $"))

  isOtherBidders = input("Are there any other bidders? Type 'yes' or 'no'\n")
  
  bidders.append({
    "name": name,
    "bid": bid
  })

  if isOtherBidders == 'no':
    break
  else:
    os.system('clear')

highest = {
  "name": bidders[0]["name"],
  "bid": bidders[0]["bid"]
}

for i in bidders:
  if highest["bid"] < i["bid"]:
    highest["name"] = i["name"]
    highest["bid"] = i["bid"]

print(f"The winner is {highest['name']} with a bid of ${highest['bid']}")