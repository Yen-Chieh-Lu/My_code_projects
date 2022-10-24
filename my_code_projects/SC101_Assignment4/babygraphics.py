"""
File: babygraphics.py
Name: Jason
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    if year_index != 0:
        x_coor = GRAPH_MARGIN_SIZE + ((width-GRAPH_MARGIN_SIZE) / len(YEARS)) * year_index
    else:
        x_coor = GRAPH_MARGIN_SIZE
    return x_coor


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT
                       - GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


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

    # ----- Write your code below this line ----- #
    n = -1
    for name in lookup_names:
        n += 1
        if n >= len(COLORS):
            n = -1
            n += 1
            color = COLORS[n]
        else:
            color = COLORS[n]
        for i in range(len(YEARS)):
            if i != 0:
                start_x = get_x_coordinate(CANVAS_WIDTH, i-1)  # 去年
                x = get_x_coordinate(CANVAS_WIDTH, i)  # 今年
                if str(YEARS[i]) in name_data[name]:  # 今年有資料
                    if str(YEARS[i - 1]) in name_data[name]:  # 去年有資料
                        start_y = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE) / 1000 * int(name_data[name][str(YEARS[i-1])]) + \
                                  GRAPH_MARGIN_SIZE
                        y = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE) / 1000 * int(name_data[name][str(YEARS[i])]) + \
                            GRAPH_MARGIN_SIZE
                        canvas.create_line(start_x, start_y, x, y, width=LINE_WIDTH, fill=color)
                        canvas.create_text(start_x+TEXT_DX, start_y, text=name + ' ' + name_data[name][str(YEARS[i-1])],
                                           anchor=tkinter.SW)
                        canvas.create_text(x + TEXT_DX, y, text=name + ' ' + name_data[name][str(YEARS[i])],
                                           anchor=tkinter.SW)
                    else:  # 去年無資料
                        start_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE) / 1000 * int(name_data[name][str(YEARS[i])]) + \
                            GRAPH_MARGIN_SIZE
                        canvas.create_line(start_x, start_y, x, y, width=LINE_WIDTH, fill=color)
                        canvas.create_text(start_x + TEXT_DX, start_y, text=name + ' *', anchor=tkinter.SW)
                        canvas.create_text(x + TEXT_DX, y, text=name + ' ' + name_data[name][str(YEARS[i])],
                                           anchor=tkinter.SW)
                else:  # 今年無資料
                    if str(YEARS[i - 1]) in name_data[name]:  # 去年有資料
                        start_y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE) / 1000 * int(name_data[name][str(YEARS[i - 1])]) \
                                  + GRAPH_MARGIN_SIZE
                        y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_line(start_x, start_y, x, y, width=LINE_WIDTH, fill=color)
                        canvas.create_text(start_x + TEXT_DX, start_y, text=name + ' ' + name_data[name][str(YEARS[i-1])],
                                           anchor=tkinter.SW)
                        canvas.create_text(x + TEXT_DX, y, text=name + ' *', anchor=tkinter.SW)
                    else:  # 去年無資料
                        start_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_line(start_x, start_y, x, y, width=LINE_WIDTH, fill=color)
                        canvas.create_text(start_x + TEXT_DX, start_y, text=name + ' *', anchor=tkinter.SW)
                        canvas.create_text(x + TEXT_DX, y, text=name + ' *', anchor=tkinter.SW)


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
