from game_data import data
import art
import random
import os


def print_names(num):
    return (f"{data[num]['name']}, a {data[num]['description']}, from {data[num]['country']}")


def compare(a, b, guess):
    if(guess == "a"):
        if(data[a]['follower_count'] > data[b]['follower_count']):
            return True
        else:
            return False
    elif(guess == "b"):
        if(data[b]['follower_count'] > data[a]['follower_count']):
            return True
        else:
            return False


def get_guess(a, b, guess):
    if(guess == "a"):
        return a
    elif(guess == "b"):
        return b


def game(start, next, score):
    print(art.logo)
    print(f"Compare A:{print_names(start)}")
    print(art.vs)
    print(f"Against B: {print_names(next)}")
    answer = input("Who has more followers? Type A or B: ").lower()

    if compare(start, next, answer):
        score += 1
        print(score)
        start = get_guess(start, next, answer)
        next = random.randint(0, len(data))
        print(print_names(start))
        print(print_names(next))
        game(start, next, score)

    else:
        start_new = random.randint(0, len(data))
        next_new = random.randint(0, len(data))
        game(start_new, next_new, score)


score = 0
start = random.randint(0, len(data))
next = random.randint(0, len(data))
game(start, next, score)
# print(get_guess(start, next, "a"))
# print(data)
