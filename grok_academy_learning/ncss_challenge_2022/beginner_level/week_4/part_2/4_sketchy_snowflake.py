
from turtle import *


def draw_branch():
    forward(50)
    left(60)
    for i in range(6):
        forward(15)
        right(60)
    right(60)
    backward(50)


# Write your code below!
pensize(2)
pencolor("white")
bgcolor("darkblue")

number_of_branches = int(input("How many branches? "))
internal_angle_of_branch = 360 / number_of_branches

fillcolor("white")
begin_fill()
for j in range(number_of_branches):
    draw_branch()
    right(internal_angle_of_branch)
end_fill()
