"""
Name: question_2.py

Description:

Draw a square.

Author:

Date:

Here is a list of colours: https://trinket.io/docs/colors, click on the 
colour to see the turtle name

"""

from turtle import *


# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw the smallest square

for counter in range(4):   # repeat 4 times
    forward(50)
    left(90)

# place the turtle on the left hand side of your canvas
penup()
setpos(-200, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("blue")

for counter in range(4): #记得缩进 indented 
 fd(64)
 lt(90)

# place the turtle on the left hand side of your canvas
penup()
setpos(-75, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("red")

for counter in range(4): 
 fd(90)
 lt(90)

# place the turtle on the left hand side of your canvas
penup()
setpos(75, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("green")

for counter in range(4): 
 fd(150)
 lt(90)
# leave the turtle on the screen until the user clicks in the screen
exitonclick()

