from ctypes.wintypes import LONG
from tkinter import *
import math
from matplotlib.pyplot import text
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
reps = 0
timer = None
ticks = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global ticks
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"))
    tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def display_timer():
    global reps
    reps += 1
    work_sec = 15
    short_break_sec = 10
    long_break_sec = 20

    if(reps % 2 != 0 and reps < 8):
        start_timer(work_sec)
        label.config(text="Work", fg=GREEN)

    if(reps % 2 == 0 and reps < 8):
        start_timer(short_break_sec)
        label.config(text="Break", fg=PINK)

    if(reps == 8):
        start_timer(long_break_sec)
        label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_timer(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, start_timer, count-1)
    else:
        display_timer()
        global ticks
        ticks = ""
        for _ in range(math.floor(reps/2)):
            ticks += TICK
        tick.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Application")
window.config(padx=100, pady=50)
window.config(bg=YELLOW)
canvas = Canvas(width=200, height=224)
tomato = PhotoImage(file="tomato.png")
canvas.config(bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=2, row=2)

label = Label(text="Timer", bg=YELLOW,  fg=GREEN, font=(FONT_NAME, 30, 'bold'))
label.grid(column=2, row=1)

start = Button(text="Start", command=display_timer)
start.grid(column=1, row=3)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=3, row=3)

tick = Label(bg=YELLOW, fg=GREEN)
tick.grid(column=2, row=4)


window.mainloop()
