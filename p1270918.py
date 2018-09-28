import turtle
turtle.shape('turtle')
def mnungle (n:int, l:int):
        for y in range(n):
                turtle.left(180-180*(n-2)//n)
                turtle.forward(l)
n=3
l=10
h1=5
h2=5
for x in range(10):
        mnungle (n, l)
        turtle.penup()
        turtle.forward(h1)
        turtle.right(90)
        turtle.forward(h2)
        turtle.left(90)
        turtle.pendown()
        n=n+1
        l=l+5
        h1=h1+3
