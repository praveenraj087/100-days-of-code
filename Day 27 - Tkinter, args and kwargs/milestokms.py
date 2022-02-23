from tkinter import *


window = Tk()
window.config(padx=50, pady=50)


def calculate():
    miles_value = float(input.get())
    kms_value = miles_value*1.609
    answer.config(text=kms_value)


miles = Label(text=" Miles", font=("Arial", 24, "normal"))
miles.grid(column=3, row=1)

equal_to = Label(text="is equal to", font=("Arial", 24, "normal"))
equal_to.grid(column=1, row=2)

km = Label(text="Km", font=("Arial", 24, "normal"))
km.grid(column=3, row=2)

answer = Label(text="0", font=("Arial", 24, "normal"))
answer.grid(column=2, row=2)

input = Entry(width=10)
input.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=3)

window.mainloop()
