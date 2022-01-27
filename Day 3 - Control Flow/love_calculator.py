# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
comb_name = name1.lower()+name2.lower()
t = comb_name.count("t")
r = comb_name.count("r")
u = comb_name.count("u")
e = comb_name.count("e")
true_total = t+r+u+e
l = comb_name.count("l")
o = comb_name.count("o")
v = comb_name.count("v")
ee = comb_name.count("e")
love_total = l+o+v+ee 
love_score = int(str(true_total)+str(love_total))

if(love_score<10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score>40 and love_score<50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")