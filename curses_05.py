import curses
from curses import wrapper
import time

def display(stdscr):
    curses.init_pair(1,curses.COLOR_CYAN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_RED,curses.COLOR_BLACK)

    cyan = curses.color_pair(1)
    green = curses.color_pair(2)
    blue = curses.color_pair(3)
    magenta = curses.color_pair(4)
    red = curses.color_pair(5)
    
    #function to create window
    def window(wh,ww,px,py,text,text_color,border_color):
        #wh = window height,ww = window width,px = x position,py = y position
            win = curses.newwin(wh,ww,px,py)
            curses.curs_set(0)
            win.clear()
            win.addstr(1,2,text,text_color | curses.A_BOLD)
            win.attron(border_color)
            win.border(0)
            win.attroff(border_color)
            win.refresh()
    
    for i in range(50):
        window(3,16,4,29,"FOCUS",blue,magenta)
        window(3,16,4,4,"CONSISTANCY",green,magenta)
        window(3,16,8,4,"GOAL",red,magenta)
        window(3,16,8,29,"SUCCUSS",cyan,magenta)
        time.sleep(.3)

    stdscr.getch()
wrapper(display)