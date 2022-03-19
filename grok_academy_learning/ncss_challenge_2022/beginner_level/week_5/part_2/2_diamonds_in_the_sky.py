from turtle import *


# Put your function here
def draw_diamond(x, y, colour):
    penup()
    goto(x, y)
    pendown()
    fillcolor(colour)
    begin_fill()

    forward(20)
    right(120)
    forward(20)
    right(60)
    forward(20)
    right(120)
    forward(20)
    right(60)

    end_fill()


# Our code to draw the diamonds
bgcolor('navy')
left(60)
draw_diamond(-100, -30, 'white')
draw_diamond(-70, 20, 'gold')
draw_diamond(-120, 70, 'red')
draw_diamond(-15, 60, 'yellow')
draw_diamond(30, 20, 'turquoise')
draw_diamond(100, 50, 'white')
draw_diamond(80, -20, 'orange')
draw_diamond(0, -30, 'red')
