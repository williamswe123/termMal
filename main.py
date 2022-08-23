from curses import wrapper
import curses

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    
    win = curses.newwin(2, 20, 2, 2)
    stdscr.refresh()
    win.addstr("oifweoifnoi\noqwid\ndw", curses.color_pair(1))
    win.refresh()

    stdscr.getkey()

wrapper(main)