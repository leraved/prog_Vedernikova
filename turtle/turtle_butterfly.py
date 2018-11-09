import turtle

turtle.shape('turtle')


def okr (l:int):
        turtle.left(90)
        for _ in range(360):
                turtle.forward(l)
                turtle.left(1)
        for _ in range(360):
                turtle.forward(l)
                turtle.right(1)
        turtle.right(90)
        return


l = 0.5

for x in range(5):
        okr(l)
        l = l + 0.5
