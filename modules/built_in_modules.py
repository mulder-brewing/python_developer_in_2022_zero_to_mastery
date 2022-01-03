import random

# help(random)
print(dir(random))

print(random.random())
print(random.randint(1, 100))
print(random.choice([1, 2, 3, 4, 5]))

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

import sys

print(sys)
# when file is run from command line, can get arguments passed in
print(sys.argv)
