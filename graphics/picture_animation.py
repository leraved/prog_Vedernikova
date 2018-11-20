import graphics as gr
import random
import time

window = gr.GraphWin("project", 500, 500)

distancex = [7, 9, 10, -9, -10, -5, -7, 12, -12]
distancey = [7, 9, 10, -9, -10, -5, -7, 12, -12]
radius = [15, 16, 17, 18, 19, 20]


def draw_sky():
        sky = gr.Rectangle(gr.Point(0, 400), gr.Point(500, 0))
        sky.setFill('skyblue')
        sky.draw(window)
        

def draw_sea():
        sea = gr.Rectangle(gr.Point(0, 400), gr.Point(500, 500))
        sea.setFill('blue')
        sea.setOutline('blue')
        sea.draw(window)


def draw_sun():
        global sun
        sun = gr.Circle(gr.Point(440, 50), 40)
        sun.setFill('yellow')
        sun.setOutline('yellow')
        sun.draw(window)


def draw_cloud(x, y):
        for _ in range(5):
                r = random.choice(radius)
                dsx = random.choice(distancex)
                dsy = random.choice(distancey)
                cloud = gr.Circle(gr.Point(x + dsx, y + dsy), r)
                cloud.setOutline('white')
                cloud.setFill('white')
                cloud.draw(window)


def draw_birds(x, y):
        global bird1_1
        global bird1_2
        global bird2_1
        global bird2_2
        global bird3_1
        global bird3_2
        
        bird1_1 = gr.Line(gr.Point(x, y), gr.Point(x+15, y-5))
        bird1_2 = gr.Line(gr.Point(x+15, y-5), gr.Point(x+10, y+10))
        bird1_1.draw(window)
        bird1_2.draw(window)

        bird2_1 = gr.Line(gr.Point(x+30, y+15), gr.Point(x+45, y+10))
        bird2_2 = gr.Line(gr.Point(x+45, y+10), gr.Point(x+40, y+25))
        bird2_1.draw(window)
        bird2_2.draw(window)

        bird3_1 = gr.Line(gr.Point(x+25, y-10), gr.Point(x+40, y-15))
        bird3_2 = gr.Line(gr.Point(x+40, y-15), gr.Point(x+35, y))
        bird3_1.draw(window)
        bird3_2.draw(window)


def draw_ship_side():
        global ship_side1
        
        ship_side1 = gr.Polygon(gr.Point(80, 420), gr.Point(180, 420), gr.Point(250, 370), gr.Point(50, 370))
        ship_side1.setFill('grey')
        ship_side1.setOutline('grey')
        ship_side1.draw(window)


def draw_ship_deck():
        global ship_deck1
        
        ship_deck1 = gr.Rectangle(gr.Point(80, 370), gr.Point(140, 320))
        ship_deck1.setFill('white')
        ship_deck1.setOutline('white')
        ship_deck1.draw(window)


def draw_ship_windows():
        global ship_window1
        global ship_window2
        
        ship_window1 = gr.Circle(gr.Point(95, 345), 5)
        ship_window1.setFill('black')
        ship_window1.draw(window)

        ship_window2 = gr.Circle(gr.Point(125, 345), 5)
        ship_window2.setFill('black')
        ship_window2.draw(window)


def draw_ship_flag():
        global ship_flag_canvas
        global ship_flag_line

        ship_flag_canvas = gr.Rectangle(gr.Point(125, 305), gr.Point(135, 315))
        ship_flag_canvas.setFill('red')
        ship_flag_canvas.setOutline('red')
        ship_flag_canvas.draw(window)

        ship_flag_line = gr.Line(gr.Point(125, 320), gr.Point(125, 315))
        ship_flag_line.draw(window)

        
def draw_ship():
        draw_ship_side()
        draw_ship_deck()
        draw_ship_windows()
        draw_ship_flag()


def draw_palm_trunk(y1, y2, y3):
        for _ in range (7):
                palm1 = gr.Polygon(gr.Point(360, y1), gr.Point(345, y2), gr.Point(375, y3))
                palm1.setFill('brown')
                palm1.setOutline('brown')
                palm1.draw(window)
                y1=y1-25
                y2=y2-25
                y3=y3-25
        

def draw_palm_ground():
        palm_ground = gr.Polygon(gr.Point(260, 460), gr.Point(460, 460), gr.Point(360, 420))
        palm_ground.setFill('brown')
        palm_ground.setOutline('brown')
        palm_ground.draw(window)


def draw_palm_list(x1, y1, x2, y2):
        palm_list = gr.Polygon(gr.Point(360, 245), gr.Point(x1, y1), gr.Point(x2, y2))
        palm_list.setFill('green')
        palm_list.setOutline('green')
        palm_list.draw(window)
        

def draw_palm_lists():
        draw_palm_list(270, 235, 330, 290)
        draw_palm_list(275, 205, 280, 170)
        draw_palm_list(350, 180, 370, 180)
        draw_palm_list(420, 205, 400, 165)
        draw_palm_list(440, 235, 370, 290)

        
def draw_palm():
        draw_palm_ground()
        draw_palm_trunk(420, 395, 395)
        draw_palm_lists()


def draw_picture():
        draw_sky()
        draw_sea()
        draw_sun()
        draw_cloud(400, 90)
        draw_cloud(50, 60)
        draw_ship()
        draw_birds(200, 55)
        draw_birds(280, 90)
        draw_birds(250, 50)
        draw_palm()
        
        for _ in range(20):
                sun.move(-1, 0)
                
                bird1_1.move(1, -1)
                bird1_2.move(1, -1)
                bird2_1.move(1, -1)
                bird2_2.move(1, -1)
                bird3_1.move(1, -1)
                bird3_2.move(1, -1)
                
                ship_deck1.move(1, 0)
                ship_side1.move(1, 0)
                ship_flag_line.move(1, 0)
                ship_flag_canvas.move(1, 0)
                ship_window1.move(1, 0)
                ship_window2.move(1, 0)
                
                time.sleep(0.2)
        

draw_picture()


window.getMouse()
window.close()

