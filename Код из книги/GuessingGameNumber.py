from random import randint
chislo = randint(0,7)
number = int(input("Введите число от 0 до 10: "))
while number != chislo:
    if number > chislo:
        print("Загаданое число меньше! уменьшааай!")
    if number < chislo:
        print("Загаданное число больше!!! Надо боольше ЗОЛОТА!")
    if number == "":
        print("Вы не ввели ЧИСЛО!!! Число хочу, давай чило!А?")
    number = int(input("Попробуй еще раз введи числдо 0 до 10: "))
    if number == chislo:
        print(number, "Правильное число! Вы победили!")
        number = input("Хотите сыграть еще раз? да/нет?")
        if number == "да":
            number = int(input("Попробуй еще раз введи числдо 0 до 10: "))
print("досвидания")
