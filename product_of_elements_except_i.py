# Given an array of integers, return a new array such that each element at index i of the new array is the product of
# all the numbers in the original array except the one at i.

# [1,2,3,4,5]
# [120, 60, 40, 30, 24]

import random
import math


def product_array():
    product = math.prod(numbers)
    lst = []
    return [math.floor(product / x) for x in numbers]


def product_array_2():
    prefix_pdts = []
    suffix_pdts = []
    for num in numbers:
        if prefix_pdts:
            prefix_pdts.append(num * prefix_pdts[-1])
        else:
            prefix_pdts.append(num)
    for num in reversed(numbers):
        if suffix_pdts:
            suffix_pdts.append(num * suffix_pdts[-1])
        else:
            suffix_pdts.append(num)
    suffix_pdts = list(reversed(suffix_pdts))
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(suffix_pdts[i + 1])
        elif i == len(numbers) - 1:
            result.append(prefix_pdts[i - 1])
        else:
            result.append(prefix_pdts[i - 1] + suffix_pdts[i + 1])


numbers = [random.randint(1, 10) for x in range(1, 6)]
print(numbers)
print(product_array())
print(product_array_2())

