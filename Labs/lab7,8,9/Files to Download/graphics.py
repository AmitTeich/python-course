# we need a root window object and then a Canvas window object (child)
# in order to be able to draw points and lines.
# The Point and Line draw() method will use this _canvas.
#
# A Canvas Window on which we can draw points, lines, rectangles, etc.
# See the Tkinter module, Canvas class, for more details.
# PyScripter may not handle Tkinter well, so to run this example,
# use the command line:
#                       python prog.py

import sys
#print(sys.version_info.major)

if(sys.version_info.major == 3):
    from tkinter import *
else:
    from Tkinter import *

try:
    rootWindow
except NameError:
    rootWindow = Tk()
    rootFrame = Frame(rootWindow, width=800, height=600, bg="white")
    rootFrame.pack()
    canvas = Canvas(rootFrame, width=800, height=600, bg="white")
    canvas.pack()


#    buttonExit = Button(rootFrame,text="Exit",command=exit)
#    buttonExit.pack(side=BOTTOM)

def show_canvas():
    if not canvas.winfo_ismapped():
        rootWindow.iconify()
        rootWindow.update()
        rootWindow.deiconify()
        rootWindow.mainloop()

def _quit(event):
    rootWindow.destroy()

def bind_key(click):
    rootWindow.bind("<Key>", click)
    rootFrame.pack()
    rootWindow.bind("q",_quit)
    rootFrame.pack()


def update_canvas():
    #rootWindow.update()
    canvas.update()

colors = 10 * ['red1', 'DarkGoldenrod2', 'yellow2', 'DarkOliveGreen1', 'chartreuse1', 'green3', 'DarkSlateGray3', 'MediumPurple3', 'MediumOrchid4', 'MediumOrchid3', 'thistle2', 'gray']
color_index = -1

def get_next_color():
    global color_index
    global colors
    color_index += 1
    if color_index >= len(colors):
        color_index = 0
    return colors[color_index]


