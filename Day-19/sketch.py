from turtle import Turtle,Screen

fifi = Turtle()
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)
    
def move_back():
    tim.backward(10)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)

def clear():
    
    tim.home()
    tim.clear()

fifi.color("red")



screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_back,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")

screen.exitonclick()