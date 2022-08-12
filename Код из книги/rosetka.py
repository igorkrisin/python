from turtle import*

'''for i in range(4):
    circle(100)
    left(90)'''
piece = int(input('Сколько кругов хотите увидеть в розетке? '))
bgcolor = 'black'
colors = input('ВВедиет цвет круга: ')
diam1 = int(input('Введиет диаметр 1: '))
diam2 = int(input('введите диаметр 2: '))


def rosetka (piece, diam1, diam2):
    for i in range(piece):
        circle(diam1)
        circle(diam2)
        left(360/piece)
        pencolor = 'colors'
        

rosetka(piece, diam1, diam2)
