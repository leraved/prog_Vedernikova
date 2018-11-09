import turtle

turtle.shape('turtle')


def semicircle (l:float):
        for _ in range (180):
                turtle.forward(l)
                turtle.left(1)


l = 0.1

for _ in range (20):
        semicircle (l)
        l += 0.3
