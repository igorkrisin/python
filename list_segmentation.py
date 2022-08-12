players = ['mariya', 'alexandr', 'petr', 'ivan']
print(players[-3:])
print(f'Here are the first players on my team: ')
for player in players[:3]:
	
	print(f'{player.title()}')
plaeyrs2 = []
plaeyrs2 = players[:]
plaeyrs2.append('fedor')
print(plaeyrs2)


my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
friend_foods = my_foods[:]
print("Three items from the middle of the list are:  ")
print(my_foods[:3])
print("the irst three in the list are: ")
print(my_foods[1:-2])
print("The last three items in the list are: ")
print(my_foods[:-2])



my_favorite_pizza = ['mariya', 'alexandr', 'petr', 'ivan']
friend_favorite_pizza = my_favorite_pizza[:]
my_favorite_pizza.append('with cheese')
friend_favorite_pizza.append('with apple')
print('My favorite pizza are: ')
for pizza in my_favorite_pizza:
	print(pizza)

print('My friend favorite pizza are; ')
for pizza in friend_favorite_pizza:
	print(pizza)












