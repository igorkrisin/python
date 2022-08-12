# statement - инструкция
# expression - выражение
# statement vs. expression
'''x=42
print(...)'''

def gen(*a):
    if len(a) == 3:
        b=a[0]
        c=a[1]
        d=a[2]
    elif len(a)==2:
        b=a[0]
        c=a[1]
        d=1
    elif len(a)==1:
        b,c,d=0,a[0],1
    if d>0:
        while b<c:
            yield b
            b+=d
    elif d<0:
        while b>c:
            yield b
            b+=d
for i in gen(6):
    print(i)

def bar():
    i=0
    while True:
        yield i
        i+=1

for i in bar(): print(i)

1,1*2,1*2*3,1*2*4,...

    b
  a
a b
1,1,2,3,5,8,...
1,2,3,4,5,6,...

#foo, bar, foobar

"""def foo(*a):
    return a


print(foo(5,7,2,0))"""


'''(while True: pass)+1

if x>0:
   print(x)
else:
   print(y)

print(x if x>0 else y)'''