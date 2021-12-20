print(type('hi there'))
print(type("hello there"))

username = 'new_user'
password = 'password'

long_multiline_string = '''
WOW
O O
---
'''
print(long_multiline_string)

# concatenation
first_name = 'first'
last_name = 'last'
full_name = first_name + ' ' + last_name
print(full_name)

# type conversion
print(type(str(100)))

# Escape Sequences
weather = 'It\'s sunny'
print(weather)
weather = "It's \"kind of\" sunny"
print(weather)
# tab and new line special
weather = "\tIt's \"kind of\" sunny\n Hope you have a nice day"
print(weather)

# Formatted Strings
name = 'Jim'
age = 55
# Python 3
print(f'Hello {name}.  You are {age} years old')
# Python 2
print('Hello {}.  You are {} years old'.format(name, age))
print('Hello {new_name}.  You are {new_age} years old'.format(new_name='new', new_age=22))

# String Indexes
indexes = '01234567'
print(indexes[0])
print(indexes[1])

# [start:stop:stepover]
print(indexes[0:8:2])
print(indexes[0:])
print(indexes[:8])
print(indexes[::])

# traverse from end backwards
print(indexes[-1])
print(indexes[-2])
# reverse order
print(indexes[::-1])

# Length
print('length is ' + str(len(indexes)))

# Immutability
immut_str = '01234567'
# will cause an error - immut_str[0] = '8'
immut_str = '8' + immut_str[1:]
print(immut_str)

# String Methods
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be', 'me'))
# strings are immutable
print(quote)
