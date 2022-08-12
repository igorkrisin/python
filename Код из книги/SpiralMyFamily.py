from turtle import*
bgcolor('black')
colors = ['red', 'blue', 'yellow', 'green','orange','pink','brown', 'gray', 'white']
family = []
name = textinput('моя семья', 'Введите имя или нажмите [return], что бы выйти: ')
while name != '':
    family.append(name)
    name = textinput('моя семья', 'Введите имя или нажмите [return], что бы выйти: ')
for i in range(100):
    pencolor(colors[i%len(family)])
    penup()
    forward(i*4)
    pendown()
    write(family[i%len(family)], font = ('Arial', int((i+4)/4), 'bold'))
    left(360/len(family) + 2)
