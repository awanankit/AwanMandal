import turtle
t = turtle.Turtle()
t.speed(0)

colors = ["red","green"]
 
for i in range(100):
    t.pencolor(colors[i % 6])
    t.circle(8)
    t.left(5) 

turtle.done()
