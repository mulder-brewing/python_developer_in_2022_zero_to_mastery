# pure function
# 1. same input, always the same output
# 2. no side effects (affecting outside world) like printing something, changing variable outside scope, mutate inputs

# this is pure
def multiply_by2(my_list):
    new_list = []
    for item in my_list:
        new_list.append(item * 2)
    return new_list


# not pure, input is mutated
def multiply_by2_not_pure(my_list):
    for i in range(0, len(my_list)):
        my_list[i] *= 2
    return my_list


num_list = [1, 2, 3, 4, 5, 6]
print(multiply_by2(num_list))
print(num_list)


# This mutates the list
# print(multiply_by2_not_pure(to_multiply))
# print(to_multiply)


# map
def times_two(num):
    return num * 2


print(list(map(times_two, num_list)))
# original list is not mutated
print(num_list)


# filter
def is_even(num):
    return num % 2 == 0


print(list(filter(is_even, num_list)))
# original list is not mutated
print(num_list)

# zip - makes tuples out of each corresponding index from the multiple iterables
names = ['Bob', 'Bill', 'Ben']
ages = (10, 15, 24)
emails = ['bob@mail.com', 'bill@mail.com', 'ben@mail.com']
print(list(zip(names, ages, emails)))

# reduce - accumulator function reduces a list to some value
from functools import reduce


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, num_list, 0))

# lambda expressions
print(list(map(lambda num: num * 2, num_list)))
print(list(filter(lambda num: num % 2 == 0, num_list)))

# comprehensions - list, set, dictionary
my_list = [char for char in 'hello']
my_list2 = {num for num in range(0, 100)}
my_list3 = [num * 2 for num in range(0, 100)]
my_list4 = [num ** 2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
my_dic = {k: v ** 2 for k, v in simple_dict.items() if v % 2 == 0}
my_dic2 = {num: num * 2 for num in [1, 2, 3]}
print(my_dic)
print(my_dic2)
