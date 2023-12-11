import curses
from curses import wrapper
import time

def cat_animation(stdscr):
    curses.curs_set(0)
    cat0 = """
  /\_/\  
 ( ^.^ )  
  - ^ -
"""
    cat1 = """
  /\_/\  
 ( o.o )
  > ^ <
"""
    cat2 = """
  /\_/\  
 ( O.O )  
  = w =
"""
    stdscr.clear()
    for i in range(50):
        intervel = 0.5
        def animate_cat(x,y,cat,intervel):
            stdscr.clear()
            stdscr.addstr(x,y,cat)
            time.sleep(intervel)
            stdscr.refresh()
        animate_cat(0,0,cat0,intervel)
        animate_cat(1,0,cat1,intervel)
        animate_cat(2,0,cat2,intervel)
    stdscr.getch()

wrapper(cat_animation)




 