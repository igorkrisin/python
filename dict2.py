users = {
      'aeinstein': {
          'first': 'albert',
          'last': 'einstein',
          'location': 'princeton',
          },
      'mcurie': {
          'first': 'marie',
          'last': 'curie',
          'location': 'paris',
          },
}


for username, user_info in users.items():
 # print(f'username: {username}')
  full_name = f"{user_info['first']} {user_info['last']}"
  location = user_info['location']
  #print(f"\tFull name: {full_name.title()}")
  #print(f"\tLocation: {location.title()}")


two_man = {
  
  'i': {
  'first_name': 'igor',
  'last_name': 'krysin',
  'age' :36,
  'city': 'Spb',
  },
  'freind': {
  'first_name': 'andrew',
  'last_name': 'kuchin',
  'age' :36,
  'city': 'yaroslavl',
  },
}

for usename, use_info in two_man.items():
  #print(f'username: {usename}')
  full_name = f"{use_info['first_name']} {use_info['last_name']}"
  loc = f"{use_info['city']}"
  old = f"{use_info['age' ]}"
  #print(f'full name: {full_name}')
  #print(f'location: {loc}')
  #print(f'age: {old}')


sharlis = {'eyes': 'green', 'color': 'grey'}
barsick = {'eyes': 'blue', 'color': 'braun'}
pets = [sharlis, barsick]

#for pett in pets:
  #print(f'{pett["eyes"]}')



favorite_places = {
  'igor': ['kiprus', 'greece'],
  'olya': ['turkey',  'egipt']
}

#for man, places in favorite_places.items():
  #print(f"man: {man.title()} ")
  #for place in places:
   # print(place.title())


cities = {
  'moscow': {'country' : 'russia', 'population': '20 mill', 'fact': 'big and ugly'} ,
  'spb' : {'country' : 'russia', 'population': '10 mill', 'fact': 'big and beautiful'},
  'bankog': {'country' : 'russia', 'population': '50 mill', 'fact': 'big and ugly'},
}

for name_city, descrp in cities.items():
  print(f'name city: {name_city.title()}')
  print(f'country: {descrp["country"].title()}, population: {descrp["population"]}, fact: {descrp["fact"]}')

  print()

  def fact(x):
    if x == 0:
      return 1
    if x == 1:
      return 1
    return x * fact(x - 1)

print(fact(6))
 












