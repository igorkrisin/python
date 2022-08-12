import curses
import random
def coord():
    global a,b
    
    b=random.randint(0,width)
    a=random.randint(0,height)
    

def main(screen):
    global height, width
    height, width = screen.getmaxyx()
    curses.curs_set(0)
    screen.addstr(0,0,'s')
    x=0
    y=0
    coord()
    while True:
        dvig=screen.getch()
        if dvig == ord('w'):
            y-=1
        elif dvig == ord('s'):
            y+=1
        elif dvig == ord('a'):
            x-=1
        elif dvig == ord('d'):
            x+=1
        screen.erase()
        if a==y and b==x:
            coord()
        if x<0: x=width-1
        if y<0: y=height-1
        if x>width-1: x=0
        if y>height-1: y=0
        screen.addstr(a,b,'j')
        screen.addstr(y,x,'s')
curses.wrapper(main)
