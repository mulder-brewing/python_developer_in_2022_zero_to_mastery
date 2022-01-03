import utils.utility
from modules.shopping.more_shopping import shopping_cart as cart
from modules.shopping.more_shopping.shopping_cart import buy
from utils.utility import *

print(utils.utility)
print(utils.utility.divide(100, 10))

print(cart.buy('orange'))
print(buy('apple'))

print(divide(8, 4))
print(multiply(2, 3))
# name collision with built in max function
# print(max(1, 2, 3, 4, 5))

# __main__ is given as name to the file that is run
print(__name__)
if __name__ == '__main__':
    print('running main')
