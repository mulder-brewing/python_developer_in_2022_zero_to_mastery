# Square
my_list = [5, 4, 3]
print(list(map(lambda num: num ** 2, my_list)))

# List sorting

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(sorted(a, key=lambda tup: tup[1]))
