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

#функция merge принимает на вход 2 массива соединяетих и сортирует

def merge(a,b):
    c = a+b
    #print(c)
    if c == []:
        return c
    min = []
    max = []
    for i in range(1,len(c)):
        if c[0]>c[i]:
            min.append(c[i])
        else:
            max.append(c[i])
    min = merge(min)
    max = merge(max)

    return min+[c[0]]+max
print(merge([0,6,4,7,2,3],[9,11,1000,73,22]))






            
            



















