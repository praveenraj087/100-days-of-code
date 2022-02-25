from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    web_search = website_inp.get()
    try:
        with open('data.json', "r") as data_file:
            data = json.load(data_file)
            s_email = data[web_search]["email"]
            s_pass = data[web_search]["password"]
            messagebox.showinfo(title=web_search,
                                message=f"Email:{s_email}\nPassword: {s_pass}")
    except (json.JSONDecodeError, KeyError):
        messagebox.showinfo(
            title="Oops!", message="Please add an entry to search!")
    finally:
        website_inp.delete(0, END)
        pass_inp.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_letters = [random.choice(letters)
                        for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols)
                        for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers)
                        for char in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password_end = "".join(password_list)
    pass_inp.insert(0, password_end)
    pyperclip.copy(password_end)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_file():
    web_save = website_inp.get()
    user_save = username_inp.get()
    pass_save = pass_inp.get()
    new_data = {
        web_save: {
            "email": user_save,
            "password": pass_save,
        },
    }

    if len(web_save) == 0 or pass_save == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except:
            with open("data.json", "w") as data_file3:
                json.dump(new_data, data_file3, indent=4)

        else:
            with open("data.json", "w") as data_file2:
                json.dump(data, data_file2, indent=4)
                website_inp.delete(0, END)
                pass_inp.delete(0, END)

        finally:
            website_inp.delete(0, END)
            pass_inp.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.config(highlightthickness=0)
canvas.create_image(100, 100, image=lock)
canvas.grid(row=1, column=2)

website = Label(text="Website")
website.grid(row=2, column=1)

website_inp = Entry(width=17)
website_inp.grid(row=2, column=2, columnspan=1)
website_inp.focus()

search_button = Button(text="Search", command=search)
search_button.grid(row=2, column=3)

username = Label(text="Email/Username")
username.grid(row=3, column=1)

username_inp = Entry(width=35)
username_inp.grid(row=3, column=2, columnspan=2)
username_inp.insert(0, "abc@gmail.com")

password = Label(text="Password")
password.grid(row=4, column=1)

pass_inp = Entry(width=17)
pass_inp.grid(row=4, column=2, columnspan=1)

gen = Button(text="Generate Password", command=generate_password)
gen.grid(row=4, column=3)

add = Button(text="Add", width=30, command=save_file)
add.grid(row=5, column=2, columnspan=2)


window.mainloop()
