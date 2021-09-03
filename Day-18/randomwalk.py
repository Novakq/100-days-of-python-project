import turtle as t
from random import *


screen = t.Screen()
screen.colormode(255)

turt = t.Turtle()
turt.shape("turtle")

is_on =True
color_dict = {}
turt.pensize(15)
turt.speed(20)

for i in [0,90,180,270]:
    color = (randint(0,255),randint(0,255),randint(0,255))
    color_dict[i] = color

while is_on == True:
    heading = choice([0,90,180,270])
    turt.setheading(heading)
    turt.color(color_dict[heading])
    turt.forward(20)



screen.exitonclick()
