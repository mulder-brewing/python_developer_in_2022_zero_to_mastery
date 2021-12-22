# Same as list but immutable
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))
print(my_tuple[1])
print(5 in my_tuple)

dictionary = {
    (1, 2): [1, 2, 3],
    123: [4, 5, 6],
    True: 'hello',
    'x': True
}

print(dictionary[(1, 2)])

# can slice tuples
new_tuple = my_tuple[1:2]
print(new_tuple)

# unpacking
x, y, z, *other = my_tuple
print(x)
print(y)
print(z)
print(type(other))

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))
