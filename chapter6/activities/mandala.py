import turtle
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
for i in range(18):
    pen.circle(100, 100)
    pen.forward(100)
pen.penup()
pen.goto(0, 200)
pen.pendown()
for i in range(36):
    star()
    pen.right(10)
# pen.goto(100, 100)
# for i in range(50):
#     pen.circle(50)
#     pen.right(10)
#     pen.forward(20)
turtle.done()