# Common Errors
# SyntaxError, NameError (undefined variable), IndexError (list), KeyError (dictionary), etc.

while True:
    try:
        age = int(input('what is your age? '))
        10 / age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter age higher than 0')
    else:
        print('thanks!')
        break
    finally:
        print('finally done')


def my_sum(num1, num2):
    try:
        return int(num1) + int(num2)
    except (TypeError, ValueError) as err:
        print(f'please enter numbers: {err}')


print(my_sum('A', 2))


def validate_id(id):
    if id <= 0:
        raise ValueError('ID must be > 0')


validate_id(0)
