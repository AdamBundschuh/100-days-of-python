from tkinter import *
from random import choice
import pandas

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
TOP_TXT_SIZE = 40
BOT_TXT_SIZE = 60
TXT_ITALIC = "italic"
TXT_BOLD = "bold"

# ----------------------------- CARDS --------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.cvs")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    to_learn = data.to_dict(orient="records")

current_card = {}


def is_known():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("./data/words_to_learn.cvs", index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy McFlasherson")
window.resizable(width=False, height=False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, TOP_TXT_SIZE, TXT_ITALIC))
card_word = canvas.create_text(400, 263, text="word", font=(FONT_NAME, BOT_TXT_SIZE, TXT_BOLD))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_btn = Button(image=wrong, command=next_card)
wrong_btn.config(highlightthickness=0, bd=0)
wrong_btn.grid(column=0, row=1, pady=(30, 0))

right_btn = Button(image=right, command=is_known)
right_btn.config(highlightthickness=0, bd=0)
right_btn.grid(column=1, row=1, pady=(30, 0))

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
