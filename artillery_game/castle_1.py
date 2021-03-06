# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 14:54:03 2018

@author: Валерия
"""

from tkinter import*

root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg = 'white')
canv.pack(fill = BOTH, expand = 1)

def castle(x, y, a, b): 
    """a - длина кирпичика, b - ширина"""
    for _ in range(2):
        for _ in range(2):
            canv.create_rectangle(x, y, x + a, y - b, fill = 'grey', outline = 'black')
            x += a
    
        x -= 2 * a
        y -= 2 * b
    
    y += 3 * b
    
    for _ in range(2):  
        for _ in range(2):
            canv.create_rectangle(x, y, x + 0.5 * a, y - b, fill = 'grey', outline = 'black')
            x += 1.5 * a
        
        x -= 3 * a
        y -= 2 * b
        
    x += 0.5 * a
    y += 4 * b
    canv.create_rectangle(x, y, x + a, y - b, fill = 'grey', outline = 'black')
    

castle(300, 300, 50, 20)

canv.mainloop()
