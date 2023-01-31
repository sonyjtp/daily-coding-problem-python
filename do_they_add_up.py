import random
from bisect import bisect_left


# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def is_num_in_numbers(k, nums):
    matches = []
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                matches.append(f"[{i},{j}]:({nums[i]},{nums[j]})")
    return matches


# O(n^2) - dcp
def is_num_in_numbers_2(k, lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
    return False


# O(n)
def is_num_in_numbers_3(k, lst):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False


def is_num_in_numbers_4(k, lst):
    lst.sort()

    for i in range(len(lst)):
        target = k - lst[i]
        j = binary_search(lst, target)

        # Check that binary search found the target and that it's not in the same index
        # as i. If it is in the same index, we can check lst[i + 1] and lst[i - 1] to see
        #  if there's another number that's the same value as lst[i].
        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(lst) and lst[j + 1] == target:
            return True
        elif j - 1 >= 0 and lst[j - 1] == target:
            return True
    return False


def binary_search(lst, target):
    lo = 0
    hi = len(lst)
    ind = bisect_left(lst, target, lo, hi)

    if 0 <= ind < hi and lst[ind] == target:
        return ind
    return -1


numbers = [random.randint(1, 8) for x in range(1, 10)]
print(numbers)
print(f"Matches: {is_num_in_numbers(int(input()), numbers)}")
