import random
import os
import time



print("Добро пожаловать в игру 21 очко\n, если вы готовы сыгрвть - \nнажмите RETURN, если нет CTRL+C")
input()
print
comp_score = random.randint(2,12)
cardPlayer = random.randint(2,12)
player_score  = cardPlayer


print("у вас на руках ", player_score, " очков\n")
""" print(comp_summ) """

while(True):
    if player_score == 21:
        print("Вы победили, поздравляю")
        input("нажмите return, что бы выйти")
        break
    elif player_score > 21:
        print("Вы проиграли, приходите еще, нажмите return, что бы выйти")
        input()
        break
    yourChoise = input("Хотите взять еще карту? введите да или нет\n ")
    if yourChoise == "да":
        cardPlayer = random.randint(2,11)
        player_score  += cardPlayer
        print("Вы взяли карту ",cardPlayer,"у вас ", player_score, " очков")

    elif yourChoise == "нет":
        print("Теперь ход компьютера, он берет карту")
        compCart = random.randint(2,11)
        time.sleep(2)
        print("он взял  ", compCart," очков")
        comp_score += compCart

        print("И теперь у него  ", comp_score, " очков")
        time.sleep(2)
        while comp_score < 15:
            print("И теперь у него  ", comp_score, " очков\nберет еще карту")
            compCart = random.randint(2,11)
            print("у компа", comp_score, "очков \n, он берет карту")
            print("Компу выпало ", compCart, " очков")
            time.sleep(2)
            comp_score += compCart
            print("Теперь у него ", comp_score, " очков")
        if comp_score == 21:
            print("Комп выиграл у него 21!, ты лузер")
            input("Нажмите return, что бы выйти")
            break
        elif comp_score > 21:
            time.sleep(2)
            print("Ты выиграл, у компа перебор -  " ,comp_score, " очков, он лузер")
            input("Нажмите return, что бы выйти")
            break
        elif comp_score > player_score:
            time.sleep(2)
            print("Комп выиграл у него !",comp_score ,"a у тебя", player_score, "ты лузер")
            input("Нажмите return, что бы выйти")
            break
        elif comp_score == player_score:
            time.sleep(2)
            print("Ничья ! у вас по ",comp_score ,"очков")
            input("Нажмите return, что бы выйти")
            break
        else:
            time.sleep(2)
            print("Ты выиграл у компа",comp_score ,"a у тебя", player_score, "он лузер")
            input("Нажмите return, что бы выйти")
            break


            







