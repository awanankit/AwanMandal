import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.width(2)

# Colors list
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw flower pattern
for i in range(120):
    pen.pencolor(colors[i % 6])
    pen.circle(100)
    pen.left(3)

# Hide turtle
pen.hideturtle()

# Finish
turtle.done()