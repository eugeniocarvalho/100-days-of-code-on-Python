from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()
coffee_order = ""



while coffee_order != 'off':
  coffee_order = input("What would you like? (espresso/latte/cappuccino) ")

  if (coffee_order == 'report'):
    coffee_maker.report()
    money.report()
  elif coffee_order != 'off':
    drink = menu.find_drink(coffee_order)
    if drink:
      flag = coffee_maker.is_resource_sufficient(drink)

      if flag:
        coffee_maker.make_coffee(drink)
        money.make_payment(drink.cost)
    else:
      break
  else:
    break

