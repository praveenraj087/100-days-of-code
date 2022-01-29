# Step 1

import random
import hangman_art
import hangman_words
print(hangman_art.logo)
eog = False
lives = 6
chosen_word = random.choice(hangman_words.word_list)
emptylist = []

for i in chosen_word:
    emptylist += "_"

print(f'Pssst, the solution is {chosen_word}.')

while not eog:
    guess = input("Guess a letter:").lower()
    for i in range(0, len(emptylist)):
        if(chosen_word[i] == guess):
            emptylist[i] = guess

    if guess not in chosen_word:
        lives -= 1
        print(
            f"You guess the letter {guess}, that's not in the word. You lose a life")
        print(hangman_art.stages[lives])
        if(lives == 0):
            print("You lose!")
            exit(0)
    print(emptylist)

    if guess in emptylist:
        print(f"You have already guessed {guess}")

    if "_" not in emptylist:
        eog = True
        print("You Win!")
