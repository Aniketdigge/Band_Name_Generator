import colorgram
import turtle as t
from random import choice, randint
"""rgb_colors = []
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)"""

#10/10 rows 20 size 50 space

color_list = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), 
              (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), 
              (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), 
              (207, 185, 181), (99, 140, 119), (184, 198, 181), (148, 116, 120), (204, 183, 186), (180, 195, 200), (53, 69, 59), 
              (122, 129, 135)]

timmy = t.Turtle()
timmy.shape("arrow")
timmy.speed("fastest")
t.colormode(255)

def draw_dot():
    x = -230
    y = -230
    timmy.penup()
    timmy.hideturtle()
    timmy.setx(x)
    timmy.sety(y)
    for i in range(10):
        for j in range(10):
            timmy.dot(20, choice(color_list))
            timmy.forward(50)     
        y += 50
        timmy.sety(y)
        timmy.setx(x)

draw_dot()

screen = t.Screen()
screen.exitonclick()
