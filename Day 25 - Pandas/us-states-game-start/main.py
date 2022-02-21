import turtle
import pandas as pd

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()
screen = turtle.Screen()
screen.title("State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state = []
missing_states = []
game_on = True

while len(guessed_state) < 50:
    score = len(guessed_state)
    answer = screen.textinput(
        f"{score}/50 States Guessed", "What's another state?").title()

    if(answer == "Exit"):
        break
    if answer in guessed_state:
        score -= 1
    elif answer in states:
        tr = turtle.Turtle()
        tr.hideturtle()
        tr.penup()
        x_init = data[data.state == answer]
        tr.goto(int(x_init.x), int(x_init.y))
        tr.write(answer)
        guessed_state.append(answer)


for value in states:
    if value not in guessed_state:
        missing_states.append(value)
df = pd.DataFrame(missing_states)
print(df)
df.to_csv("Missing_states.csv")
