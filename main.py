import getpass
print('*' * 50)
user_pass = getpass.getpass("Enter your password")
print(user_pass)

some_string = 'My name is John. My name is Marta'
# print(some_string)
# print(id(some_string))
#
# new_string = some_string.lower()
# print(some_string)
# print(new_string)

# print(some_string.center(20, '*'))
# print(some_string.lower())
# print(some_string.upper())
#
# print('Straße'.lower())
# print('Straße'.upper().lower())

# print(some_string.replace('My', 'Your', 1))

# print(some_string.casefold())
# print('Straße'.casefold())


# print(some_string.capitalize())
# print(some_string.swapcase())
# print(some_string.title())

# some_string = some_string.replace('M', 'N')  bad idea
# print(some_string.replace('N', 'P'))

# translate_map = str.maketrans('MN', 'NP')
# translate_result = some_string.translate(translate_map)
# print(translate_result)

user_name = input('Enter your name >>> ').title()
print(user_name)

print('*' * 50)
