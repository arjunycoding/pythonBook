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
stamp.goto(0, 0)
for i in range(20):
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    stamp.color(red, green, blue)
    stamp.stamp()
    stamp.forward(10)
    stamp.right(25)
stamp.goto(0, 0)
for i in range(20):
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    stamp.color(red, green, blue)
    stamp.stamp()
    stamp.forward(20)
    stamp.right(25)
stamp.goto(0, 0)
for i in range(30):
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    stamp.color(red, green, blue)
    stamp.stamp()
    stamp.forward(30)
    stamp.right(25)
turtle.done()