from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 12, "bold")
Q_FONT = ("Arial", 18, "italic")
TEMP_TXT = "Some filler text lorem ipsum blah blah blah"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzinator")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=SCORE_FONT)
        self.score_label.grid(column=0, row=0, columnspan=2)

        # Text Area
        self.text_area = Canvas(width=300, height=250, bg="white")
        self.q_text = self.text_area.create_text(150, 125, text=TEMP_TXT, font=Q_FONT, width=280)
        self.text_area.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=true_img, command=self.true_pressed)
        self.true_btn.config(highlightthickness=0)
        self.true_btn.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=false_img, command=self.false_pressed)
        self.false_btn.config(highlightthickness=0)
        self.false_btn.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.text_area.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            self.button_state("normal")
            q_text = self.quiz.next_question()
            self.text_area.itemconfig(self.q_text, text=q_text)
        else:
            self.text_area.itemconfig(self.q_text, text="You've reached the end of the quiz.")
            self.button_state("disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))
        self.button_state("disabled")

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
        self.button_state("disabled")

    def give_feedback(self, is_correct):
        if is_correct:
            self.text_area.config(bg="green")
        else:
            self.text_area.config(bg="red")
        self.window.after(100, self.get_next_question)

    def button_state(self, state):
        self.true_btn.config(state=state)
        self.false_btn.config(state=state)
