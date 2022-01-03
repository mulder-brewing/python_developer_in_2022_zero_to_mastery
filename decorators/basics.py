# functions are 1st class citizens, they act like variables, can be passed around
def hello():
    print('hello')


# Higher Order Function - function that accepts a function as a parameter or returns a function
# map, filter, reduce are examples of HOF
def call_func(func):
    func()


def return_hello():
    return hello


greet = return_hello()
# reference hello is deleted but the function lives on because greet references it
del hello

call_func(greet)


# Decorator - function that wraps another function to enhance it
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print()
        func(*args, **kwargs)

    return wrap_func


@my_decorator
def bye(greeting, emoji=':('):
    print(greeting, emoji)


bye('bye bye', ':)')
bye('bye bye')

# performance decorator
from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return result

    return wrap_func


@performance
def long_time():
    for i in range(100000):
        i * 5


long_time()
