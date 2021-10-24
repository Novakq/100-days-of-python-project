from turtle import Turtle
import random


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0,250)
        self.score = 0
        self.color("white")
        self.write(f'Current Score: {self.score}',move=False,font=("Arial",20,"normal"))
        self.hideturtle()
        
    def score_up(self):
        self.clear()
        self.score += 1
        self.write(f'Current Score: {self.score}',move=False,font=("Arial",20,"normal"))