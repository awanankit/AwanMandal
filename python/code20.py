import turtle
t = turtle.Turtle()
t.speed(0)

for i in range(36):
    for j in range(2):
        t.circle(100,90)
        t.circle(100//2,90)
    t.left(10)

turtle.done()