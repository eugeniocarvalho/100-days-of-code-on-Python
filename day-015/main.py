import art 
import resources as rs

menu = rs.MENU
stock = rs.resources
money = 0.0
coffe_type = ""

def print_report():
    print(f"Water: {stock['water']}ml")
    print(f"Milk: {stock['milk']}ml")
    print(f"Coffee: {stock['coffee']}g")
    print(f"Money: ${money}")

def check_stock(coffee_required):
    isEspresso = coffee_required == 'espresso'

    hasWater = stock['water'] >= menu[coffee_required]['ingredients']['water']
    hasCoffee = stock['coffee'] >= menu[coffee_required]['ingredients']['coffee']
    
    if not isEspresso:
        hasMilk = stock['milk'] >= menu[coffee_required]['ingredients']['milk']

    if isEspresso:
        if hasCoffee and hasWater:
            stock['water'] -=  menu[coffee_required]['ingredients']['water']
            stock['coffee'] -=  menu[coffee_required]['ingredients']['coffee']
            return True
    elif hasWater and hasMilk and  hasCoffee:
        stock['water'] -=  menu[coffee_required]['ingredients']['water']
        stock['milk'] -=  menu[coffee_required]['ingredients']['milk']
        stock['coffee'] -=  menu[coffee_required]['ingredients']['coffee']
        return True
    else:
        print("Sorry there is not enough:")
        if not hasWater:
            print('water')
        
        if not hasMilk:
            print('milk')
        
        if not hasCoffee:
            print('coffee')

        return False

def make_order(coffe_type):
    print('PLease insert coins')

    quarters = int(input('How many quarters? '))
    quarters *= 0.25 
    dimes = int(input('How many dimes? '))
    dimes *= 0.10
    nickles = int(input('How many nickles? '))
    nickles *= 0.05
    pennies = int(input('How many pennies? '))
    pennies *= 0.01
    sum = quarters + dimes + nickles + pennies

    if sum >= menu[coffe_type]['cost']:
        global money
        money += menu[coffe_type]['cost']
        transation = sum - menu[coffe_type]['cost']
        
        if transation > 0:
            print(f"here is ${round(transation, 2)} in change.")
        
        print(f'Here is your {coffe_type}. Enjoy!')
    else:
        print("Sorry that's not enough money. Money refounded.")

print(art.img)
while coffe_type != 'off':
    coffe_type = input('What would you like? (espresso/latte/cappuccino) ')

    if coffe_type == 'report':
        print_report()
    elif coffe_type != 'off':
        haveStock = check_stock(coffe_type)

        if haveStock:
            make_order(coffe_type)