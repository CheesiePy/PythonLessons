from turtle import *  # import the turtle module
import math  # import the math module

# set up the screen
screensize(900, 600)  # set the size of the screen
bgcolor('black')  # set the background color to black
color('red')  # set the pen color to red
speed(0)  # set the speed to 0
#fillcolor('red')  # set the fill color to red
pensize(2)  # set the pen width to 3
counter = 0  # set the counter to 0
while True:  # create a while loop
    #shape(name='triangle')  # draw a triangle'
    goto(counter/math.pi * math.cos(counter/(math.e/math.pi)),
         counter/math.e * math.sin(counter/(math.e/math.pi)))  # move to the next point
    counter += 1    # add 1 to the counter

    if counter % 3 == 0:
        color('red')  # change the pen color to green
    # elif counter % 5 == 0:
    #     color('purple')  # change the pen color to green
    elif counter % 7 == 0:
        color('blue')
    #elif counter % 11 == 0:
    #    color('teal')
    else:
        color('lightblue')
