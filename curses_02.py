import curses
from curses import wrapper
import time

def main(stdscr):
    #initialize color :forground and background colors
    curses.init_pair(1,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_RED,curses.COLOR_BLACK)

    maganta = curses.color_pair(1)
    blue = curses.color_pair(2)
    green = curses.color_pair(3)
    red = curses.color_pair(4)

    #for loop to change the colors
    for i in range(50):
        stdscr.clear()
        color = blue
        if i%2 == 0:
            color = green
        elif i%3 == 0:
            color = maganta
        elif i%5 == 0:
            color = blue
        elif i%7 == 0:
            color = red
        stdscr.addstr(2,14,"PYTHON",color | curses.A_BOLD)
        stdscr.addstr(4,16,"IS",color | curses.A_BOLD)
        stdscr.addstr(6,14,"AWESOME",color | curses.A_BOLD)

        time.sleep(0.1)
        stdscr.refresh()

    #after blinking stops press any key to exit
    stdscr.getch()

wrapper(main)