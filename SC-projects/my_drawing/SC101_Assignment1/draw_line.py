"""
File: draw line
Name: Geoffrey
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 5

window = GWindow()

i = 0
record_x = 0
record_y = 0

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(paint)



def paint(mouse):
    global i, record_x, record_y
    point = GOval(SIZE, SIZE)
    point.color = True
    window.add(point, mouse.x, mouse.y)
    if i % 2 == 0:  # to check the if its a even point or not
        record_x = point.x
        record_y = point.y
    l_point = window.get_object_at(record_x+SIZE/2, record_y)  # +Size to catch the top of the point
    if i % 2 != 0:
        window.remove(point)
        window.remove(l_point)
    line = GLine(record_x, record_y, mouse.x, mouse.y)
    window.add(line)
    i += 1




if __name__ == "__main__":
    main()
