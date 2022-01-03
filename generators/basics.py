# range is a generator
# range(100)
# list(range(100))


def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)
    return result


my_list = make_list(100)
print(my_list)

giant_list = list(range(10000))
print(giant_list)


# iterable objects have a __iter__ method but list and range are different.
# returning a list consumes memory for every item, where range only holds one item in memory at a time using yield

def generator_func(num):
    for i in range(num):
        yield i


g = generator_func(10)
# can manually step through generator using next
print(g)
print(next(g))
print(next(g))
for item in g:
    print(item)

# if next is called when there is no next, it causes a StopIteration error
next(g)
