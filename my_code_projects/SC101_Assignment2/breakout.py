"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 12         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    global NUM_LIVES
    score = 0
    while True:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.reverse_dx()
        if graphics.ball.y <= 0:
            graphics.reverse_dy()
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            if NUM_LIVES > 1:
                NUM_LIVES -= 1
                graphics.restart()
                graphics.set_ball_position()
            else:
                break
        obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj2 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.height, graphics.ball.y)
        obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
        obj4 = graphics.window.get_object_at(graphics.ball.x+graphics.ball.height, graphics.ball.y+graphics.ball.height)
        if obj1 is not None:
            if obj1.y < graphics.get_paddle_offset():
                graphics.window.remove(obj1)
                graphics.reverse_dy()
                score += 1
        elif obj2 is not None:
            if obj2.y < graphics.get_paddle_offset():
                graphics.window.remove(obj2)
                graphics.reverse_dy()
                score += 1
        elif obj3 is not None:
            if obj3.y < graphics.get_paddle_offset():
                graphics.window.remove(obj3)
                graphics.reverse_dy()
                score += 1
            else:
                graphics.reverse_dy()
        elif obj4 is not None:
            if obj4.y < graphics.get_paddle_offset():
                graphics.window.remove(obj4)
                graphics.reverse_dy()
                score += 1
            else:
                graphics.reverse_dy()
        if score == graphics.total_bricks():
            break


if __name__ == '__main__':
    main()
