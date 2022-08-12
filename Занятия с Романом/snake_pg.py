import pygame
import random

pygame.init()

#Если необходимо сделать на всю ширину монитора
#infoObject = pygame.display.Info()
#win=pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
vh=400
vw=400

win = pygame.display.set_mode((vh,vw))

pygame.display.set_caption("Snake")
def coord_apple():
    global a,b,x,y
    a = random.randint(10,vh-10)
    b = random.randint(10,vw-10)
    a=a-a%10
    b=b-b%10

direction_x=10
direction_y=0    
x=10
y=10
w=10
h=10
speed=200
snake_coord = [[y,x]]
coord_apple()
run = True
score = 0
clock = pygame.time.Clock()
while run:
    pygame.time.delay(speed)
#Выход по крестику мышкой
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Клавиша нажата "1 клик" движение
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                direction_y+=10
                direction_x=0
                if direction_y<10 or direction_y>10:
                    direction_y=10
                    print(direction_y)
            elif event.key == pygame.K_a:
                direction_y-=10
                direction_x=0
                if direction_y<-10 or direction_y>-10:
                    direction_y=-10
                    print(direction_y)
            elif event.key == pygame.K_s:
                direction_x+=10
                direction_y=0
                if direction_x<10 or direction_x>10:
                    direction_x=10
            elif event.key == pygame.K_w:
                direction_x-=10
                direction_y=0
                if direction_x<-10 or direction_x>-10:
                    direction_x=-10
            elif event.key == pygame.K_v:
                save()
            elif event.key == pygame.K_b:
                load()
            #Выход по ESC 
            elif event.key == pygame.K_ESCAPE:
                run = False
            # Зарисовываем хвост
            
    x+=direction_x
    y+=direction_y  
    win.fill((0,0,0))  
    #Переход за границы экранаё
    if x<0: x = vw-10
    if x>vw-10: x = 0
    if y<0: y = vh-10
    if y>vh-10: y = 0
    pygame.draw.rect(win, (255,0,0), (a,b, w ,h))
    
    #Кушает яблоко
    if  not (a == y and b == x):
        snake_coord.pop(0)
    else:
        coord_apple()
        pygame.draw.rect(win, (255,0,0), (a,b, w ,h))
        speed-=15
        score+=1
    #Врезалась в свой хвост
    if [y,x] in snake_coord:
        pygame.font.Font(None, 24)     
    snake_coord.append([y,x])
    pygame.draw.rect(win, (0,0,255), (y,x, w ,h)) 
     #Рост змеи
    for i in range (len(snake_coord)):
        pygame.draw.rect(win, (0,0,255), (snake_coord[i][0],snake_coord[i][1],w,h))
    pygame.display.update()
    clock.tick(10)

    def save():
        global list_save
        list_save={'snake_coord': snake_coord[:],\
        'a':a,'b':b, 'direction_x':direction_x,\
        'direction_y':direction_y,'y':y, 'x':x}
    def load():
        global snake_coord,a,b,direction_x,direction_y,y,x,list_save
        snake_coord =list_save['snake_coord']
        a=list_save['a']
        b=list_save['b']
        direction_x=list_save['direction_x']
        direction_y=list_save['direction_y']
        x=list_save['x']
        y=list_save['y']
pygame.quit()

   
    