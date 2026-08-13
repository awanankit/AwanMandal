import turtle


def draw_flower():
    screen = turtle.Screen()
    screen.bgcolor("midnight blue")
    screen.title("Beautiful Flower")

    pen = turtle.Turtle()
    pen.speed(0)
    pen.width(2)
    pen.hideturtle()

    colors = ["magenta", "deep pink", "hot pink", "orange", "yellow"]

    for i in range(36):
        pen.color(colors[i % len(colors)])
        pen.begin_fill()
        for _ in range(2):
            pen.circle(100, 60)
            pen.left(120)
            pen.circle(100, 60)
            pen.left(60)
        pen.end_fill()
        pen.left(10)

    pen.color("forest green")
    pen.penup()
    pen.goto(0, -20)
    pen.pendown()
    pen.right(90)
    pen.forward(250)

    pen.color("light green")
    pen.penup()
    pen.goto(0, -140)
    pen.pendown()
    pen.right(45)
    pen.forward(80)
    pen.backward(80)
    pen.left(90)
    pen.forward(80)
    pen.hideturtle()

    screen.exitonclick()


if __name__ == "__main__":
    draw_flower()
