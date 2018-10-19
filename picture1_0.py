import random
from tkinter import *

colors = ['green', 'red', 'blue', 'grey', 'pink', 'yellow']
rs = [10, 20, 25, 70, 40, 50]

def circle():
        R = random.choice(rs)
        x = random.randint(100, 700)
        y = random.randint(100, 500)
        canv.create_oval(x-R, y-R, x+R, y+R, fill=random.choice(colors))

def tick():
        root.after(1000, tick)
        canv.delete(ALL)
        circle()
        
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

root.after_idle(tick)

root.mainloop()
