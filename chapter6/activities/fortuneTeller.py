import turtle
import random

pen = turtle.Turtle()
spinAmount = random.randint(1, 360)
pen.penup()

pen.goto(200, 0)
pen.pendown()
pen.write("Yes!", font=('Open Sanns', 30))
pen.penup()

pen.goto(-400, 0)
pen.pendown()
pen.write("Absolutely Not!", font=('Open Sanns', 30))
pen.penup()

pen.goto(-100, 300)
pen.pendown()
pen.write("Uhh mabe?", font=('Open Sanns', 30))
pen.penup()

pen.goto(10, -200)
pen.pendown()
pen.write("Yes, But after 50 years!", font=('Open Sanns', 30))
pen.penup()
pen.right(spinAmount)

turtle.done()