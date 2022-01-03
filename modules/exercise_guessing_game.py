import random
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

print(f'Guess a random number between {start} and {end}')
random_num = random.randint(start, end)

while True:
    try:
        guess = int(input('Your guess? '))
        if guess < start or guess > end:
            print('not within the range')
            continue
        if guess == random_num:
            print("Correct!!")
            break
        print('Wrong number, guess again')
    except ValueError:
        print('Not a number')
