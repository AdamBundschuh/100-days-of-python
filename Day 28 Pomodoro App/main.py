from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
timer = None
timer_running = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    start_btn.config(state="normal")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    top_text.config(text="Timer")
    checks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    start_btn.config(state="disabled")
    global reps
    reps += 1
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_seconds)
        top_text.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        top_text.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        top_text.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        num_checks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            num_checks += CHECKMARK
        checks.config(text=num_checks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato Timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Top Text
top_text = Label(text="Timer", font=(FONT_NAME, 36, "bold"), fg=GREEN, bg=YELLOW)
top_text.grid(column=1, row=0)

# Start Button
start_btn = Button(text="Start", command=start_timer, borderwidth=0)
start_btn.grid(column=0, row=2)

# Reset Button
reset_btn = Button(text="Reset", command=reset_timer, borderwidth=0)
reset_btn.grid(column=2, row=2)

# Check Marks
checks = Label(text="", font=(FONT_NAME, 16, "bold"), fg=GREEN, bg=YELLOW)
checks.grid(column=1, row=3)

window.mainloop()
