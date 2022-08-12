# Функция count_element(2,[1,8,9,2,5,2,2]) -> 3, подсчитывает кол-во элементов
#массива равных первому аргументу
import timeit
def count_element(a,b):
        count = 0
        for i in range(len(b)):
            if a==b[i]:
                count += 1
        return count
print(count_element(2,[1,8,9,2,5,2,2]))

def count_element(a,b): return sum([1 for i in b if a==i])
print(timeit.timeit('count_element(2,[1,8,9,2,5,2,2])',number=100,globals=globals()))


'''Функция equal_elements([2,2,2,2]) -> True, возвращает
истину если все элементы массива одинаковы, ложь, если хотя
бы один элемент не равен остальным'''


def equal_elements(a):
    for i in range(len(a)-1):
        if a[i]!=a[i+1]:
            return False
    return True
print(equal_elements([2,2,2,2]))

def count_element(a,b): return sum([1 for i in b if a==i])
print(count_element(2,[1,8,9,2,5,2,2]))
