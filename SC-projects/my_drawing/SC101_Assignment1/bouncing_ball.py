"""
File: bouncing ball
Name: Geoffrey
-------------------------

"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

i = 0
click = 0

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(fall)



def fall(mouse):
    global i, click
    click += 1
    if click == 1:  # to make sure that I can click without starting again when the ball is going
        bbal = window.get_object_at(START_X+SIZE/2, START_Y)  # start from second round have to delete the ball image
        if bbal is not None and i < 3:
            window.remove(bbal)
        if i < 3:  # to set the total rounds we can play the ball
            ball = GOval(SIZE, SIZE)
            ball.filled = True
            window.add(ball, START_X, START_Y)
            while True:
                global VX, GRAVITY
                ball.move(VX, GRAVITY)
                if ball.y > window.height:
                    GRAVITY = -GRAVITY * REDUCE
                pause(DELAY)
                GRAVITY += 1
                if ball.x > window.width:
                    window.clear()
                    click = 0
                    break
            window.add(ball, START_X, START_Y)
            i += 1  # i add 1 to accumulate the amount of rounds
        else:
            pass



if __name__ == "__main__":
    main()
