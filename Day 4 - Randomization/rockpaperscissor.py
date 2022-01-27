import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("ROCK(0) PAPER(1) SCISSORS(2)")
user = int(input("What do you choose?"))
if(user == 0):
    print(rock)
if(user == 1):
    print(paper)
if(user == 2):
    print(scissors)
comp = random.randint(0, 2)
print("Computer Choose:")
if(comp == 0):
    print(rock)
if(comp == 1):
    print(paper)
if(comp == 2):
    print(scissors)

if(user == comp):
    print("Draw")
if(user == 0 and comp == 1):
    print("You Lose!")
if(user == 0 and comp == 2):
    print("You Win!")
if(user == 1 and comp == 0):
    print("You win!")
if(user == 1 and comp == 2):
    print("You Lose!")
if(user == 2 and comp == 0):
    print("You Lose!")
if(user == 2 and comp == 1):
    print("You Win!")
