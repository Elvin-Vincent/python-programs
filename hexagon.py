import turtle
t=turtle.Turtle()
def hexagon(t,len):
    for i in range(6):
        t.forward(len)
        t.left(60)
hexagon(t,100)
turtle.done()