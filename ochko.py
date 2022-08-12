
import random
import os
import time


score_playera = 0
score_bota = 0

all_carts = [2,3,4,5,6,7,8,9,10,11]
print("Поиграем в 21? \nЕсли хотите играть нажмите retutn, если хоттие выйти нажмите Ctrl+C")
input()
score_playera = random.choice(all_carts)
print("У вас :",score_playera," очков.")

while True:
    if score_playera ==21:
        print('Больше карт не нужно у Вас 21, вы Выиграли!')
        print('Вы автоматически победили бота!')
        input("Нажмите return, что бы закрыть"); break
    elif score_playera>21:
        print("Вы проиграли, так как набрали больше 21 очка")
        print("В следующий раз повезет...")
        input("Нажмите return, что бы выйти");break
        
    yes_or_no=input("Возьмете еще карту?\nвведите да, если хотите брать карту, введите нет если вам хватит: ")
    os.system("clear")
    if yes_or_no == "да":
        os.system("clear")
        score_carts = random.choice(all_carts)
        print("Вы взяли карту, выпало:", score_carts)
        score_playera += score_carts
        print("Сейчас у вас ",score_playera, "очков.")
    elif yes_or_no =="нет":
        print("Ход бота")
        time.sleep(3)
        print("Бот берет карту")
        time.sleep(2)
        score_carts = random.choice(all_carts)
        print("Боту выпало" ,score_carts,"очков.")
        time.sleep(3)
        score_bota += score_carts
        print("У бота", score_bota,"очков")
        time.sleep(3)
        while True:
            if score_bota<15:
                print("Бот берет карту")
                time.sleep(2)
                score_carts = random.choice(all_carts)
                print("Боту выпало" ,score_carts,"очков.")
                time.sleep(3)
                score_bota += score_carts
                print("У бота", score_bota,"очков")
                time.sleep(3)
                
            elif score_bota>21:
                time.sleep(1)
                print("Бот проиграл у него: ", score_bota," очков, а у вас ", score_playera," очков")
                input("Нажмите return, что бы звкрыть"); exit(0)
            elif score_bota>score_playera:
                time.sleep(1)
                print("Бот победил.\nТак как у него: ",score_bota, " очков, а у тебя: ",score_playera," очков.")
                input("Нажмите return, что бы закрыть");exit(0)
            elif score_bota<score_playera:
                time.sleep(1)
                print("Вы победили.\nВы набрали: ",score_playera,"очков, а уботдаа: ",score_bota,"очков.")
                input("Нажмите return, что бы закрыть");exit(0)
            elif score_bota==score_playera:
                time.sleep(1)
                print("У вас ничья вы оба набрали по :",score_bota,"очков.")
                input("Нажмите return, что бы закрыть");exit(0)
        
