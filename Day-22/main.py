
from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game")


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(5,1)
paddle.goto(350,0)

        

def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(),new_y)

def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(),new_y)

screen.onkey(up, "Up")
screen.onkey(down, "Down")




screen.exitonclick()