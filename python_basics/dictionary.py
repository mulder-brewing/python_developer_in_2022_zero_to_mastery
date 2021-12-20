dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}

print(dictionary)
print(dictionary['a'])

my_list = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': True
    }
]
print(my_list)

dictionary = {
    123: [1, 2, 3],
    123: [4, 5, 6],
    True: 'hello',
    'x': True
}

print(dictionary[123])
print(dictionary[True])

# get is safe if key doesn't exist, returns None
print(dictionary.get('z'))
# get with default
print(dictionary.get('z', 777))
# check for key with in
print('x' in dictionary)
print('z' in dictionary)
print('hello' in dictionary.values())

# items
print(dictionary.items())

# not used much but is available
user = dict(name='Someone', age=55)
print(user)

# copy and clear
user_2 = user.copy()
user.clear()
print(user)
print(user_2)

# pop
print(user_2.pop('age'))
print(user_2)
