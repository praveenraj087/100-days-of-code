# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/(height **2)
bmi_round=round(bmi)
if(bmi<18.5):
    print(f"Your BMI is {bmi_round}, you are underweight.")

if(bmi>18.5 and bmi<25):
    print(f"Your BMI is {bmi_round}, you have a normal weight.")

if(bmi>25 and bmi<30):
    print(f"Your BMI is {bmi_round}, you are slightly overweight.")

if(bmi>30 and bmi<35):
    print(f"Your BMI is {bmi_round}, you are obese.")

if(bmi>35):
    print(f"Your BMI is {bmi_round}, you are clinically obese.")
