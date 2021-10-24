from turtle import Turtle

MOVE_DISTANCE = 5
UP = 90
DOWN = 270

class Paddle:


    def __init__(self):
        self = Turtle("square")
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.got
        self.x_pos = 350
        self.y_pos = 0

    def move(self):
        self.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(UP)

    def down(self):
        self.head.setheading(DOWN)