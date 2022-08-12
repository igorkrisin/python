
a = 100100
s = str(a)
count = 0

for i in range(len(s) - 1, 0, -1):
    if int(s[i]) == 0:
        print("ok")
    else:
        break
    
def backward_string(val: str) -> str:
    temp = ""
    for i in range(len(val) - 1, -1 , -1):
        print("i", i)
        temp += val[i]
    return temp

def remove_all_before(items: list, border: int):
    temp = items.copy()
    for i in range(0, len(items) - 1):
        
        if items[i] != border:
            temp.remove(items[i])
        else:
            return temp
    
    return items


k = '55  55'
for i in range(0, len(k)):
    if k.isdigit() and i == " ":
        
        print(k.isdigit())
        
        
        
def is_all_upper(text: str) -> bool:
    if all([i.isdigit() or i == ' ' for i in text]):
        return True
    elif text.isupper():
        return True
    else:
        return False
    
    
def replace_first(items: list):
    if items == []:
        return []
    newArr = []
    for i in range(1, len(items)):
        newArr.append(items[i]) 
    newArr.append( items[0])
    return newArr
        

print(replace_first([]))