def fibMem(numb, dict):
    dict = {}
    if (len(dict) != 0):
        return dict[numb]
    elif numb == 1 or numb == 2:
        dict[numb] = 1
        return 1
    else:
        temp = fibMem(numb - 1, dict) + fibMem(numb - 2, dict)
        dict[numb] = temp
        return temp
dict = {}


def perm(str):
    if str == "":
        return [""]
    else:
        arr = []
        for i in range(0, len(str)):
            temp = perm(str[:i]+str[i+1:])
            for j in range(0, len(temp)):
                arr.append(temp[j]+str[i:i+1])
    return arr

print(perm("abc"))

