from tkinter import *

root = Tk()

def time_handler():
        global freeze
        speed = speed_scale.get()
        if speed == 0:
                print ("Заморозка")
                freeze = True
        else:       
                print ("Значение скорости:", speed)
                sleep_dt = 1100 - 100*speed
                root.after(sleep_dt, time_handler)
        
def unfreezer():
        global freeze
        if freeze == True:
                speed = speed_scale.get()
                if speed != 0:
                        freeze = False
                        root.after(0, time_handler)
        
        
speed_scale = Scale(root, orient=HORIZONTAL, length=300, from_ = 0, to = 10,
                     tickinterval=1, resolution=1)

speed_scale.pack()

speed_scale.set(1)
freeze = False

speed_scale.bind("<Motion>", unfreezer)
root.after(10, time_hadler)

root.mainloop()
