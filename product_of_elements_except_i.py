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


numbers = [random.randint(1, 10) for x in range(1, 6)]
print(numbers)
print(product_array())
