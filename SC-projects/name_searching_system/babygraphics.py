"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """

    space = (CANVAS_WIDTH//len(YEARS))
    p = YEARS.index(year_index)
    x = GRAPH_MARGIN_SIZE+p * space + TEXT_DX
    return int(x)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    w = canvas
    space = (CANVAS_WIDTH//len(YEARS))
    line_end = CANVAS_WIDTH-GRAPH_MARGIN_SIZE
    height_end = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
    w.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, line_end, GRAPH_MARGIN_SIZE, fill='black')
    w.create_line(GRAPH_MARGIN_SIZE, height_end, line_end, height_end, fill='black')
    for i in range(len(YEARS)):
        w.create_line(GRAPH_MARGIN_SIZE+i*space, 0, GRAPH_MARGIN_SIZE+i*space, CANVAS_HEIGHT)
        w.create_text(GRAPH_MARGIN_SIZE+i*space+TEXT_DX, height_end, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    w = canvas
    name_box = []
    rank_box = []
    x_box = []
    count = 0

    for i in range(len(lookup_names)):  # to create list for drawing lines and text
        if count >= 4:
            count = 0
        for j in range(len(YEARS)):
            name = lookup_names[i]
            year = YEARS[j]
            x_spot = get_x_coordinate(CANVAS_WIDTH, year)
            if str(year) not in name_data[name]:
                rank = MAX_RANK
                rank_box.append(rank)
            else:
                rank = name_data[name][str(year)]
                rank_box.append(rank)
                name_box.append(name)
            x_box.append(x_spot)

        for k in range(11):  # to create lines
            w.create_line(x_box[k] - TEXT_DX, GRAPH_MARGIN_SIZE + int(rank_box[k]) * 0.56, x_box[k+1] - TEXT_DX,
                          GRAPH_MARGIN_SIZE + int(rank_box[k+1]) * 0.56, fill=COLORS[count], width=LINE_WIDTH)

        for m in range(12):  # to create text
            name = lookup_names[i]
            if rank_box[m] == MAX_RANK:
                w.create_text(x_box[m] + TEXT_DX, GRAPH_MARGIN_SIZE + int(rank_box[m]) * 0.54,
                              text=str(name) + ' *', fill=COLORS[count], anchor=tkinter.NW)
            else:
                w.create_text(x_box[m] + TEXT_DX, GRAPH_MARGIN_SIZE + int(rank_box[m]) * 0.54,
                              text=str(name) + ' ' + str(rank_box[m]), fill=COLORS[count], anchor=tkinter.NW)
        x_box = []
        rank_box = []
        count += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()



if __name__ == '__main__':
    main()

