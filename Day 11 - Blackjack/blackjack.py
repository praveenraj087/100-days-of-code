import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# ace = cards[0]


def deal_card(user_cards):
    if len(user_cards) == 0:
        user_cards = random.sample(cards, 2)
        return user_cards
    else:
        user_cards.append(random.choice(cards))
        return user_cards


def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards:
        if(sum(cards) > 21):
            cards.remove(11)
            cards.append(1)
    return sum(cards)


def compare(user_score, comp_score):
    if(user_score == comp_score):
        return "Draw"
    elif (user_score) == 0:
        return "You win with a Blackjack!"
    elif(comp_score) == 0:
        return "You lose, opponent has blackjack"
    elif user_score > 21:
        return "You lose! Over 21"
    elif comp_score > 21:
        return "You win! Computer over 21"
    elif(user_score > comp_score):
        return "You Win! You have higher score"
    elif(comp_score > user_score):
        return "You lose! Computer has higher score"


def blackjack():
    user_cards = []
    comp_cards = []
    game_over = False

    user_cards = deal_card(user_cards)
    comp_cards = deal_card(comp_cards)

    # user_sum = calc_score(user_cards)
    # comp_sum = calc_score(comp_cards)
    while not game_over:
        user_result = calc_score(user_cards)
        comp_result = calc_score(comp_cards)
        print(f"Your cards: {user_cards} and sum is: {user_result}")
        print(f"Computer's first card: {comp_cards[0]}")

        if(user_result == 0 or comp_result == 0 or user_result > 21):
            game_over = True
        else:
            if input("do you want to draw a card? ") == "y":
                user_cards = deal_card(user_cards)
                user_result = calc_score(user_cards)
            else:
                game_over = True
    while (comp_result != 0 and comp_result < 17):
        comp_cards = deal_card(comp_cards)
        comp_result = calc_score(comp_cards)

    print(f"You final cards are {user_cards} and your score is {user_result}")
    print(
        f"Computer's final cards are {comp_cards} and computer's final score is {comp_result}")
    print(compare(user_result, comp_result))


print(art.logo)
decision = input("Do you want to play a game of blackjack? ").lower()
if decision == "y":
    blackjack()
else:
    exit(0)

    # print(user_cards, user_result, comp_cards, comp_result)
    # blackjack = ace+10
