from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on = True

menu_object = Menu()
money_counter = MoneyMachine()
coffee_maker_machine= CoffeeMaker()

while is_on == True:
    
    choice = input("What would you like?"+ menu_object.get_items())
    selected_drink = menu_object.find_drink(choice)
    if choice == "off":
        is_on = False
    if choice == "report":
        coffee_maker_machine.report()
        money_counter.report()
    else:
        if coffee_maker_machine.is_resource_sufficient(selected_drink) == True:
            if money_counter.make_payment(selected_drink.cost) == True:
                coffee_maker_machine.make_coffee(selected_drink)
