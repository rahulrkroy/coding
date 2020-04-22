import curses


s=curses.initscr()
curses.curs_set(0)
sh,sw=s.getmaxyx()
w=curses.newwin(sh,sw,0,0)
w.keypad(1)
w.timeout(100)

print("sh,sw",sh,' ',sw)
w.addch(8,187,curses.ACS_PI)