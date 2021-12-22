for item in 'Zero to Mastery':
    print(item)

for item in [1, 2, 3, 4, 5]:
    print(item)

for item in {1, 2, 3, 4, 5}:
    print(item)

for item in (1, 2, 3, 4, 5):
    print(item)
# can still use the last item after exiting the loop!
print(item)

dictionary = {
    'one': 1,
    'two': 2
}

# default is keys
for key in dictionary:
    print(key)

for value in dictionary.values():
    print(value)

for item in dictionary.items():
    print(item)

# items with unpacking
for key, value in dictionary.items():
    print(key, value)

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

# range
for num in range(1, 51, 1):
    print(num)

# in reverse
for num in range(50, 0, -1):
    print(num)

print(range(100))
# same as
print(range(0, 100))

# list from range
print(list(range(10)))

# enumerate - gives index while iterating
for i, char in enumerate('hello'):
    print(i, char)

for i, num in enumerate(list(range(20, 100))):
    if num == 50:
        print(f'index of 50 is {i}')

# while loops - they have an else statement
i = 100
while i < 110:
    print(i)
    i += 1
else:
    print('done')

# break in while loop - else does not get run if there is a break
# break also works in for loop
i = 200
while True:
    print(i)
    i += 1
    if i == 211:
        break
else:
    print('done')

# continue
i = 200
while True:
    i += 1
    if i == 211:
        break
    if i % 2 != 0:
        continue
    print(f'even number: {i}')
else:
    print('done')

# pass is only good as a placeholder for actual logic
for num in [1, 2, 3]:
    # TODO: do some logic
    pass
