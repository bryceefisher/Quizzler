import tkinter
from tkinter import *
from tkinter import messagebox

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.question_text = None
        self.score_label = None
        self.true_button = None
        self.canvas = None
        self.quiz = quiz_brain

        # Window
        self.window = tkinter.Tk()
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.window.title("Quizzler")

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Are You Ready?", fill=THEME_COLOR,
                                                     font=("Arial", 15, "normal"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)

        # True Button
        true_img = PhotoImage(file="true.png")
        self.true_button = Button(image=true_img, command=self.true_press)
        self.true_button.grid(column=0, row=2)

        # False Button
        false_img = PhotoImage(file="false.png")
        self.false_button = Button(image=false_img, command=self.false_press)
        self.false_button.grid(column=1, row=2, padx=10, pady=10)

        # Score Label
        self.score_label = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15, "normal"),
                                 bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.configure(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.configure(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"You're finished. Score: {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        if self.quiz.question_number <= 10:
            is_right = self.quiz.check_answer("true")
            self.give_feedback(is_right)
            self.score_label.configure(text=f"Score: {self.quiz.score}", font=("Arial", 15, "normal"),
                                       bg=THEME_COLOR, fg="white")

    def false_press(self):
        if self.quiz.question_number <= 10:
            is_right = self.quiz.check_answer("false")
            self.give_feedback(is_right)
            self.score_label.configure(text=f"Score: {self.quiz.score}", font=("Arial", 15, "normal"),
                                       bg=THEME_COLOR, fg="white")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
        print(bool(is_right))
