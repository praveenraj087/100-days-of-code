
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
listval = len(names) -1
rand_num = random.randint(1, listval)
print(f"{names[rand_num]} is going to buy the meal today!")
#Write your code below this line 👇
