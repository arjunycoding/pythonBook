# from turtle import *
# fillcolor("blue")
# begin_fill()
# circle(50)
# end_fill()

# fillcolor("green")
# begin_fill()
# circle(30)
# end_fill()
# done()

# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed(-10)
turtle.bgcolor('black')
for x in range(1000):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)