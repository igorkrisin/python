from os import name
import random
import time


print("Добро поджаловать в автоматическую считалку")
playerCounts = int(input("ВВедите количество игроков \n"))
playerName  = []
for i in range(playerCounts):
    playerName.append([input("Введите имя игрока\n")])
print(playerName)

shcitalka = ["на ", "злотом ", "крыльце ", "сидели ", "царь ", "царевич ", "король ", "корлевич ", "сапожник ", "портной ", "кто ты будешь такой ", "выбирай поскорей","не задерживай", "добрых и честных", "людей"]
yourChoise = input("приступиступим к считалке? введите 'да' с клавиатуры\n для отмены введите нет\n")
if yourChoise == "да":
    for y in range(len(shcitalka)):
        time.sleep(1)
        count = random.randint(0,playerCounts - 1)
        print(shcitalka[y]," ", playerName[count][0])
else:
    exit(0)
time.sleep(2)
print("Итааак Водит - ", playerName[count][0])
#print(playerName[1][0])
        
  
