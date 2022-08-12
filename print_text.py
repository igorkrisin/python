name = "eric"
name = name.title()
print("hello "+ name + ", wold you like to learn some Python today")

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new." '

user_name = ' Igor Krysin	'
print(user_name)


def my_lstrip(string):
	new_str = ''
	for i in range(0, len(string)):
		if(string[i] != ' '):
			new_str = string[:i]
	print(new_str)


my_lstrip(user_name)
print(user_name.lstrip())