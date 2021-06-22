import turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
pen = turtle.Turtle()
pen.shape("turtle")
for i in range(len(colors)):
    pen.color(colors[i])
    pen.stamp()
    pen.forward(30)
turtle.done()
