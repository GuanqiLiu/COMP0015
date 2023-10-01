"""
Name: question_1.py

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

# set the pen colour to a grenen colour
pencolor("green")

# Draw a square
forward(50)     # move forward 50 pixels （像素点）
left(90)        # turn left 90 degrees （90度）
forward(50)
lt(90)          # an abbreviation for turn left
fd(50)          # an abbreviation for move forward
lt(90)
fd(50)
lt(90)


# set the pen colour to a blue colour
pencolor("blue")

# place the turtle on the left hand side of your canvas
penup()
setpos(-200, 0)
pendown()

# Draw a square
forward(75)     # move forward 75 pixels
left(90)        # turn left 90 degrees
forward(75)
lt(90)          # an abbreviation for turn left
fd(75)          # an abbreviation for move forward
lt(90)
fd(75)
lt(90)

pencolor("green")

# place the turtle on the left hand side of your canvas
penup()
setpos(-75, 0)
pendown()

# Draw a square
forward(100)     # move forward 75 pixels
left(90)        # turn left 90 degrees
forward(100)
lt(90)          # an abbreviation for turn left
fd(100)          # an abbreviation for move forward
lt(90)
fd(100)
lt(90)

pencolor("red")

# place the turtle on the left hand side of your canvas
penup()
setpos(70, 0)
pendown()

# Draw a square
forward(150)     # move forward 75 pixels
left(90)        # turn left 90 degrees
forward(150)
lt(90)          # an abbreviation for turn left
fd(150)          # an abbreviation for move forward
lt(90)
fd(150)
lt(90)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()
