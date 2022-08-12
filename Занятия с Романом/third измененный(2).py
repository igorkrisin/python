def is_sorted(a):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            return False
        
            
    return True
#print(is_sorted([8,3,5,7]))

def bubble_sort(a):
    while not is_sorted(a):
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
    return a

import timeit


#print(timeit.timeit('bubble_sort([5,9,1,3,4,7])',number=100,globals=globals()))

def bubble_sort(a):
    
    while True:
        bubble = 0
        for i in range(len(a)-1):
        
            if a[i]>a[i+1]:
                bubble = 1
                a[i],a[i+1]=a[i+1],a[i]
        if bubble == 0:
            break
                
    return a

#print(timeit.timeit('bubble_sort([5,9,1,3,4,7])',number=100,globals=globals()))

#max([3,5,8,0,4])  -> 8

def max(a):
    planka=a[0]
    for i in range(len(a)):
        if a[i]>planka:
            planka = a[i]
    return planka
#print(max([-3,-5,-7,-10,-2]))


[5,9,1,8,3,4]
[1,3,4,5,8,9]

def selection_sort(a):
    for i in range(len(a)):
        planka = i
        for x in range(i,len(a)):
            if a[x]<a[planka]:
                planka = x
        a[planka],a[i] = a[i],a[planka]
    return a
#print(selection_sort([5,9,1,4,6,8]))


'''[5,9,1,4,0,8,7,5]
1 4 0  - 0 1 4
9 8 7  - 7 8 9 
[0,1,4,5,7,8,9]'''

def qsort(a):
    if a == []:
        return a
    min = []
    max = []
    for i in range(1,len(a)):
        if a[0]>a[i]:
            min.append(a[i])
        else:
            max.append(a[i])
    min = qsort(min)
    max = qsort(max)

    return min+[a[0]]+max
#print(qsort([0,6,4,7,2,3]))



#[5,7,0,1,9,2,3,4]
#[5,7,0,1][9,2,3,4]

#[0,1,2,3,4,5,7,9]

# не (a и b) = (не a) или (не b)
# не (a или b) = (не a) и (не b)

            
def merge(a,b):
    c=[]
    while a != [] and  b != []:   # (not a==[]) or b==[]
        if a[0]<b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    c.extend(a)
    c.extend(b)
    return c
#print(merge([1,4,8,12],[2,3,7,10]))

def merge_sort(a):
        # ploho
    if a == [] or len(a)==1:
        return a
    n = len(a)//2
    return merge(merge_sort(a[:n]),merge_sort(a[n:]))
#print(merge_sort([2,1,5,6,7,8,0,99,65]))


#[42]
#[] [42]
#    [] [42]
#       [] [42] 
#          ....

def gnom_sort(a):
    i=1
    while i<len(a):
        if a[i-1]<a[i]:
            i+=1
        else:
            a[i-1],a[i] = a[i],a[i-1]
            i-=1
            if i == 0:
                i+=1
    return a
#print(gnom_sort([2,14,9,0,18,5,1]))


'''4!=1*2*3*4

i=1,2,3,4
n=24

#1!=1
#2!=2
#3!=1*2*3=6
#4!=1*2*3*4=24
#5!=1*2*3*4*5=120=24*5=4!*5
#6!=5!*6
#n!=(n-1)!*n

def fact(a):
    n=1
    for i in range(1,a+1):
        n=n*i
    return n

#print(fact(5))

def factRecur(n):
    if n!=1:
        return factRecur(n-1)*n
    else:
        return 1
#print(factRecur(5))

1,1,2,3,5,8,13,21...
1,2,3,4,5,6,7, 8...

n = (n-1)+(n-2)'''
...
'''def fib(n):
    if n==1 or n==2:
       return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(5))
        
#fib(6)=fib(5)+4=5+4
#fib(6)=5+3

for i in range(1,51):
    #print(fib(i))'''


    
def fib(n):
    a=1
    b=1
    for i in range(2,n):
        a,b=b,a+b
    return b
#print(fib(6))

'''my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in my_list)
for val in gen_obj:
    print(val)'''

def bar():
    i=0
    while True:
        yield i
        i+=1

#for i in bar():print(i)
from itertools import islice

def fact_gen():
    n=1
    i=1
    while True:
        yield n
        n=n*i
        i+=1
for i in islice(fact_gen(),10):print(i)


def fib_gen():
    n=1
    i=1
    yield i
    yield n
    while True:
        n,i=i,n+i
        yield i       
#for i in islice(fib_gen(),10):print(i)






























