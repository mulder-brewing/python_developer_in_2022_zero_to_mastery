# If statements
is_old = True
is_licensed = True

if is_old and is_licensed:
    print('you can drive')
else:
    print('you cannot drive')

print('check')

# Truthy and Falsy
print(bool('hello'))
print(bool(''))

print(bool(5))
print(bool(0))

print(bool(['']))
print(bool([]))

username = 'johnny'
password = 'password'
if username and password:
    print('username and password present')

# Ternary - I like ? : more but just what you're used to I suppose
print('is true') if True else print('is false')

# Short Circuiting
is_friend = True
is_user = False

if is_friend or is_user:
    print('best friends')

# logical operators
# and, or, >, <, ==, !=, <=, >=, etc
print(1 < 2)
print(1 > 2)
print(1 == 2)
print(1 != 2)
print('a' > 'b')
print('a unicode: ' + str(ord('a')))
print('b unicode: ' + str(ord('b')))

# not
print(not True)
print(not False)

print('----------- is vs == -------------')

print('\n==')
print(True == 1)  # True
print('' == 1)  # False
print([] == 1)  # False
print(10 == 10.0)  # True
print([] == [])  # True

# is needs to be same location in memory
print('\nis')
print(True is 1)  # False
print(True is True)  # True
print('1' is 1)  # False
print('1' is '1')  # True
print([] is 1)  # False
print(10 is 10.0)  # False
print(10 is 10)  # True
print([] is [])  # False

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a is a)
