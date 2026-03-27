import turtle
t = turtle.Turtle()
t.speed(0)

for i in range(50):
    t.circle(i * 5)
    t.right(45)

turtle.done()