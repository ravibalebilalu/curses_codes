import curses
from curses import wrapper
import time

def display(stdscr):
    curses.curs_set(0)
    # Set non-blocking input
    stdscr.nodelay(1)  
    #coordinats 
    maxyx = stdscr.getmaxyx()
    x, y = maxyx[0], maxyx[1]
    z = 0
    text = "<PYTHON>"
    count = 0
    running = True

    while running:
        count += 1
        #limit the coordinates
        if count >= y:
            count = 0
            z += 1
        elif z >= x - 1:
            z, count = 0, 0

        stdscr.clear()
        stdscr.addstr(z, count, text, curses.A_BOLD)
        stdscr.addstr(maxyx[0] -1,0,"press 'q' to exit")
        stdscr.refresh()
        time.sleep(0.1 / 10)

        # Check for user input to stop the loop
        key = stdscr.getch()
        if key == ord('q'):
            running = False

wrapper(display)
