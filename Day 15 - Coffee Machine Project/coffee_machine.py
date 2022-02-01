from machine_data import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
toCont = True


def show_resources():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


def find_change(quart, dime, nickel, pen):
    total_sum = round((quart*0.25)+(dime*0.10)+(nickel*0.05)+(pen*0.01), 2)
    return total_sum


def check_resource(option):
    ing_water = MENU[option]["ingredients"]["water"]
    ing_milk = MENU[option]["ingredients"]["milk"]
    ing_coffee = MENU[option]["ingredients"]["coffee"]
    if(water > ing_water and milk > ing_milk and coffee > ing_coffee):
        return True
    else:
        return False


def check_transaction(option, paid):
    opt_cost = MENU[decision]["cost"]
    change = paid-opt_cost
    return change


def make_coffee(option):
    global water, milk, coffee, money
    water -= MENU[option]["ingredients"]["water"]
    milk -= MENU[option]["ingredients"]["milk"]
    coffee -= MENU[option]["ingredients"]["coffee"]
    money += MENU[option]["cost"]


def process_coin():
    q = int(input("How many quarters?: "))
    d = int(input("How many dimes?: "))
    n = int(input("How many nickels?: "))
    p = int(input("How many pennies?: "))
    return find_change(q, d, n, p)


while toCont:
    decision = input(
        "What would you like? (espresso/latte/cappuccino) ").lower()
    if(decision == "report"):
        show_resources()
    elif(decision == "off"):
        toCont = False
    elif(decision == "espresso"):
        if check_resource(decision):
            user_money = process_coin()
            if check_transaction(decision, user_money) == 0:
                make_coffee(decision)
                print(f"Here is your {decision}. Enjoy!")
            elif check_transaction(decision, user_money) > 0:
                print(
                    f"Your change is {check_transaction(decision, user_money)}")
                make_coffee(decision)
                print(f"Here is your {decision}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif(decision == "latte"):
        if check_resource(decision):
            user_money = process_coin()
            if check_transaction(decision, user_money) == 0:
                make_coffee(decision)
                print(f"Here is your {decision}. Enjoy!")
            elif check_transaction(decision, user_money) > 0:
                print(
                    f"Your change is {check_transaction(decision, user_money)}")
                make_coffee(decision)
                print(f"Here is your {decision}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry, not enough resources")
    elif(decision == "cappuccino"):
        if check_resource(decision):
            user_money = process_coin()
            if check_transaction(decision, user_money) == 0:
                make_coffee(decision)
                print(f"Here is your {decision}. Enjoy!")
            elif check_transaction(decision, user_money) > 0:
                print(
                    f"Your change is {check_transaction(decision, user_money)}")
                make_coffee(decision)
                print(f"Here is your {decision}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry, not enough resources")
    else:
        print("Not the right Keyword")
