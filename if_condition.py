alien_color = 'red'


if alien_color == 'green':
	print('the player gets five points')
elif alien_color == 'yellow':
	print('the player gets ten points')
elif alien_color == 'red':
	print('the plaer gets fifteen points')

fruit = ['apple', 'banana', 'orange']
if 'strawberry' in fruit:
	print('you really like apples!')

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for i in requested_toppings:
	if i in available_toppings:
		print(f"Adding{requested_toppings}.")
	else:
		print(f"sorry we don't {i}.")
print('\nFinished making your pizza')


list_name = ['admin', 'jussy', 'jully', 'yossy', 'kat']
if list_name:
	for name in list_name:
		if name == 'admin':
			print(f'Hello {name}, would you like to see status report?')
		else:
			print(f'Hello {name}, thank you for logging in again')
else:
	print('We need to ind some users')

current_users = ['fred', 'jussy', 'jully', 'yossy', 'kat']
new_users = ['jessica', 'alba', 'jully', 'jussy', 'babell']

for i in new_users:
	if i.lower() in current_users:
		print('enter new name, this name used other user')
	else:
		print('name available')





