import random

gameStore = ["к", "н", "б"]

print("Вас приветствует игра камень, ножницы, бумага!")

enter = input("Сыграем? Елсли хоттие начать - введите нажмите ENTER\nили введите с клавиатуры 'нет' для выхода: ")
if enter == "нет":
    exit()
countAttempt = int(input("До скольки очков будем играть? "))
print("Окей играем до ", countAttempt, "очков. \n Погнали!!!")
playerScore = 0
compScore = 0
while playerScore != countAttempt and compScore != countAttempt:
    print("очки игрока: ", playerScore,"\n", "очки компа: ", compScore )
    playerChoise = input("введи камень - 'к', ножницы - 'н', бумага - 'б': ")
    compChoise = gameStore[random.randint(0, 2)]

    if compChoise == playerChoise:
        print("Ничья, попробуем еще раз")
    elif compChoise == "к" and playerChoise == "б":
        print("выбор компа: камень, тебе одно очко!")
        playerScore += 1
    elif compChoise == "н" and playerChoise == "б":
        print("выбор компа: ножницы, ему одно очко!")
        compScore += 1
    elif compChoise == "б" and playerChoise == "к":
        print("выбор компа: бумага, ему одно очко!")
        compScore += 1
    elif compChoise == "н" and playerChoise == "к":
        print("выбор компа: ножницы, тебе одно очко!")
        playerScore += 1
    elif compChoise == "б" and playerChoise == "н":
        print("выбор компа: бумага, тебе одно очко!")
        playerScore+= 1
    elif compChoise == "к" and playerChoise == "н":
        print("выбор компа: камень, ему одно очко!")
        compScore += 1
    else:
        print("Неправильный ввод")

print("Твои очки - ", playerScore, "очки компа - ", compScore)
if playerScore == countAttempt:
    print("Отличная игра, приходи еще")
elif compScore == countAttempt:
    print("Увы, ты проиграл, начинай заново")
else:
    print("Ничья!!!")


    