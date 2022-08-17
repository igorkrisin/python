import sys
from time import sleep
from tkinter import Y
import pygame


pygame.init()

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (1300, 500))
car = pygame.image.load("car1.png")
car = pygame.transform.scale(car, (180, 132))
car_pink = pygame.image.load("car2.png")
car_pink = pygame.transform.scale(car_pink, (100, 117))
bullet = pygame.image.load("bul.png")
bullet = pygame.transform.scale(bullet,(20,30))
finish = pygame.image.load("finish.png")
finish1 = False
finish2 = False

window = pygame.display.set_mode((1300, 500))
screen = pygame.Surface((1300, 500))
start_game = True
speed = 25
number = 1
bull_speed = 0.1



def bul_to_go(y_bull, bull_speed):
    while y_bull>0:
        y_bull -= bull_speed
        screen.blit(bullet,(788,y_bull))
        

y_car = 340
y_car_pink = 344
y_bull = y_car

text_font = pygame.font.SysFont("comicsansmc", 80)
text_render = text_font.render("Выиграл Игрок 1", 0, (0,0,0))
text_render_2 = text_font.render("Выиграл Игрок 2", 0, (0,0,0))
text_render_3 = text_font.render(str(number), 0, (0,0,0))

while start_game:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            y_car -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y_car_pink -= speed
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bul_to_go(y_bull, bull_speed)
            
    if y_car < 50 and finish2 == False:
        screen.blit(text_render, (200, 200))
        finish1 =True
    elif  y_car_pink < 50 and finish1 == False:
        screen.blit(text_render_2, (200, 200))
        finish2 =True
        
        
    window.blit(screen, (0,0))
    
    screen.blit(bg, (0,0))
    screen.blit(finish, (0, -150))
    screen.blit(car,(712, y_car+22))
    screen.blit(car_pink,(812, y_car_pink))
  
    
    
    
    
    
    pygame.display.update()
   

pygame.quit()


