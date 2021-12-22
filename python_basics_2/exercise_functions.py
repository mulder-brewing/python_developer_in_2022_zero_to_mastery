def highest_even(nums):
    result = 0
    for num in nums:
        if num % 2 == 0 and num > result:
            result = num
    return result


print(highest_even([10, 1, 2, 3, 4, 8, 11]))
