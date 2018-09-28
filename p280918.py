import graphics as gr
window=gr.GraphWin("Russian game", 500, 500)
my_circle=gr.Circle(gr.Point(50,50), 10)
my_circle.draw(window)
window.getMouse()
window.close()
