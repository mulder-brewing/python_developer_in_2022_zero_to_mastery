li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
# can mix
li3 = [1, 2, 'a', True]

print(li)
print(li2)
print(li3)

amazon_cart = ['notebook', 'sunglasses']
print(amazon_cart[1])

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li)
# [start:stop:stepover]
print(li[0:2])
print(li[0::2])
# list is mutable
# making a copy
li2 = li[:]
li2[0] = 100
print(li2)
li2.append(10)
print(li2)
print(li)

# Matrix 2D list
matrix = [
    [1, 0, 5],
    [0, 1, 0],
    [1, 0, 1]
]

for line in matrix:
    print(line)

print(matrix[0][2])

# List methods
print('-----------List Methods-----------')
# Adding
li.append(10)
li.insert(3, 88)
li.extend([200, 201])
print(li)

# Removing
print(li.pop())
print(li.pop(3))
li.remove(200)
print(li)
li.clear()
print(li)

# Index
li = ['a', 'b', 'c', 'd', 'e']
print(li.index('d'))
print('d' in li)

# Count
print(li.count('d'))
li.append('d')
print(li.count('d'))

# Sort
# sort mutates
li = ['a', 'b', 'c', 'e', 'd']
li.sort()
print(li)

# sorted does not mutate
li = ['a', 'b', 'c', 'e', 'd']
print(sorted(li))
print(li)

# copy and reverse
copy = li.copy()
# mutate reverse
li.reverse()
print(li)
print(copy)
# non mutate reverse
print(copy[::-1])

# range
print(list(range(101)))

# join
new_sentance = ' '.join(['hi', 'my', 'name', 'is', 'JOJO'])
print(new_sentance)

# list unpacking
basket = [1, 2, 3, 4, 5, 6, 7, 8]
a, b, c, *other, d = basket
print(a)
print(b)
print(c)
print(other)
print(d)
