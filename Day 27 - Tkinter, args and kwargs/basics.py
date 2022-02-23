from tkinter import *


window = Tk()

window.minsize(500, 300)


my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)


def button_clicked():
    my_label.config(text="Button Clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=2)

button2 = Button(text="Click me x2", command=button_clicked)
button2.grid(column=3, row=1)

input = Entry(width=10)
input.grid(column=4, row=3)

window.mainloop()
