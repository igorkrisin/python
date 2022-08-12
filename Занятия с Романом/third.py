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



'''5. Функция max([3,7,9,4]) -> 9 возвращает максимальный элемент массива.'''


def max(a):
    
    while True:
        bubble = 0
        for i in range(len(a)-1):
            if a[i]>a[i+1]:
                bubble = 1
                a[i],a[i+1]=a[i+1],a[i]
        if bubble == 0:
            break
                
    return a[-1]

print(max([3,7,9,4]))


#Функция возвращает слияние двух массивов





















