from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
toCont = True
menu = Menu()
# menuitem = MenuItem()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while toCont:
    decision = input(f"What would you like?{menu.get_items()} ").lower()
    order = menu.find_drink(decision)
    if(decision == "report"):
        coffee_maker.report()
        money_machine.report()
    if(decision == "off"):
        toCont = False
    if(decision == "latte"):
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    if(decision == "cappuccino"):
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    if(decision == "espresso"):
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
