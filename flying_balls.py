from tkinter import *


root = Tk()
root.geometry("300x300")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)


balls = []
global R
R = 40

for x, y, dx, dy in (100, 100, 2, 3), (250, 200, -2, 3):
    oval = canvas.create_oval(x, y, x+R, y+R, fill = 'pink')
    ball = [x, y, dx, dy, oval]
    balls.append(ball)


def tick_handler():
    for ball in balls:
        x, y, dx, dy, oval = ball
        
        if x < 0:
            dx = -dx;
            x = 0
        elif x > 300-R:
            dx = -dx
            x = 300-R
            
        if y < 0:
            dy = -dy
            y = 0
        elif y > 300-2*R:
            dy = -dy
            y = 300-2*R

        r1 = (balls[0][0]-balls[1][0])*(balls[0][0]-balls[1][0])
        r2 = (balls[0][1]-balls[1][1])*(balls[0][1]-balls[1][1])
        
        if (r1 + r2 < R*R):
             balls[0][2] = - balls[0][2]
             balls[0][3] = - balls[0][3]

             balls[1][2] = - balls[1][2]
             balls[1][3] = - balls[1][3]
             
        x = x + dx; y = y + dy
        
        canvas.move(oval, dx, dy)

        ball[0] = x
        ball[1] = y
        ball[2] = dx
        ball[3] = dy


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return

    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)


def unfreezer(event):
    global freeze
    if freeze == True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)


speed_scale = Scale(root, orient=HORIZONTAL, length=300,
               from_=0, to=10, tickinterval=1, resolution=1)

speed_scale.pack()
speed_scale.set(1);
freeze = False


root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()
