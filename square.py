import turtle  
t=turtle.Turtle()
def square(t,len):
    for i in range(4):
        t.forward(len)
        t.left(90)
square(t,100)
turtle.done()