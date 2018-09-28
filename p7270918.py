import turtle
turtle.shape('turtle')
def fun (l:int, n:int):
        if (n==0):
                turtle.left(60)
                return
        x=l/(n+1)
        for i in range(n):
                turtle.forward(l)
                turtle.left(60)
                draw(0.5*x*(n-i-1), n-i-1)
                turtle.right(120)
        turtle.forward(x)

draw(100, 4)
