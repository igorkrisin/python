import pygame
import random
pygame.init()
winwidth=500
winheight=500
win = pygame.display.set_mode((winwidth,winheight))
pygame.display.set_caption('Snake')
x = 50
y = 50
width = 10
height= 10
speed = 5
b = random.randint(0,winwidth-1)
a = random.randint(0,winheight-1)
coord_snake=[[x,y]]

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
       x -= speed
    if keys[pygame.K_d]:
       x += speed
    if keys[pygame.K_w]:
       y -= speed
    if keys[pygame.K_s]:
       y += speed
    win.fill((0,0,0))
    

    if x<0: x=winwidth-1
    if x>winwidth: x=0+1
    if y<0: y=winwidth-1
    if y>winwidth: y=0+1
    
    #рисуем яблоко
    pygame.draw.rect(win, (0,255,0),(a, b, width,height))
    if [a,b] in coord_snake:
        pygame.draw.rect(win, (0,255,0),(a, b, width,height))
    #рисуем змею
    pygame.draw.rect(win, (0,0,255),(x, y, width,height))
    pygame.display.update()

pygame.quit()
    
