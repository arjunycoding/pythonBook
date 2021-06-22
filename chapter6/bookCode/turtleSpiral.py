import turtle
import random
# turtle.setup(500, 500)
stamp = turtle.Turtle()
stamp.shape("turtle")
stamp.penup()
turtle.colormode(255)
paces = 20
red = 50
blue = 50
green = 50
for i in range(100):
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    stamp.color(red, green, blue)
    stamp.stamp()
    paces += 1
    stamp.forward(paces)
    stamp.right(25)
turtle.done()
