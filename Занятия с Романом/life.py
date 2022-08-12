""" 
from curses import* 

f = open('ex.txt','r')
s = f.read()
#print(s)

#s='[ ][*][ ]\n[ ][ ][*]\n[*][*[*]'
#"[ ][*][ ]\n[ ][ ][*]\n[*][*][*]" -> ["[ ][*][ ]",'[ ][ ][*]',..] -> [["[ ]","[*]","[ ]"],["[ ]","[ ]","[*]"],...]
def main(screen):
    global m
    speed = 5
    halfdelay(speed)
    while True:
        screen.addstr(0,0,print_matrix(m))
        m=next_generation(m)
        dvig=screen.getch()
        if dvig == ord('q'):
            return

#split_3("abdefgh12") -> ["abd","efg","h12"]

def split_3(s):
    m=[]
    for i in range(0,len(s)-1,3):
        m+=[s[i:i+3]]
    return m
#print(split_3(s))      
        
def string_to_matrix(s):
    m=[]
    n=''
    n=s.split('\n')
    
    for i in range(len(n)):
        m+=[[0 if i == '[ ]' else 1 for i in  split_3(n[i])]]
      
    
    return m
m = string_to_matrix(s)

def print_matrix(m):
    str=''
     
    for i in m:
        str+='\n'
        for j in i:
            
            if j==0:
                str+='[ ]'
            if j==1:
                str+='[*]'
    return str
 """

m = [[3,4,5,6],
	[4,5,6,7],
	[5,6,7,8]] 

def get_cell(x,y,m):
    if x<0 or y>=len(m) or x>=len(m[y]) or y<0:
        return 0
    else:
        return m[y][x]

def count_neighbours(x,y,m):
    return get_cell(x-1,y+1,m)+\
    get_cell(x, y+1,m)+\
    get_cell(x+1, y+1,m)+\
    get_cell(x-1,y,m)+\
    get_cell(x+1,y,m)+\
    get_cell(x-1,y-1,m)+\
    get_cell(x,y-1,m)+\
    get_cell(x+1,y-1,m)
    
print(count_neighbours(0,5,m))


""" def play_rules(x,y,m):
    if m[y][x]==0 and count_neighbours(x,y,m) == 3:
        return 1
    elif m[y][x] ==1 and count_neighbours(x,y,m) == 2\
        or  count_neighbours(x,y,m) == 3:
        return 1
    else:
        return 0
#print(play_rules(1,1,m))


def next_generation(m):
    n=[]
    
    for y in range(len(m)):
        b=[]
        for x in range(len(m[y])):
            b+=[play_rules(x,y,m)]
        n+=[b]
    return n
print(print_matrix(next_generation(m)))

#print(print_matrix(m))
f.close()
wrapper(main)

 """

