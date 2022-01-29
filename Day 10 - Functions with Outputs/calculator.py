import calculator_art

print(calculator_art.logo)


def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def mul(n1, n2):
    return n1*n2


def div(n1, n2):
    return n1/n2


operation = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    toCont = True

    n1 = float(input("What is your first number?"))
    for symbol in operation:
        print(symbol)
    opr = input("Pick an Operation: ")

    while toCont:
        n2 = float(input("What us the next number? "))
        calc_opr = operation[opr]
        a1 = calc_opr(n1, n2)
        print(f"{n1} {opr} {n2} = {a1}")
        if input("Press y to use the same answer or n to use new number: ") == "y":
            n1 = a1
        else:
            toCont = False
            calculator()


calculator()
