


def is_prime(a):
    k=0
    for i in range(2,a):

        if a%i==0:
            k+=1
    if k<=0:
        return True
    else:
        return False


def replace_first(arr):
    if len(arr) <= 1:
        return arr
    newArr = []
    for i in range(1, len(arr)):
        newArr.append(arr[i])
        print(arr[i])
    newArr.append(arr[0])    
    return newArr
    

def max_digit(num):
    strnum = str(num)
    if len(strnum) <= 1:
        return num
    maxNum = strnum[0]
    for i in range(0, len(strnum)):
        if strnum[i]>maxNum:
            maxNum = strnum[i]
    return int(maxNum)
        
print(max_digit(3053456))
""" a  = 123
print(len(str(a)))
for i in str(a):
    print(i) """