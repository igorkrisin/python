squares = [value ** 2 for value in range(1, 11)]
print(max(squares))

for i in range(1, 21, 2):
	print(i)

million = [value + 1 for value in range(1, 1000000)]
print(sum(million))

for i in range(3, 31, 3):
	print(i)

cub = [value ** 3 for value in range(1, 11)]
print(cub)

list_cub = []
for i in range(1, 11):
	list_cub.append(i)
print(list_cub)

for cub in list_cub:
	print(cub**3)

