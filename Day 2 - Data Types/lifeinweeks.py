# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_int = int(age)
years_rem = 90-age_int
mon_rem = years_rem*12
week_rem = years_rem*52
days_rem = years_rem*365

print(f"You have {days_rem} days, {week_rem} weeks, and {mon_rem} months left.")



