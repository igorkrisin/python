Python 3.8.7 (v3.8.7:6503f05dd5, Dec 21 2020, 12:45:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============== RESTART: /Users/macbookpro/dev/python/DZ 15.02.py ==============
>>> 
=============== RESTART: /Users/macbookpro/dev/python/DZ 15.02.py ==============
Traceback (most recent call last):
  File "/Users/macbookpro/dev/python/DZ 15.02.py", line 5, in <module>
    circle()
TypeError: circle() missing 1 required positional argument: 'radius'
>>> 
=============== RESTART: /Users/macbookpro/dev/python/DZ 15.02.py ==============
>>> 
=============== RESTART: /Users/macbookpro/dev/python/DZ 15.02.py ==============
>>> 
=============== RESTART: /Users/macbookpro/dev/python/DZ 15.02.py ==============
>>> for i in range(18):
	cirle(100)
	lt(20)
	pencolor('red','blue','green')

	
Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    cirle(100)
NameError: name 'cirle' is not defined
>>> for i in range(18):
	circle(100)
	lt(20)
	pencolor('red','blue','green')

	
Traceback (most recent call last):
  File "<pyshell#6>", line 4, in <module>
    pencolor('red','blue','green')
  File "<string>", line 8, in pencolor
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 2253, in pencolor
    color = self._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 2697, in _colorstr
    return self.screen._colorstr(args)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 1165, in _colorstr
    r, g, b = [round(255.0*x) for x in (r, g, b)]
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 1165, in <listcomp>
    r, g, b = [round(255.0*x) for x in (r, g, b)]
TypeError: can't multiply sequence by non-int of type 'float'
>>> for i in range(18):
	circle(100)
	lt(20)
	pencolor(red)

	
Traceback (most recent call last):
  File "<pyshell#8>", line 4, in <module>
    pencolor(red)
NameError: name 'red' is not defined
>>> for i in range(18):
	circle(100)
	lt(20)
	pencolor('red')

	
>>> clear()
>>> for i in range(18):
	circle(100)
	lt(20)
	pencolor['red','green']

	
Traceback (most recent call last):
  File "<pyshell#13>", line 4, in <module>
    pencolor['red','green']
TypeError: 'function' object is not subscriptable
>>> colors = ['red','green','blue']
>>> colors = ['red','green','blue']
for i in range(18):
	circle(100)
	lt(20)
	pencolor(colors[i%3])
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> colors = ['red','green','blue']
for i in range(18):
	circle(100)
	lt(20)
	pencolor(colors[i%3])
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> colors = ['red','green','blue']
for i in range(18):
	circle(100)
	lt(20)
	pencolor(colors)
	
SyntaxError: multiple statements found while compiling a single statement
>>> colors = ['red','green','blue']
for i in range(18):
	pencolor(colors[i%3])
	circle(100)
	lt(20)
	
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> colors = ['red','blue','yellow','green']
>>> for i in range(18):
	pencolor(colors[i%3])
	circle(100)
	lt(20)

	
>>> for i in range(18):
	pencolor(colors[i%4])
	circle(100)
	lt(20)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 2, in <module>
    pencolor(colors[i%4])
  File "<string>", line 5, in pencolor
turtle.Terminator
>>> colors = ['red','blue','yellow','green']
>>> for i in range(18):
	pencolor(colors[i%4])
	circle(100)
	lt(20)

	
>>> def myCircle(piece, size):
	for i in range(piece):
		circle(size)
		lt(360/piece)

		
>>> miCircle(10,2)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    miCircle(10,2)
NameError: name 'miCircle' is not defined
>>> myCircle(10,2)

======================================= RESTART: Shell =======================================
>>> def myCircle(piece, size):
	for i in range(piece):
		circle(size)
		lt(360/piece)

		
>>> myCircle(10,2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    myCircle(10,2)
  File "<pyshell#38>", line 3, in myCircle
    circle(size)
NameError: name 'circle' is not defined
>>> myCircle(10,100)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    myCircle(10,100)
  File "<pyshell#38>", line 3, in myCircle
    circle(size)
NameError: name 'circle' is not defined
>>> def myCircle(piece, size):
	for i in range(piece):
		circle(size)
		lt(360/piece)

		
>>> myCircle(10,100)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    myCircle(10,100)
  File "<pyshell#42>", line 3, in myCircle
    circle(size)
NameError: name 'circle' is not defined
>>> from turtle import*
>>> def myCircle(piece, size):
	for i in range(piece):
		circle(size)
		lt(360/piece)

		
>>> myCircle(10,100)
>>> myCircle(2,200)
>>> def myCircle(piece, size):
	for i in range(piece):
		pincolor(red)
		circle(size)
		lt(360/piece)

		
>>> myCircle(2,200)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    myCircle(2,200)
  File "<pyshell#50>", line 3, in myCircle
    pincolor(red)
NameError: name 'pincolor' is not defined
>>> def myCircle(piece, size):
	for i in range(piece):
		pencolor(red)
		circle(size)
		lt(360/piece)

		
>>> myCircle(2,200)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    myCircle(2,200)
  File "<pyshell#53>", line 3, in myCircle
    pencolor(red)
NameError: name 'red' is not defined
>>> def myCircle(piece, size):
	for i in range(piece):
		pencolor('red')
		circle(size)
		lt(360/piece)

		
>>> myCircle(2,200)
>>> def myCircle(piece, size):
	colors = ['red','blue','green']
	for i in range(piece):
		pencolor(color[i%3])
		circle(size)
		lt(360/piece)

		
>>> myCircle(8,100)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    myCircle(8,100)
  File "<pyshell#59>", line 4, in myCircle
    pencolor(color[i%3])
TypeError: 'function' object is not subscriptable
>>> def myCircle(piece, size):
	colors = ['red','blue','green']
	for i in range(piece):
		pencolor(colors[i%3])
		circle(size)
		lt(360/piece)

		
>>> myCircle(8,100)
>>> clear()
>>> myCircle(500,100)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    myCircle(500,100)
  File "<pyshell#62>", line 5, in myCircle
    circle(size)
  File "<string>", line 8, in circle
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 1988, in circle
    self.speed(0)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 2175, in speed
    self.pen(speed=speed)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 2460, in pen
    self._update()
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/turtle.py", line 567, in _delay
    self.cv.after(delay)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/tkinter/__init__.py", line 811, in after
    self.tk.call('after', ms)
KeyboardInterrupt
>>> сдуфк()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    сдуфк()
NameError: name 'сдуфк' is not defined
>>> clear()
>>> myCircle(13,25)
>>> clear()
>>> fd(70)
>>> lt(170)
>>> fd(70)
>>> home()
>>> cr()
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    cr()
NameError: name 'cr' is not defined
>>> clear()
>>> pencolor('black')
>>> fd(100)
>>> lt(60
   lt(60)
   
SyntaxError: invalid syntax
>>> lt(60)
>>> fd(100)
>>> lt(120)
>>> fd100
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    fd100
NameError: name 'fd100' is not defined
>>> fd(100)
>>> lt(120)
>>> lt(-120)
>>> lt(60)
>>> fd(100)
>>> clear()
>>> home()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lt(90)
>>> fd(300)
>>> home()
>>> clear()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> lt(90)
>>> fd(200)
>>> home()
>>> clear()
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> fd(100)
>>> lt(60)
>>> fd(100)
>>> lt(120)
>>> fd(100)
>>> lt(60)
>>> fd(100)
>>> 
>>> 
>>> def fower(piece, size):
	for i in range(piece):
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		fd(size)
		lt(60)
		fd(size)
		lt(120)

		
>>> fower(4,70)
>>> fower(10,70)
>>> def flower(piece, size,corner):
	for i in range(piece):
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		corner(lt(10))

		
>>> def flower(piece, size,corner):
	for i in range(piece):
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		lt(360/piece)

		
>>> def flower(piece, size):
	for i in range(piece):
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		lt(360/piece)

		
>>> flower(5,70)
>>> home()
>>> clear()
>>> flower(5,100)
>>> def flower(piece, size):
	for i in range(piece):
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		lt(360/piece)
		home()

		
>>> flower(6,100)
>>> clear()
>>> flower(6,100)
>>> def flower(piece, size):
	for i in range(piece):
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		fd(size)
		lt(60)
		fd(size)
		lt(120)
		lt(360/piece)

>>> flower(6,100)
>>> def flower(piece, size):
	for i in range(piece):
		fd(size)
		lt(45)
		fd(size)
		lt(130)
		fd(size)
		lt(45)
		fd(size)
		lt(130)
		lt(360/piece)

		
>>> clear()
>>> flower(6,100)
>>> flower(6,100)
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

		
>>> clear()
>>> flower(6,100)
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
		home()
		lt(90)
		back(300)

		
>>> clear()
>>> flower(6,100)
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

		
>>> clear
<function clear at 0x7fd064481b80>
>>> clear()
>>> flower(6,100)
>>> home()
>>> clear()
>>> flower(6,100)
>>> rh(90)
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    rh(90)
NameError: name 'rh' is not defined
>>> rt(90)
>>> fd(300)
>>> clear()
>>> home()
>>> clear()
>>> flower(6,100)
>>> flower(8, 200)
>>> flower(12,50)
>>> flower(3,150)
>>> rt(90)
>>> fd(400)
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

		
>>> home()
>>> clear
<function clear at 0x7fd064481b80>
>>> clear()
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
	for i in range(1)
	
SyntaxError: invalid syntax
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
>>> 