import turtle
t=turtle.Turtle()
def pentagon(t,len):
    for i in range(5):
        t.forward(len)
        t.left(72)
pentagon(t,100)
turtle.done()