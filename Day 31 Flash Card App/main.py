from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
TOP_TXT_SIZE = 30
BOT_TXT_SIZE = 50
TXT_ITALIC = "italic"
TXT_BOLD = "bold"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card App")
window.resizable(width=False, height=False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# Images
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_btn = Button(image=wrong)
wrong_btn.config(highlightthickness=0, bd=0, relief="flat")
wrong_btn.grid(column=0, row=1, pady=(30, 0))

right_btn = Button(image=right)
right_btn.config(highlightthickness=0, bd=0, relief="flat")
right_btn.grid(column=1, row=1, pady=(30, 0))

# Text
top_title = Label(text="French", font=(FONT_NAME, TOP_TXT_SIZE, TXT_ITALIC))
top_title.grid(column=0, row=0, columnspan=2, pady=(0, 150))

bot_title = Label(text="croissant", font=(FONT_NAME, BOT_TXT_SIZE, TXT_BOLD))
bot_title.grid(column=0, row=0, columnspan=2, pady=(150, 0))

window.mainloop()
