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
for i in range(120+6):
    pen.pencolor(colors[i % 6])
    pen.circle(1000)
    pen.left(30)

# Hide turtle
pen.hideturtle()

# Finish
turtle.done()