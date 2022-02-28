from turtle import *

pensize(5)
pencolor("pink")
length_of_side = int(input("Length? "))

for i in range(6):
    forward(length_of_side)
    left(60)
    back(length_of_side / 2)