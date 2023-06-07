from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Consolas"
FONT_SIZE = 10
FONT_BOLD = "bold"
LIGHT_GREY = "#f3f6f4"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)

    pw_copied_lbl = Label(text="Password Copied to Clipboard")
    pw_copied_lbl.config(highlightbackground="green", fg="green", borderwidth=0, bg=LIGHT_GREY)
    pw_copied_lbl.place(x=175, y=190)
    window.after(3500, pw_copied_lbl.destroy)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_json_to_file(data):
    with open("data.json", mode="w") as data_file:
        json.dump(data, data_file, indent=4)


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or password == 0:
        messagebox.showerror(title="Oops!",
                             message="Website and/or password field is blanks.\n"
                                     "Please maksure sure you haven't left any fields blank.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            save_json_to_file(new_data)
        else:
            data.update(new_data)
            save_json_to_file(data)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH WEBSITES ------------------------------- #
def find_password():
    searched_website = website_entry.get()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oopsy Poopsie!",
                             message="No Data File Found.\nPlease add a website/password first.")
    else:
        if searched_website in data:
            email = data[searched_website]["email"]
            password = data[searched_website]["password"]
            messagebox.showinfo(title=searched_website + " Information",
                                message=f"Email: {email}\n"
                                        f"Password: {password}\n\nPassword has been copied to the clipboard.")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Oh no!", message="No details for the website exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.resizable(width=False, height=False)
window.config(padx=30, pady=30, bg=LIGHT_GREY)
window.iconbitmap("logo_s.ico")

# Logo
canvas = Canvas(width=200, height=200, bg=LIGHT_GREY, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Website Row
website_lbl = Label(text="Website:", font=(FONT_NAME, FONT_SIZE, FONT_BOLD), bg=LIGHT_GREY)
website_lbl.grid(column=0, row=1, stick="E", padx=(0, 10), pady=(25, 0))

website_entry = Entry(width=21, font=(FONT_NAME, FONT_SIZE))
website_entry.grid(column=1, row=1, sticky="EW", pady=(25, 0), padx=(0, 10))
website_entry.focus()

search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="EW", pady=(25, 0))

# Email/User Row
email_lbl = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE, FONT_BOLD), bg=LIGHT_GREY)
email_lbl.grid(column=0, row=2, padx=(0, 10))

email_entry = Entry(width=35, font=(FONT_NAME, FONT_SIZE))
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", pady=(5, 0))
email_entry.insert(END, "bundschuh.adam@gmail.com")

# Password Row
password_lbl = Label(text="Password:", font=(FONT_NAME, FONT_SIZE, FONT_BOLD), bg=LIGHT_GREY)
password_lbl.grid(column=0, row=3, stick="E", padx=(0, 10))

password_entry = Entry(width=21, font=(FONT_NAME, FONT_SIZE))
password_entry.grid(column=1, row=3, sticky="EW", padx=(0, 10))

password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3, sticky="EW")

# Add Row
add_btn = Button(text="Add", command=save, width=36)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW", pady=(5, 0))

window.mainloop()
