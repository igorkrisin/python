import curses
import random
def coord():
    global a,b
    
    b=random.randint(5,width-1)
    a=random.randint(5,height-1)
    
#(11,14)    <-    (12,14) -> (13,14)
        # <-  x  ->
        #    x x
          # x+=1
          # x-=1
#x+=a

def main(screen):
    global height, width, napravl_x,napravl_y,coord_snake,y,x, speed,score
    score=1
    speed=5
    curses.halfdelay(speed)
    napravl_x=1
    napravl_y=0
    x=5
    y=5
    coord_snake = [[y,x]]
    height, width = screen.getmaxyx()
    curses.curs_set(0)
    screen.addstr(0,0,'s')
    coord()
    while True:
        screen.addstr(0,0,'score: '+ str(score))
        dvig=screen.getch()
        if dvig == ord('w'):
            napravl_y=-1
            napravl_x=0
        elif dvig == ord('s'):
            napravl_y=1
            napravl_x=0
        elif dvig == ord('a'):
            napravl_x=-1
            napravl_y=0
        elif dvig == ord('d'):
            napravl_x=1
            napravl_y=0
        elif dvig == ord('v'):
             save()
        elif dvig == ord('b'):
             load()
        elif dvig == ord('m'):
            return
        screen.erase()
        
        
        
        x+=napravl_x
        y+=napravl_y



        if x<0: x=width-1
        if y<0: y=height-1
        if x>width-1: x=0
        if y>height-1: y=0
        if not (a==y and b==x):
            coord_snake.pop(0)
            
        else:
            coord()
            speed+=2
            score+=1
            #print(score)
        #for i,j in coord_snake:
            #if y == i and x == j:
        if [y,x] in coord_snake:
                score=1
                main(screen)
                return


        coord_snake.append([y,x])
        
#[1,2,3] append(4) -> [1,2,3,4]
        #coord_snake += [[y,x]]
#[1,2,3]+[4,5]  -> [1,2,3,4,5]
#[y,x,y,x,y,x]
#[[y,x],[y,x],...]
# [42,13][0] -> 42
# ([42,13]+[666])[2] -> [42,13,666][2] -> 666
# reverse([42,13,666])[0]

        screen.addstr(a,b,'j')
        if [a,b] in coord_snake:
            screen.addstr(a,b,'j')
        for i in range(len(coord_snake)):
             screen.addstr(coord_snake[i][0],coord_snake[i][1],'s')
        
             
def save():
    global list_save
    list_save= {'coord_snake':coord_snake[:],\
    'a':a,'b':b,'napravl_x':napravl_x,\
    'napravl_y':napravl_y,'y':y,'x':x}

def load():
    global coord_snake,a,b,napravl_x,napravl_y,y,x,list_save
    cord_snake = list_save['coord_snake']
    a = list_save['a']
    b = list_save['b']
    napravl_x= list_save['napravl_x']
    napravl_y= list_save['napravl_y']
    y = list_save['y']
    x = list_save['x']


curses.wrapper(main)







