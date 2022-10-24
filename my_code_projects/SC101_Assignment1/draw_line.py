"""
File: 
Name:
-------------------------
TODO:
"""


from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 5


window = GWindow()
n = 0
circle = GOval(0, 0)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global n
    global circle
    n += 1
    if n % 2 != 0:
        circle = GOval(SIZE * 2, SIZE * 2, x=mouse.x - SIZE, y=mouse.y - SIZE)
        window.add(circle)
    if n % 2 == 0:
        line = GLine(circle.x + SIZE, circle.y + SIZE, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)


if __name__ == "__main__":
    main()
