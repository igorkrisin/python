import random
choices = ["камень", "ножницы", "бумага"]
print("Камень давит нажницы. Ножницы режут бумагу. Бумага накрывает камень")
player = input("введите: камень, ножницы или бумага или (выйти)?: ")
while player != "выйти":
    player = player.lower()
    computer = random.choice(choices)
    print("Твой выбор " +player+ ", компьютер выбрал " +computer+ ".")
    if player == computer:
        print("У вас ничья :-)")
    elif player == "камень":
        if computer == "ножницы":
            print("Вы победили!!!")
        else:
            print("Победил компьютер.......")
    elif player == "ножницы":
        if computer == "бумага":
            print("Вы  победили!!!")
        else:
            print("Победил компьютер.......")
    elif player == "бумага":
        if computer == "камень":
            print("Вы победили!!!")
        else:
            print("Победил компьютер.......")
    else:
        print("Кажется что-то пошло не так.")
    print()
    player = input("введите: камень, ножницы или бумага или (выйти)?: ")
