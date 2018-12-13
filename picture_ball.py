import random
from tkinter import *

colors = ['green', 'red', 'blue', 'grey', 'pink', 'yellow']
rs = [10, 20, 25, 70, 40, 50]
"""радиусы шариков"""
global goals
goals = 0

def circle():
        global x1, y1, R
        """ координаты центра шарика:x1 - по Ох, y1 - по Оу""" 
        R = random.choice(rs)
        """радиус шарика"""
        x1 = random.randint(100, 700)
        y1 = random.randint(100, 500)
        canv.create_oval(x1 - R, y1 - R, x1 + R, y1 + R, fill = random.choice(colors))


def left_click(event):
        x = event.x
        y = event.y
        if ((x >= x1 - R) and (x <= x1 + R) and (y >= y1 - R) and (y >= y1 - R)):
            global goals
            goals += 1
        else:
            goals -= 1
        
            
def tick():
        root.after(1000, tick)
        canv.delete(ALL)
        circle()
        canv.create_text(400, 300, text = goals, font = 'Arial 25')
        
        
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill = BOTH, expand = 1)

root.bind ('<Button-1>', left_click)
root.after_idle(tick)

root.mainloop()
