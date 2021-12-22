my_set = {1, 2, 3, 4, 5}
print(my_set.add(100))
print(my_set.add(2))
print(my_set)

my_arr = [1, 2, 3, 4, 5, 5]
new_set = set(my_arr)
print(new_set)

print(1 in my_set)
copy = my_set.copy()

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# difference - does not update
print(my_set.difference(your_set))
print(my_set)

# discard
# my_set.discard(5)
# print(my_set)

# difference update - remove the duplicates
# my_set.difference_update(your_set)
# print(my_set)

# intersection
print(my_set.intersection(your_set))
# shortcut
print(my_set & your_set)

# isdisjoint - do they have nothing in common
print(my_set.isdisjoint(your_set))

# union - all unique values between the 2 sets
print(my_set.union(your_set))
# shortcut
print(my_set | your_set)

my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# issubset - entirety of set is part of other set
print(my_set.issubset(your_set))
print(your_set.issubset(my_set))

# issuperset - entirety of other set is part of this set
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))
