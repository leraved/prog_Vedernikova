import turtle

turtle.shape('turtle')


def okr(l1:int, l2:int):
        for _ in range(180):
                turtle.forward(l1)
                turtle.right(1)
        for _ in range(180):
                turtle.forward(l2)
                turtle.right(1)
        return


l1 = 0.5
l2 = 0.2

turtle.left(90)

for x in range(3):
        okr(l1, l2)
        
