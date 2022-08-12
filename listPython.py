transport = ['machine', 'moto', 'airplane']
transport.append('monocicle')
transport.insert(1, 'gidrocicle')
print(transport)
remove_trs = 'moto'
transport.remove('moto')
print(transport)
print("remove ", remove_trs)

poped_transport = transport.pop()



print(poped_transport)



gest = ['ivan', 'marya', 'fedor']

gest[1] = "juliya"



gest.insert(0, "valeriy")
gest.insert(len(gest)//2, "petr")
gest.append('nastya')
print(gest)
print(len(gest))
i = 1
while(len(gest) > 2):
	print('i: ', i)
	gest.pop()
	print(gest)
	print(len(gest))
	print(f"i'm sorry {gest[i].title()}, see you later")

del gest[1]
del gest[0]
print(gest)

for i in range(len(gest)):
	print(f"hello, my freind {gest[i].title()}")