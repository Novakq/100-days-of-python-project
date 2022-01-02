from tkinter import * 
import os
from tkinter import font
from quiz_brain import QuizBrain
os.chdir("Day-34")
###
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)
        self.score = Label(text="Score",fg="white", bg = THEME_COLOR)
        self.score.grid(column=1,row=0)
        self.canvas = Canvas(width=300  , height=250, highlightthickness=0, bg = "white")
        self.card_title = self.canvas.create_text(150,125,text="Title",width=280,font=("Ariel",20,"italic"))
        self.canvas.grid(column=0, row=1,columnspan=2,pady = 20)

        right_img = PhotoImage(file="images/true.png")
        wrong_img = PhotoImage(file="images/false.png")

        self.right_button = Button(image=right_img,highlightthickness=0,command=self.true_answer)
        self.right_button.grid(column=1, row=2)
        self.wrong_button = Button(image=wrong_img,highlightthickness=0,command=self.false_answer)
        self.wrong_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop() 

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.config(bg="white")
            self.score.config(text=self.quiz.score)
            self.canvas.itemconfig(self.card_title,text = q_text)
        else:
            self.canvas.config(text="End of quiz")

    def true_answer(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        
        
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)



