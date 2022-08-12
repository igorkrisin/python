from turtle import*
number = int(numinput('Количество сторон или окружностей', 'Сколько сторон или окружностей будет у фигуры?', 6))
shape = textinput('Какую фигуру хотите?', 'Введите "м" для многоугольника и "р" для розетки: ')
for i in range(number):
    if shape == 'р':
        circle(100)
    else:
        fd(150)
    lt(360/number)
