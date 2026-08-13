import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Beautiful Python Drawing")

artist = turtle.Turtle()
artist.speed(0)
artist.width(2)
artist.hideturtle()

num_petals = 120
radius = 250

for i in range(num_petals):
    hue = i / num_petals
    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    artist.pencolor(color)
    artist.penup()
    artist.goto(0, 0)
    artist.setheading(i * 3)
    artist.forward(radius)
    artist.pendown()
    artist.circle(80,120)
    artist.left(60)
    artist.circle(80, 120)

artist.penup()
artist.home()
artist.pencolor("white")
artist.write("Beautiful Python Drawing", align="center", font=("Arial", 24, "bold"))

screen.mainloop()
