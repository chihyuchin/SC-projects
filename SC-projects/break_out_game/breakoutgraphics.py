"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.

COUNT = 0
I = 0
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING, __num_lives = NUM_LIVES,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.space = paddle_offset

        # Create a paddle.
        self.pad = GRect(paddle_width, paddle_height)
        self.pad.filled = True
        self.window.add(self.pad, (self.window_width-paddle_width)/2, self.window_height-self.space)
        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window_width-ball_radius*2)/2, (self.window_height-ball_radius*2)/2)
        self.radius = ball_radius
        # Default initial velocity for the ball.
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Initialize our mouse listeners.
        onmousemoved(self.move)
        onmouseclicked(self.start)
        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                k = brick_rows/5
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if k*0 <= j <= k * 1 - 1:
                    self.brick.fill_color = 'red'
                elif k*1 <= j <= k * 2 - 1:
                    self.brick.fill_color = 'orange'
                elif k * 2 <= j <= k * 3 - 1:
                    self.brick.fill_color = 'yellow'
                elif k * 3 <= j <= k * 4 - 1:
                    self.brick.fill_color = 'green'
                elif k * 4 <= j <= k * 5 - 1:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, (brick_width+brick_spacing)*i, (brick_height+brick_spacing)*j)

        # SET
        self.first = self.window.get_object_at(self.ball.x, self.ball.y)
        self.second = self.window.get_object_at(self.ball.x+self.radius*2, self.ball.y)
        self.third = self.window.get_object_at(self.ball.x, self.ball.y+self.radius*2)
        self.forth = self.window.get_object_at(self.ball.x+self.radius*2, self.ball.y+self.radius*2)

        # Clear
        self.count = COUNT
        self.i = I

    def kill_brick(self):
        self.count = 0
        self.first = self.window.get_object_at(self.ball.x, self.ball.y)
        self.second = self.window.get_object_at(self.ball.x+self.radius*2, self.ball.y)
        self.third = self.window.get_object_at(self.ball.x, self.ball.y+self.radius*2)
        self.forth = self.window.get_object_at(self.ball.x+self.radius*2, self.ball.y+self.radius*2)

        if self.first is not None and self.first is not self.pad:
            self.count += 1

        elif self.second is not None and self.second is not self.pad:
            self.count += 1

        elif self.third is not None and self.third is not self.pad:
            self.count += 1

        elif self.forth is not None and self.forth is not self.pad:
            self.count += 1

        return self.count




    def move(self, mouse):
        self.pad.x = mouse.x-self.pad.width/2
        if mouse.x < 0:
            self.pad.x = 0
        elif mouse.x > self.window.width:
            self.pad.x = self.window.width-self.pad.width

    # Getter
    def get_x_speed(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    #Setter
    def set_x_speed(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # Getter
    def get_y_speed(self):
        return self.__dy

    # start click
    def start(self, mouse):
        self.i += 1

