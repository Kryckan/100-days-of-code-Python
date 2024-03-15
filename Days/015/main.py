# import's
from beverage_meny import MENU
from resources import resources

# variables
drink_choice = ""
drink_price = 0.00


# lists:
money_in_machine = float()
money_payed = float()


def check_resources():
    for item in MENU[drink_choice]["ingredients"]:
        if MENU[drink_choice]["ingredients"][item] > resources[item]:
            print(f'Sorry we do not have enough {item}')
            greet()
        else:
            return True


def get_payed():
    global money_payed
    global money_in_machine
    print(f'Price of {drink_choice}: ${drink_price}')
    print(f'Money inserted: ${money_payed:.2f}')
    money_payed += float(input('Input quarters ($0.25): ')) * 0.25
    money_payed += float(input('Input dimes ($0.10): ')) * 0.10
    # money_payed += float(input('Input nickles ($0.05): ')) * 0.05
    # money_payed += float(input('Input pennies ($0.01): ')) * 0.01
    if money_payed < drink_price:
        print(f'There is ${(drink_price - money_payed):.2f} missing.')
        get_payed()
    elif money_payed > drink_price:
        print(f'Change returned: ${(money_payed - drink_price):.2f}')
        print('Preparing drink. Please hold...\n')
        money_in_machine += drink_price
    else:
        money_in_machine += drink_price


def report():
    print('\nReport:')
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffe: {resources["coffee"]}g')
    print(f'Money: $ {money_in_machine:.2f}')
    greet()

def greet():
    global drink_choice
    global drink_price
    print('What would you like?')
    for drink in MENU:
        print(f' {drink.title()}')
    drink_choice = input('Please enter your choice: ').lower()
    if drink_choice == 'off':
        print('Turning off machine...')
        quit()
    elif drink_choice == 'report':
        report()
    elif drink_choice not in MENU:
        print(f'Sorry. {drink_choice} is not on the menu. Please try again.')
        greet()
    drink_price = MENU[drink_choice]["cost"]


def make_drink(drink_choice):
    for ingredient in MENU[drink_choice]["ingredients"]:
        amount_needed = MENU[drink_choice]["ingredients"][ingredient]
        resources[ingredient] -= amount_needed
    print(f'Here is your {drink_choice}. Enjoy!')


def main():
    global money_payed
    money_payed = 0.00
    greet()
    check_resources()
    get_payed()
    make_drink(drink_choice)
    main()


if __name__ == '__main__':
    main()


# xTODO 1    Prompt user by asking “ What would you like? (espresso/latte/cappuccino)a.
#           a.  Check the user’s input to decide what to do next.
#           b.  The prompt should show every time action has completed, e.g. once the drink is
#               dispensed. The prompt should show again to serve the next customer.
# xTODO 2    Turn off the Coffee Machine by entering “ off ” to the prompt.
#           a.  For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#               the machine. Your code should end execution when this happens.
# xTODO 3    Print report.
#           a.  When the user enters “report” to the prompt, a report should be generated that shows
#               the current resource values. e.g.
#               Water: 100ml
#               Milk: 50ml
#               Coffee: 76g
#               Money: $2.5
# xTODO 4    Check resources sufficient?
#           a.  When the user chooses a drink, the program should check if there are enough
#               resources to make that drink.
#           b.  E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#               not continue to make the drink but print: “ Sorry there is not enough water. ”
#           c.  The same should happen if another resource is depleted, e.g. milk or coffee.
# xTODO 5    Process coins
#           a.  If there are sufficient resources to make the drink selected, then the program should
#               prompt the user to insert coins.
#           b.  Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#           c.  Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#               pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# xTODO 6    Check transaction successful?
#           a.  Check that the user has inserted enough money to purchase the drink they selected.
#               E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#               program should say “ Sorry that's not enough money. Money refunded. ”.
#           b.  But if the user has inserted enough money, then the cost of the drink gets added to the
#               machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#               Water: 100ml
#               Milk: 50ml
#               Coffee: 76g
#               Money: $2.5
#           c.  If the user has inserted too much money, the machine should offer change.
#               E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
#               places.
# xTODO 7    Make Coffee.
#           a.  If the transaction is successful and there are enough resources to make the drink the
#               user selected, then the ingredients to make the drink should be deducted from the
#               coffee machine resources.
#               E.g. report before purchasing latte:
#               Water: 300ml
#               Milk: 200ml
#               Coffee: 100g
#               Money: $0
#               Report after purchasing latte:
#               Water: 100ml
#               Milk: 50ml
#               Coffee: 76g
#               Money: $2.5
#           b.  Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#               latte was their choice of drink.