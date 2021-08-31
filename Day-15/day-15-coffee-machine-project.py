from main import * 

report = f'Water: {resources["water"]}ml\n Milk: {resources["milk"]}ml\n Coffee: {resources["coffee"]}g\n Money: {resources["money"]}$'

def checkResources(resource,amount):
    if (resources[resource] - amount) >= 0:
        return True
    else:
        return resource

def makeDrink(resource,amount):
    resources[resource] = resources[resource] - amount 
    

def processCoins():
    print("Insert quarters")
    quarters = int(input())
    print("Insert dimes")
    dimes= int(input())
    print("Insert nickles")
    nickles = int(input())
    print("Insert pennies")
    pennies = int(input())
    total = quarters * 0.25 + dimes *0.1 + nickles*0.05 + pennies * 0.01
    return total 




while True:
    print("What would you like? (espresso/latte/cappuccino):")
    choice = input()
    if choice == "report":
        print(report)
        
        
    if choice == "off":
        print("Switching off")
        break
    if choice in MENU.keys():
        for i,j in MENU[choice]['ingredients'].items():
            ingredientsOk = True
            if checkResources(i,j) != True:
                print(f'Sorry there is not enough {i}')
                ingredientsOk = False
                break
            
        if ingredientsOk == True:
            inserted = processCoins()
            if inserted < MENU[choice]['cost']:
                print("Sorry that's not enough money. Money refunded")
            else:
                resources["money"]+= MENU[choice]['cost']
                for i,j in MENU[choice]['ingredients'].items():
                    makeDrink(i,j)
                print("Here is your "+ choice)
                if inserted > MENU[choice]['cost']:
                    print("Your change: "+ str(inserted -MENU[choice]['cost'])+"$")































































