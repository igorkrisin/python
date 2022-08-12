#круги цикл

colors = ['red','blue','yellow','green']
>>> for i in range(18):
	pencolor(colors[i%4])
	circle(100)
	lt(20)


#Круги функция
def myCircle(piece, size):
	colors = ['red','blue','green']
	for i in range(piece):
		pencolor(colors[i%3])
		circle(size)
		lt(360/piece)

		
>>> myCircle(8,100)


#Функция цветок

>>> def flower(piece, size):
	for i in range(piece):
		fd(size)
		lt(45)
		fd(size)
		lt(135)
		fd(size)
		lt(45)
		fd(size)
		lt(135)
		lt(360/piece)
	for i in range(1):
		home()
		rt(90)
		fd(300)

		
>>> flower(6,100)


#Квадратики

>>> def square(piece, size, gap):
	for i in range(piece):
		fd(size)
		lt(90)
		fd(size)
		lt(90)
		fd(size)
		lt(90)
		fd(size)
		lt(90)
		fd(size)
		penup()
		fd(gap)
		pendown()

		
>>> square(5, 50, 10)


#спираль из на увеличение


line(100)
>>> def line(size):
	for i in range(1):
		fd(size)
		bk(size)


spirale(100,100,1)
>>> def spirale(maxSize,piece):
	for i in range (0,maxSize,1):line(i);lt(360/piece)

	
>>> spirale(150, 200)


def snake(piece, thickness, color):
	for i in range(piece):
		fd(i)
		lt(90)
		width(thickness)
		pencolor(color)

snake(100,1,'orange')





