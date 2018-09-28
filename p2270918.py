import turtle
turtle.shape('turtle')
def okr (l:int):
        for x in range(360):
                turtle.forward(l)
                turtle.left(1)
        for x in range(360):
                turtle.forward(l)
                turtle.right(1)
        return
l=1
for y in range(3):
        okr(l)
        turtle.left(120)
