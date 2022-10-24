"""
File: 
Name:
-------------------------
TODO:
"""


from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked


VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.8
START_X = 30
START_Y = 40


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
switch = 0
count = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball)
    onmouseclicked(move)


def move(click):
    if click:
        global ball
        global count
        global switch
        if ball.x == START_X and ball.y == START_Y:
            switch = 1
            count += 1
            vy = 0
            if switch == 1 and count <= 3:
                while True:
                    ball.move(VX, vy)
                    vy += GRAVITY
                    if ball.y + SIZE >= window.height:
                        ball.y = window.height - SIZE  # 不要跑出視窗
                        vy = -vy * REDUCE
                    pause(DELAY)
                    if ball.x >= window.width:
                        ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
                        ball.filled = True
                        window.add(ball)
                        switch = 0
                        return switch


if __name__ == "__main__":
    main()
