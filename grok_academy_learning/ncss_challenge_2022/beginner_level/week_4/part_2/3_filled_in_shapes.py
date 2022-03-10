from turtle import*

bgcolor("plum")
fillcolor("cornflowerblue")
pensize(10)
pencolor("royalblue")

number_of_sides = int(input("How many sides? "))
internal_angle = 360 / number_of_sides

begin_fill()
for side_number in range(number_of_sides):
    forward(40)
    left(internal_angle)
end_fill()
