import pygame
import random

pygame.init()

#Если необходимо сделать на всю ширину монитора
#infoObject = pygame.display.Info()
#win=pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
vh=200
vw=200

win = pygame.display.set_mode((vh,vw))

pygame.display.set_caption("Snake")
def coord_apple():
    global a,b
    a = random.randint(0,vh)
    b = random.randint(0,vw)
    a=a-a%10
    b=b-b%10

    
x=10
y=10
w=10
h=10
speed=10
snake_coord = [[y,x]]
coord_apple()
run = True
while run:
    pygame.time.delay(100)
#Выход по крестику мышкой
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Клавиша нажата "1 клик" движение
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x +=speed
            elif event.key == pygame.K_a:
                x -=speed
            elif event.key == pygame.K_s:
                y +=speed
            elif event.key == pygame.K_w:
                y -=speed
            #Выход по ESC 
            if event.key == pygame.K_ESCAPE:
                run = False
    # Клавиша зажата движение
   
        '''keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            x+=speed
        elif keys[pygame.K_a]:
            x-=speed
        elif keys[pygame.K_s]:
            y+=speed
        elif keys[pygame.K_w]:
            y-=speed'''
        
    #Переход за границы экрана

    if x<0: x = vw-10
    if x>vw: x = 5
    if y<0: y = vh-10
    if y>vh: y = 5
    #удаление хвоста, пока не скушает яблоко
    if not (a==y and b==x):
        snake_coord.pop(0)
    else:
        coord_aplle()
    if [y,x] in snake_coord:
        run = False
    #Рост змейки
        
    snake_coord.append([y,x])
    
    # Зарисовываем хвост
    win.fill((0,0,0))
    #Отрисовка яблока
    pygame.draw.rect(win, (255,0,0), (a,b, w ,h))
    if a==x and b==y:
        coord_apple()
        pygame.draw.rect(win, (255,0,0), (a,b, w ,h))
    #Отрисовка змеи
    for i in range(len(snake_coord)):    
        pygame.draw.rect(win, (0,0,255), (snake_coord[i][0],snake_coord[i][1], w ,h))
    pygame.display.update()
pygame.quit()
