import turtle
import random
pen = turtle.Turtle()
def star():
    for i in range(5):
        pen.forward(100)
        pen.right(144)

turtle.setup(1000, 1000)
pen.speed(50)
pen.penup()
pen.goto(50, 50)
pen.pendown()
for i in range(200):
    turtle.colormode(255)
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    pen.penup()
    pen.color(red, green, blue)
    pen.goto(0, 0)
    pen.pendown()
    pen.circle(100 + i, 100)
    pen.forward(100)
# pen.goto(100, 100)
# for i in range(50):
#     pen.circle(50)
#     pen.right(10)
#     pen.forward(20)
turtle.done()