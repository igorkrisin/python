from turtle import*
sides = int(numinput("Количество сторон спирали", "Сколько сторон будет у Вашей спирали?", 4))
for m in range(5,75):
    lt(360/sides+5)
    width(m//25+1)
    penup()
    fd(m*4)
    pendown()
    if (m % 2 == 0):
        for n in range(sides):
            circle(m/3)
            rt(360/sides)
    else:
        for n in range(sides):
            fd(m)
            rt(360/sides)
