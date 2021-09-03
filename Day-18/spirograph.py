import turtle as t
from random import *

screen = t.Screen()
screen.colormode(255)

turt = t.Turtle()
turt.shape("turtle")

is_on =True
color_dict = {}

turt.speed(20)

num_of_circles = randint(10,50)
angle = 360/num_of_circles

for i in range(num_of_circles):
    color = (randint(0,255),randint(0,255),randint(0,255))
    turt.color(color)
    turt.circle(100)
    turt.right(angle)
    




    # 


  
    # turt.setheading(heading)
    # turt.color(color_dict[heading])
    # turt.forward(20)



screen.exitonclick()
