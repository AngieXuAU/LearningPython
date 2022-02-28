from turtle import *

number_of_pickets = int(input("How many pickets? "))

pensize(5)
pencolor("peru")

penup()
forward(20)
pendown()
left(90)

for i in range(number_of_pickets):
    forward(60)
    backward(60)
    left(90)
    penup()
    forward(10)
    right(90)
    pendown()
