from dataclasses import replace


spam = ['apples', 'bananas', 'tofu', 'cats', 'gora', 'goga']
temp = ''
temp += spam[0]
for i in range(1, len(spam)-1):
    temp += ', ' + spam[i]
temp += ' and ' + spam[-1]

a = "4556364607935616"
s=""
for i in range (len(a) - 1):
    s += a[i - 3]
#print(s)
n = 5

#for i in range(1, n+1):
   # print(i)

def myDivmod(a, b):
    
    print(a//b)
    print(a%b)
    c = (a//b, a%b,)
    print(c)

myDivmod(7857252, 4949)