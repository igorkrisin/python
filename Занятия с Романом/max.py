#5. Функция max([3,7,9,4]) -> 9 возвращает максимальный элемент массива.
def maxi(a):
    
    return a[-1]
#print(maxi([3,71,22,44]))

'''Функция is_sorted([3,7,9]) -> True,
если массив отсортирован по возрастанию,
False в противном случае'''

a=[3,3,3,3,3,0,3,3]

for i in range(len(a)-2):
    

    while a[i]==a[i+1]:
        i+=1
        print(i)
    else:
        print(False)
