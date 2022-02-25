from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

random_gen = {}
data_dict = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except:
    og_data = pd.read_csv("data/french_words.csv")
    data_dict = og_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# ---------------------------- GENERATE FLASH CARDS ------------------------------- #


def generator():
    global random_gen, timer
    window.after_cancel(timer)
    random_gen = random.choice(data_dict)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(language, text="French")
    canvas.itemconfig(word, text=random_gen["French"])
    timer = window.after(3000, flip_cards)

# ---------------------------- FLIP CARDS ------------------------------- #


def flip_cards():
    canvas.itemconfig(card_bg, image=card_back)
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=random_gen["English"])

# ---------------------------- SAVE PROGRESS ------------------------------- #


def save_cards():
    data_dict.remove(random_gen)
    print(len(data_dict))
    data = pd.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generator()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_cards)
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
card_bg = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")

wrong = Button(image=wrong_img, highlightthickness=0, command=generator)
wrong.grid(row=2, column=1)
right = Button(image=right_img, highlightthickness=0, command=save_cards)
right.grid(row=2, column=2)

window.mainloop()
