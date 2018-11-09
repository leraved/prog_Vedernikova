import turtle

turtle.shape('turtle')


def sq(l:int):
        for _ in range (4):
                turtle.forward(l)
                turtle.left(90)


l = 10

for _ in range (10):
        sq(l)
        turtle.penup()
        turtle.left(180)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
        turtle.left(90)
        l = l + 20
        turtle.pendown()
