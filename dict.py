allien_0 = {'color': 'green', 'points': 5}

new_points = allien_0['points']
print(f'You just earned {new_points} points!')

allien_0['x_position'] = 0
allien_0['y_position'] = 0
print(allien_0)

allien_0 = {}
allien_0['color'] = 'green'
allien_0['points'] = 5
print(allien_0)

allien_0['color'] = 'yellow'
print(allien_0)

allien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {allien_1['x_position']}")

del allien_1['x_position']

print(allien_1,'\n\n\n')

man = {
	'first_name': 'igor',
	'last_name': 'Krysin',
	'age' :36,
	'city': 'Spb',
	}
print(man['first_name'])
print(man['last_name'])
print(man['age'])
print(man['city'])


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
user_0['width'] = 85
user_0['hight'] = 172
for key, value in user_0.items():
	print(f'\nKey: {key}')
	print(f'Value: {value}')

for key,value in user_0.items():
	print(f'{key}', f'{value}')

name_river = {
	'neva': 'russia',
	'nile': 'egypt',
	'amasonca': 'usa',
	}
for key, value in name_river.items():
	print(f'The {key.title()} runs through {value.title()}')

for key in name_river.values():
	print(key)

favorite_languages = {
      'jen': 'python',
      'sarah': 'c',
      'edward': 'ruby',
      'phil': 'python',
      }
list_for_poll = {
	'jen': 'python',
  	'sarah': 'c',
   	'piter': 'c++',
    'kat': 'js',
}

for languages in favorite_languages:
	if languages in list_for_poll:
		print(f"Thank's {languages.title()} for takes our poll")
	else:
		print(f"Dear {languages.title()} the following languages have been menitioned")

