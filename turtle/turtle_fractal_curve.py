import turtle

turtle.shape('turtle')
turtle.speed('fastest')


def fractal(l, n):
    if n == 0:
        turtle.forward(l)
        return
    
    x = l / 3
    fractal(x, n - 1)
    turtle.left(60)
    fractal(x, n - 1)
    turtle.right(120)
    fractal(x, n - 1)
    turtle.left(60)
    fractal(x, n - 1)


fractal(270, 4)
    
        
