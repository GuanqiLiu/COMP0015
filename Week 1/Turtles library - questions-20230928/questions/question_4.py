"""
Name: question_4.py

Description:

Draw shapes: triangle, square, pentagon, hexagon, octagon.

Author:

Date:

Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name

"""

from turtle import *

# Function to draw a triangle
def draw_triangle(side_length):
    
    for counter in range(3):
        fd(side_length)
        lt(120)
        
penup()
setpos(-260, 0)
pendown()
pensize(2)
pencolor("Green")
draw_triangle(30)


# Function to draw a square

def draw_square(side_length):
    
    for counter in range(4):
        fd(side_length)
        lt(90)


# place the turtle on the left hand side of your canvas
penup()
setpos(-210, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("Blue")

# Draw square
draw_square(50)


# Function to draw a pentagon
penup()
setpos(-120, 0)
pendown()
def draw_pentagon(side_length):
    
    for counter in range(5):
        fd(side_length)
        lt(72)

pensize(2)
pencolor("Green")
draw_pentagon(70)


penup()
setpos(20, 0)
pendown()
def draw_hexagon(side_length):
    
    for counter in range(6):
        fd(side_length)
        lt(60)

pensize(2)
pencolor("Red")
draw_hexagon(80)


penup()
setpos(200, 0)
pendown()
def draw_octagon(side_length):
    
    for counter in range(8):
        fd(side_length)
        lt(45)
pensize(2)
pencolor("Pink")
draw_octagon(81)
exitonclick()