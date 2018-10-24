import graphics as gr
window=gr.GraphWin("project", 500, 500)
def draw_sky():
        sky=gr.Rectangle(gr.Point(0, 400), gr.Point(500, 0))
        sky.setFill('skyblue')
        sky.draw(window)

def draw_sea():
        sea=gr.Rectangle(gr.Point(0, 400), gr.Point(500, 500))
        sea.setFill('blue')
        sea.draw(window)

def draw_sun():
        sun=gr.Circle(gr.Point(500, 0), 60)
        sun.setFill('yellow')
        sun.draw(window)

def draw_cloud():
        cloud1=gr.Circle(gr.Point(40, 60), 20)
        cloud1.setFill('white')
        cloud1.draw(window)

        cloud2=gr.Circle(gr.Point(60, 55), 30)
        cloud2.setFill('white')
        cloud2.draw(window)

        cloud3=gr.Circle(gr.Point(90, 60), 20)
        cloud3.setFill('white')
        cloud3.draw(window)

        cloud4=gr.Circle(gr.Point(50, 75), 20)
        cloud4.setFill('white')
        cloud4.draw(window)

        cloud5=gr.Circle(gr.Point(80, 80), 20)
        cloud5.setFill('white')
        cloud5.draw(window)

        cloud6=gr.Circle(gr.Point(110, 70), 15)
        cloud6.setFill('white')
        cloud6.draw(window)

def draw_bird():
        bird1_1=gr.Line(gr.Point(200, 75), gr.Point(215, 70))
        bird1_2=gr.Line(gr.Point(215, 70), gr.Point(210, 85))
        bird1_1.draw(window)
        bird1_2.draw(window)

        bird2_1=gr.Line(gr.Point(230, 90), gr.Point(245, 85))
        bird2_2=gr.Line(gr.Point(245, 85), gr.Point(240, 100))
        bird2_1.draw(window)
        bird2_2.draw(window)

        bird3_1=gr.Line(gr.Point(225, 65), gr.Point(240, 60))
        bird3_2=gr.Line(gr.Point(240, 60), gr.Point(235, 75))
        bird3_1.draw(window)
        bird3_2.draw(window)

def draw_ship():
        ship_side=gr.Polygon(gr.Point(80, 420), gr.Point(180, 420), gr.Point(250, 370), gr.Point(50, 370))
        ship_side.setFill('grey')
        ship_side.draw(window)

        ship_deck=gr.Rectangle(gr.Point(80, 370), gr.Point(140, 320))
        ship_deck.setFill('white')
        ship_deck.draw(window)

        ship_window1=gr.Circle(gr.Point(95, 345), 5)
        ship_window1.setFill('black')
        ship_window1.draw(window)

        ship_window2=gr.Circle(gr.Point(125, 345), 5)
        ship_window2.setFill('black')
        ship_window2.draw(window)

        ship_flag=gr.Rectangle(gr.Point(125, 305), gr.Point(135, 315))
        ship_flag.setFill('red')
        ship_flag.draw(window)

        ship_flagline=gr.Line(gr.Point(125, 320), gr.Point(125, 315))
        ship_flagline.draw(window)

def draw_palm():
        palm_ground=gr.Polygon(gr.Point(260, 460), gr.Point(460, 460), gr.Point(360, 420))
        palm_ground.setFill('brown')
        palm_ground.draw(window)

        palm1=gr.Polygon(gr.Point(360, 420), gr.Point(345, 395), gr.Point(375, 395))
        palm1.setFill('brown')
        palm1.draw(window)

        palm2=gr.Polygon(gr.Point(360, 395), gr.Point(345, 370), gr.Point(375, 370))
        palm2.setFill('brown')
        palm2.draw(window)

        palm3=gr.Polygon(gr.Point(360, 370), gr.Point(345, 345), gr.Point(375, 345))
        palm3.setFill('brown')
        palm3.draw(window)

        palm4=gr.Polygon(gr.Point(360, 345), gr.Point(345, 320), gr.Point(375, 320))
        palm4.setFill('brown')
        palm4.draw(window)

        palm5=gr.Polygon(gr.Point(360, 320), gr.Point(345, 295), gr.Point(375, 295))
        palm5.setFill('brown')
        palm5.draw(window)

        palm6=gr.Polygon(gr.Point(360, 295), gr.Point(345, 270), gr.Point(375, 270))
        palm6.setFill('brown')
        palm6.draw(window)

        palm7=gr.Polygon(gr.Point(360, 270), gr.Point(345, 245), gr.Point(375, 245))
        palm7.setFill('brown')
        palm7.draw(window)

        palm_list1=gr.Polygon(gr.Point(360, 245), gr.Point(270, 235), gr.Point(330, 290))
        palm_list1.setFill('green')
        palm_list1.draw(window)

        palm_list2=gr.Polygon(gr.Point(360, 245), gr.Point(275, 205), gr.Point(280, 170))
        palm_list2.setFill('green')
        palm_list2.draw(window)

        palm_list3=gr.Polygon(gr.Point(360, 245), gr.Point(350, 180), gr.Point(370, 180))
        palm_list3.setFill('green')
        palm_list3.draw(window)

        palm_list4=gr.Polygon(gr.Point(360, 245), gr.Point(420, 205), gr.Point(400, 165))
        palm_list4.setFill('green')
        palm_list4.draw(window)

        palm_list5=gr.Polygon(gr.Point(360, 245), gr.Point(440, 235), gr.Point(370, 290))
        palm_list5.setFill('green')
        palm_list5.draw(window)

def draw_picture():
        draw_sky()
        draw_sea()
        draw_sun()
        draw_cloud()
        draw_ship()
        draw_bird()
        draw_palm()

draw_picture()



window.getMouse()
window.close()
