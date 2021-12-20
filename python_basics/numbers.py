def print_result_and_type(num):
    print('result: ' + str(num))
    print('type: ' + str(type(num)))
    print()


# int and float
print_result_and_type(2 + 4)
print_result_and_type(2 - 4)
print_result_and_type(2 * 4)
print_result_and_type(2 / 4)
print_result_and_type(0)

print(type(2 + 4) == int)
print(type(2 / 4) == float)

print_result_and_type(9.9 + 1.1)

# 2 to the power of 3
print_result_and_type(2 ** 3)

# int division rounded down
print_result_and_type(2 // 4)
print_result_and_type(5 // 4)

# modulo (remainder after division
print_result_and_type(5 % 4)
print_result_and_type(6 % 4)
print_result_and_type(1 % 6)

# math functions
print_result_and_type(round(3.1, 0))
print_result_and_type(round(3.1, 1))

print_result_and_type(abs(-20.25))

# advance topic: complex numbers
complex

# numbers are stored as binary
print(bin(5))
# convert base 2 binary string to number
print(int('0b101', 2))
