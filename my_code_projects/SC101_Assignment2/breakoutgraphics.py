"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
n = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset
                        - paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window_width-self.ball.height)/2, y=(self.window_height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.reset_ball)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for i in range(brick_cols):
            start_x = 0
            start_x += i*(brick_width + brick_spacing)
            start_y = brick_offset
            for j in range(brick_rows):
                start_y += (brick_height + brick_spacing)
                brick = GRect(brick_width, brick_height, x=start_x, y=start_y)
                brick.filled = True
                if start_y <= brick_offset + 2 * (brick_height + brick_spacing):
                    brick.fill_color = 'red'
                elif start_y <= brick_offset + 4 * (brick_height + brick_spacing):
                    brick.fill_color = 'orange'
                elif start_y <= brick_offset + 6 * (brick_height + brick_spacing):
                    brick.fill_color = 'yellow'
                elif start_y <= brick_offset + 8 * (brick_height + brick_spacing):
                    brick.fill_color = 'green'
                elif start_y <= brick_offset + 10 * (brick_height + brick_spacing):
                    brick.fill_color = 'blue'
                self.window.add(brick)

    def move_paddle(self, mouse):
        self.paddle.x = mouse.x - PADDLE_WIDTH / 2
        if mouse.x - PADDLE_WIDTH / 2 <= 0:
            self.paddle.x = 0
        if mouse.x + PADDLE_WIDTH / 2 >= self.window_width:
            self.paddle.x = self.window_width - PADDLE_WIDTH

    def reset_ball(self, clicked):
        global n
        if clicked:
            n += 1
            if n == 1:
                self.set_ball_position()
                self.__dy = INITIAL_Y_SPEED
                self.__dx = random.randint(1, MAX_X_SPEED)
                if random.random() > 0.5:
                    self.__dx = -self.__dx
                self.window.add(self.ball)

    def set_ball_position(self):
        self.ball.x = (self.window_width-self.ball.height)/2
        self.ball.y = (self.window_height-self.ball.height)/2
        self.__dx = 0
        self.__dy = 0
        self.window.add(self.ball)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def reverse_dx(self):
        self.__dx = -self.__dx

    def reverse_dy(self):
        self.__dy = -self.__dy

    def get_paddle_offset(self):
        return self.window_height - PADDLE_OFFSET - PADDLE_HEIGHT - 2*BALL_RADIUS

    @staticmethod
    def restart():
        global n
        n = 0
        return n

    @staticmethod
    def total_bricks():
        return BRICK_ROWS * BRICK_COLS
