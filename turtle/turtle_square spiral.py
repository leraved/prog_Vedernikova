import turtle

turtle.shape ('turtle')

l = 10

for x in range(20):
        for y in range(2):
                turtle.forward(l)
                turtle.left(90)
        l = l + 5
