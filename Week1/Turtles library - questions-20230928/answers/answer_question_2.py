"""
Name: question_2.py

Description:

Draw 4 squares.

Author: Rae Harbird

Date: August 2018
"""

from turtle import *


penup()
setpos(-225, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw smallest square
for counter in range(4):
    forward(50)
    left(90)


# Draw next square
# move the turtle along
penup()
fd(75)
pendown()

# change the colour of the pen
pencolor("blue")

for counter in range(4):
    fd(75)
    lt(90)

# move the turtle along
penup()
fd(100)
pendown()

# change the colour of the pen
pencolor("green")

for counter in range(4):
    fd(100)
    lt(90)


# move the turtle along
penup()
fd(125)
pendown()

# change the colour of the pen
pencolor("red")

for counter in range(4):
    fd(125)
    lt(90)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
