import turtle
t = turtle.Turtle()
t.speed(0)

colors = ["red","orange","yellow","green","blue","purple"]

for i in range(2000):
    t.pencolor(colors[i % 6])
    t.forward(i)
    t.left(59)

turtle.done()