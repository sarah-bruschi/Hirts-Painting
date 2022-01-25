import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(229, 239, 234), (241, 232, 237), (207, 154, 110), (171, 71, 37), (11, 19, 37), (235, 210, 101), (236, 65, 38), (159, 20, 28), (173, 20, 13), (86, 93, 115), (60, 31, 25), (149, 159, 169), (172, 144, 61), (72, 23, 27), (159, 68, 77), (180, 144, 151), (210, 67, 78), (235, 169, 158), (45, 49, 118), (169, 179, 175), (226, 169, 176), (94, 111, 109), (14, 21, 20), (180, 199, 188), (84, 75, 31), (188, 188, 203), (243, 
206, 5), (253, 6, 13)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    


screen = turtle_module.Screen()
screen.exitonclick()