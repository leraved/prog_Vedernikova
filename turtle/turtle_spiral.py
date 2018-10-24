import turtle
turtle.shape('turtle')
def polokr (l:float):
        for x in range (180):
                turtle.forward(l)
                turtle.left(1)

l=0.1
for x in range (20):
        polokr (l)
        l+=0.3
