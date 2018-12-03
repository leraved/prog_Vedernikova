# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 23:58:06 2018

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
        
    x += 0.5* a
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
    
castle(300, 300, 80, 30)

canv.mainloop()
