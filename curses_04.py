#this script shows date ,time and day in terminal
import datetime
from datetime import timedelta
import curses
from curses import wrapper
import time

def display(stdscr):
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_RED,curses.COLOR_BLACK)
    blue = curses.color_pair(1)
    green = curses.color_pair(2)
    red = curses.color_pair(3)
    bottom_text = "Press any key to exit"

    x,y = stdscr.getmaxyx()
    for i in range(20):
        stdscr.clear()
        # As my  system time is slower than IST,added 30 minuts to time object
        now = datetime.datetime.now() + timedelta(minutes=30)
        date_today = now.strftime("%d-%m-%Y")
        time_now = now.strftime("%I:%M %p")
        today_name = datetime.datetime.today().strftime("%A")

        stdscr.addstr((x//3),(y//2)- len(date_today)//2,date_today,blue | curses.A_BOLD)
        stdscr.addstr((x//2),(y//2)- len(time_now)//2,time_now,green | curses.A_BOLD)
        stdscr.addstr((x//2) + 2,(y//2)- len(today_name)//2,today_name,red | curses.A_BOLD)
        stdscr.refresh()
        time.sleep(0.2)
    stdscr.addstr(x -1,y//2 ,bottom_text)
    stdscr.getch()
wrapper(display)
 