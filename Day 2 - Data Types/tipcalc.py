print("Welcome to tip calculator")
total = float(input("What was the total bill?"))
tip = int(input("What percentage of the tip would you like to give?"))
tip_percent = tip/100
split = int(input("How many people to split the bill?"))

final_bill = total + (total*tip_percent)
split_bill = round(final_bill/split, 2)


print(f"Each person should pay: ${split_bill}")
