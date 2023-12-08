import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(2,10,"HELLO WORLD",curses.A_BOLD)
    stdscr.refresh()
    #press any key to exit
    stdscr.getch()

wrapper(main)