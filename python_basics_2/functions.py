# positional arguments
def say_hello_positional(name, emoji):
    print(f'hello {name} {emoji}')


print(say_hello_positional)
say_hello_positional('user', '😊')


# keyword arguments with defaults
def say_hello_keyword(name='default_name', emoji='😒'):
    print(f'hello {name} {emoji}')


say_hello_keyword(emoji='😊', name='user')
say_hello_keyword()


# return, and functions can contain functions
def my_sum(num1, num2):
    """ Sums two nums """  # This is a Docstring to document the method

    def perform_sum(n1, n2):
        return n1 + n2

    return perform_sum(num1, num2)


# print docstring for method - 2 options
help(my_sum)
print(my_sum.__doc__)

print(my_sum(4, 5))


# *args (variable number of args as a tuple)
# **kwargs (variable number of keyword args as a dict)
# important when mixing that they appear in this order
def super_func(positional, *args, my_defult='default', **kwargs):
    print(f'psotional: {positional}')
    print(f'args: {args}')
    print(f'default: {my_defult}')
    print(f'kwargs: {kwargs}')


super_func('my positional arg', 1, 2, 3, 4, num1=5, num2=10)

# scope - little weird that variables within if are accessible outside if
if True:
    x = 10

print(x)

# global
a = 1


def scope():
    # parent
    a = 5

    def child():
        # local
        a = 7
        return a

    return child()


# Scope goes local, parent, global, and lastly built in puthon functions
print(a)
print(scope())

# Access global variables inside func
total = 0


def increment():
    global total
    total += 1
    return total


print(increment())
print(increment())


# nonlocal - pull a variable from outside local scope
def outer():
    x = 'nonlocal'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print(f'inner: {x}')

    inner()
    print(f'outer: {x}')


outer()
