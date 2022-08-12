print('MathHomework.py')
problem = input('Введите задачу или нажмите q для выхода: ')
while (problem != 'q'):
    print('ОТвет на Вашу задачу:',problem ,'-это', eval(problem))
    problem = input('Введите задачу или нажмите q для выхода: ')
