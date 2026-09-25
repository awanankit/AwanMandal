import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("white")
screen.title("Windows Logo")

# Create turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Function to draw a square (Windows window)
def draw_square(x, y, size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

# Draw Windows logo - 4 squares in 2x2 grid
spacing = 40
square_size = 60
gap = 15

# Position for the 2x2 grid (centered)
start_x = -spacing - gap // 2
start_y = spacing + gap // 2

# Colors for Windows logo (official blue)
windows_blue = "#0078D4"

# Top-left square
draw_square(start_x, start_y, square_size, windows_blue)

# Top-right square
draw_square(start_x + square_size + gap, start_y, square_size, windows_blue)

# Bottom-left square
draw_square(start_x, start_y - square_size - gap, square_size, windows_blue)

# Bottom-right square
draw_square(start_x + square_size + gap, start_y - square_size - gap, square_size, windows_blue)

# Add text
pen.penup()
pen.goto(0, -180)
pen.pendown()
pen.color(windows_blue)
pen.penup()
style = ("Arial", 24, "bold")
screen.textinput = False
pen.write("Windows Logo", align="center", font=style)

# Finish
pen.hideturtle()
screen.exitonclick()
