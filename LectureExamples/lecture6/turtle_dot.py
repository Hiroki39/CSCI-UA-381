#!/usr/bin/env python3

## This program makes 350  sample dots appear on the turtle screen and
## Information about each dot is printed on the command line.
##
## The following pieces of information are used and printed:
##     The radius of each dot in pixels (1 to 35)
##     The red, green and blue components (from 0-255)
##     The X position of the dot on the screen (from -350 to +350)
##      The Y position of the dot from -350 to +350

def draw_dot(X,Y,red,green,blue,radius,turtle):
    turtle.pu()
    turtle.goto(X,Y)
    turtle.pencolor(red,green,blue)
    turtle.pd()
    turtle.dot(radius)

def main():
    import random
    import turtle
    my_screen = turtle.Screen()
    dotty = turtle.Turtle()
    my_screen.colormode(255)
    for num in range(350):
        X = random.randint(-350,350)
        Y = random.randint(-350,350)
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        radius = random.randint(1,35)
        print('X=',X,'Y=',Y,'red=',red,'green=',green,'blue=',blue,'radius=',radius)
        draw_dot(X,Y,red,green,blue,radius,dotty)

main()
