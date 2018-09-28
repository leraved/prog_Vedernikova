import turtle
turtle.shape('turtle')
def prm (n:int, l:int):
        turtle.forward(l)
        turtle.left(180-180//n)
        return
n=11
l=100
turtle.left(180)
for x in range(n):
        prm(n, l)
        
