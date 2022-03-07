from cgitb import text
from tkinter import *
from turtle import right
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.config(bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.config(highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="Sample",
                                                fill="black", font=("Arial", 20, "italic"))
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)

        self.score = Label(text="Score: 0", background=THEME_COLOR)
        self.score.grid(row=1, column=2)

        self.right_img = PhotoImage(file="images/true.png")
        self.wrong_img = PhotoImage(file="images/false.png")
        self.right = Button(image=self.right_img, command=self.check_right)
        self.right.grid(row=3, column=1)
        self.wrong = Button(image=self.wrong_img, command=self.check_wrong)
        self.wrong.grid(row=3, column=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question, text="You've reached the end of the Quiz!")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def check_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)
