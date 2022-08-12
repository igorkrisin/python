a=[3,4,8,2,9,1]
b = []
for i in range(len(a)):
    b.append(a[i]*2)

#print(b)  # [6,8,16,4,18,2]
b = []
for i in range(len(a)):
    b.append(a[i])
    b.append(a[i])

#print(b)  # [3,3,4,4,8,8,2,2,9,9,1,1]

b = []
for i in range(len(a)):
    if a[i]%2==0:
        b.append(a[i])

#print(b)  # [4,8,2]

...

#print(b) # [1,9,2,8,4,3]

b = []
for i in range(1,len(a)+1):
    b.append(a[-i])
#print(b)
b = []
def revers (a):
    b = []
    for i in range(1,len(a)+1):
        b.append(a[-i])
    return b
#print(revers(revers([15,4,6,0])))

[6,9,2,7]
[7,2,9,6]

def revers (a):
    b = []
    for i in range(len(a)):
        b.insert(0,a[i])
    return(b)
#print(revers([44,55,78,0]))

#Функция возвращает количество чисел а из массива b
def count_element (a, b):
    c = b.count(a)
    return(c)
#print(count_element(2,[3,2,2,2,2,4,5]))

#2. Функция equal_elements([2,2,2,2]) -> True, возвращает истину если
#все элементы массива одинаковы, ложь,
#если хотя бы один элемент не равен остальным

def equal_elements(a):
    for i in range(len(a)):
        if a.count(a[i]) == len(a):
            a = True
            return a
        else:
            a = False
            return a
print(equal_elements([]))


#3. Функция merge([2,5,9],[1,4,8]) -> [1,2,4,5,8,9], сливающая два
#отсортированных массива так,
#чтобы результриующий массив был отсортирован.


def merge(a,b):
    c = []
    c = a+b
    c.sort()
    return c
#print(merge([2,5,9],[1,22,56]))

#4. Функция is_sorted([3,7,9]) -> True,
#если массив отсортирован по возрастанию,
#False в противном случае

def is_sorted(c):
    print(c)
    if c == c.sort():
        print(c)
        print(c.sort())
        return True
    else:
        return False
        print(c)
        print(c.sort())
print(is_sorted([3,7,9]))

#print(c.sort())
#print(a.append(''))
    
#a=[3,1,9]
#for i in range(len(a)):
	#a.append(a[i])
#print(a)
#if b == a.sort():
    #print(True)
#else:
   # print(False)
    


#5. Функция max([3,7,9,4]) -> 9 возвращает максимальный элемент массива.


