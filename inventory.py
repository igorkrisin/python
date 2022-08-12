stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print('inventory: ')
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print('Total number of items: ' + str(itemTotal))

#displayInventory(stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin','gold coin', 'ruby']

def maskify(cc):
    print(len(cc)-1)
    print(len(cc)-5)
    temp = ""
    if len(cc) < 5:
        return cc
    for i in range(len(cc)):
        if i < len(cc)-4:
           temp += "#"
        else:
            temp += cc[i]
    return temp

def in_asc_order(arr):
    for i in range(len(arr) - 1):
        if arr[i]>arr[i+1]:
            return False
        else:
            continue
    return True #(True or false)

#print(in_asc_order([9,8,7,6,5,4,3,2,1]))

def comp(array1, array2):
    # your code