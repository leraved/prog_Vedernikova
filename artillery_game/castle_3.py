# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:12:21 2018

@author: Валерия
"""

from tkinter import*

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

def castle(x, y, a, b):
    """a - длина кирпичика, b - ширина"""
    for _ in range(3):
        for _ in range(2):
            canv.create_rectangle(x, y, x + a, y - b, fill = 'grey', outline = 'black')
            x += a
    
        x -= 2 * a
        y -= 2 * b
    
    y += 5 * b
    
    for _ in range(3):  
        for _ in range(2):
            canv.create_rectangle(x, y, x + 0.5 * a, y - b, fill = 'grey', outline = 'black')
            x += 1.5 * a
        
        x -= 3 * a
        y -= 2 * b
        
    x += 0.5 * a
    y += 6 * b
    
    for _ in range(2): 
        canv.create_rectangle(x, y, x + a, y - b, fill = 'grey', outline = 'black')
        y -= 2 * b
    
    x -= 0.25 * a
    y -= b
    
    for _ in range(2):
        canv.create_line(x, y, x, y - 0.25 * b)
        canv.create_rectangle(x, y - 0.25 * b, x + 0.2 * a, y - 0.5 * b, fill = 'red', outline = 'red')
        x += 1.5 * a
    
    x -= 4.75 * a
    y += 4 * b
    
    for _ in range(2):
        canv.create_oval(x, y, x + 1.5* a, y - 2 * b, fill = 'grey', outline = 'black')
        y += 2 * b

        for _ in range(2):
            canv.create_rectangle(x, y, x + a, y - b, fill = 'grey', outline = 'black')
            y -= 2 * b
    
        y += 4 * b
        x += a
        
        for _ in range(2):
            canv.create_rectangle(x, y, x + 0.5 * a, y - b, fill = 'grey', outline = 'black')
            y -= 2 * b
    
        y += 3 * b
        x -= a
        canv.create_rectangle(x, y, x + 0.5 * a, y - b, fill = 'grey', outline = 'black')
        x += 0.5 * a
        canv.create_rectangle(x, y, x + a, y - b, fill = 'grey', outline = 'black')
        x += 3 * a
        y -= b
castle(300, 400, 100, 40)
canv.mainloop()
