import random

print("Вас приветствует Игра 'угадай число'\n")
startNum = int(input("Введите начальное значение диапазона "))
finishNum = int(input("Введите конечное значение диапазона "))
readyGame = ""
while(readyGame != "да"):
    print("Введите 'да', если хотите, что бы компьютер загадал число от ", startNum, " до ", finishNum)
    readyGame = input()
if(readyGame == "да"):
    compNum = random.randint(startNum, finishNum)
    playerNum = int(input("Введите ваше число "))

while(compNum != playerNum):
    if(compNum < playerNum):
        print("Число компьютера меньше")

    elif(compNum > playerNum):
        print("Число компьютера больше")
    playerNum = int(input("Введите ваше число заново "))
print("Вы победили!")



   