from turtle import *

colour = input("Colour? ")

pencolor(colour)
pensize(3)

# first eye
left(60)
forward(60)
right(120)
forward(60)
left(60)

# mouth
penup()
forward(10)
pendown()
forward(30)
penup()
forward(10)
pendown()

# second eye
left(60)
forward(60)
right(120)
forward(60)
