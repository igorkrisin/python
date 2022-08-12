def square(h):
    a= h*h
    b= 4*h
    return a,b
#print(square(5))

max=0
for i in range(0,101):
    if i%2 == 0 and i % 3 == 0:
        if i > max:
            max = i
        #print(i)
i=0
while i<10:
    
    i+=1
#print(i)

f = open("ex.txt","r")
#f.write("\nHello world")
print(f.read())
""" for line in f:
    print(line) """
f.close()