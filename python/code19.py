import turtle
t = turtle.Turtle()
t.speed(0)
for i in range(36):
    for j in range(45):
        t.forward(100)
        t.right(90)
    t.right(10)
turtle.done()