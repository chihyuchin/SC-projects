"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics


FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3




def main():

    graphics = BreakoutGraphics()
    # Add animation loop here!
    dx = graphics.get_x_speed()
    dy = graphics.get_y_speed()
    global NUM_LIVES

    while True:
        pause(FRAME_RATE)
        if graphics.i >= 1:
            if NUM_LIVES > 0:
                graphics.ball.move(dx, dy)
                graphics.kill_brick()
                if graphics.first or graphics.second or graphics.third or graphics.forth is graphics.pad:
                    dy = -7
                if graphics.ball.x <= 0 or graphics.ball.x > graphics.window.width-graphics.radius*2:
                    dx = -dx
                elif graphics.ball.y <= 0:
                    dy = -dy
                if graphics.ball.y > graphics.window_height - graphics.space:
                    pass
                if graphics.ball.y > graphics.window_height:
                    NUM_LIVES -= 1
                    graphics.i = 0
                    graphics.window.add(graphics.ball, (graphics.window_width-graphics.radius*2)/2, (graphics.window_height-graphics.radius*2)/2)
                elif graphics.count % 2 == 1:
                    if graphics.first is not None and graphics.first is not graphics.pad:
                        graphics.window.remove(graphics.first)
                        dx = graphics.get_x_speed()
                        dy = -dy
                    elif graphics.second is not None and graphics.second is not graphics.pad:
                        graphics.window.remove(graphics.second)
                        dx = graphics.get_x_speed()
                        dy = -dy
                    elif graphics.third is not None and graphics.third is not graphics.pad:
                        graphics.window.remove(graphics.third)
                        dx = graphics.get_x_speed()
                        dy = -dy
                    elif graphics.forth is not None and graphics.forth is not graphics.pad:
                        graphics.window.remove(graphics.forth)
                        dx = graphics.get_x_speed()
                        dy = -dy
            else:
                break






if __name__ == '__main__':
    main()
