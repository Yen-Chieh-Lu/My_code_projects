"""
File: 
Name:
----------------------
TODO: Draw pictures.
"""


from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: 小朋友學畫畫

    大家小時候一定都畫過的一幅畫，
    剛學會用python繪圖，就像剛學會畫畫的小孩><
    """
    window = GWindow(800, 500)
    sky = GRect(800, 400)
    sky.filled = True
    sky.color = 'dodgerblue'
    sky.fill_color = 'dodgerblue'
    window.add(sky)
    ground = GRect(800, 100, x=0, y=400)
    ground.filled = True
    ground.fill_color = 'green'
    window.add(ground)
    house = GRect(130, 130, x=520, y=270)
    house.filled = True
    house.fill_color = 'tan'
    window.add(house)
    roof = GPolygon()
    roof.add_vertex((515, 270))
    roof.add_vertex((655, 270))
    roof.add_vertex((585, 180))
    roof.filled = True
    roof.fill_color = 'red'
    window.add(roof)
    sun = GOval(80, 80, x=650, y=50)
    sun.filled = True
    sun.color = 'yellow'
    sun.fill_color = 'yellow'
    window.add(sun)
    door = GRect(40, 50, x=565, y=350)
    door.filled = True
    door.fill_color = 'peru'
    window.add(door)
    handle = GOval(7, 7, x=570, y=370)
    handle.filled = True
    handle.fill_color = 'gold'
    window.add(handle)
    window1 = GRect(40, 40, x=535, y=290)
    window1.filled = True
    window1.fill_color = 'silver'
    window.add(window1)
    window2 = GRect(40, 40, x=598, y=290)
    window2.filled = True
    window2.fill_color = 'silver'
    window.add(window2)
    line1 = GRect(40, 1, x=535, y=310)
    window.add(line1)
    line2 = GRect(1, 40, x=555, y=290)
    window.add(line2)
    line3 = GRect(40, 1, x=598, y=310)
    window.add(line3)
    line4 = GRect(1, 40, x=618, y=290)
    window.add(line4)
    cloud1 = GOval(70, 70, x=60, y=60)
    cloud1.filled = True
    cloud1.fill_color = 'white'
    cloud1.color = 'white'
    window.add(cloud1)
    cloud2 = GOval(70, 70, x=110, y=60)
    cloud2.filled = True
    cloud2.fill_color = 'white'
    cloud2.color = 'white'
    window.add(cloud2)
    cloud3 = GOval(70, 70, x=160, y=60)
    cloud3.filled = True
    cloud3.fill_color = 'white'
    cloud3.color = 'white'
    window.add(cloud3)
    cloud4 = GOval(70, 70, x=300, y=100)
    cloud4.filled = True
    cloud4.fill_color = 'white'
    cloud4.color = 'white'
    window.add(cloud4)
    cloud5 = GOval(70, 70, x=350, y=100)
    cloud5.filled = True
    cloud5.fill_color = 'white'
    cloud5.color = 'white'
    window.add(cloud5)
    cloud6 = GOval(70, 70, x=400, y=100)
    cloud6.filled = True
    cloud6.fill_color = 'white'
    cloud6.color = 'white'
    window.add(cloud6)
    body = GOval(20, 60, x=290, y=320)
    body.filled = True
    body.fill_color = 'gray'
    window.add(body)
    head = GOval(40, 40, x=280, y=300)
    head.filled = True
    head.fill_color = 'gray'
    window.add(head)
    l_hand = GPolygon()
    l_hand.add_vertex((290, 350))
    l_hand.add_vertex((265, 325))
    l_hand.add_vertex((260, 330))
    l_hand.filled = True
    l_hand.fill_color = 'gray'
    window.add(l_hand)
    r_hand = GPolygon()
    r_hand.add_vertex((310, 350))
    r_hand.add_vertex((335, 325))
    r_hand.add_vertex((330, 320))
    r_hand.filled = True
    r_hand.fill_color = 'gray'
    window.add(r_hand)
    l_foot = GPolygon()
    l_foot.add_vertex((291, 370))
    l_foot.add_vertex((275, 400))
    l_foot.add_vertex((270, 400))
    l_foot.filled = True
    l_foot.fill_color = 'gray'
    window.add(l_foot)
    r_foot = GPolygon()
    r_foot.add_vertex((309, 370))
    r_foot.add_vertex((320, 400))
    r_foot.add_vertex((315, 400))
    r_foot.filled = True
    r_foot.fill_color = 'gray'
    window.add(r_foot)


if __name__ == '__main__':
    main()
