import random


# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def is_num_in_numbers(k, nums):
    matches = []
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                matches.append(f"[{i},{j}]:({nums[i]},{nums[j]})")
    return matches


def is_num_in_numbers_2(k, lst):  # dcp solution
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
    return False


numbers = [random.randint(1, 8) for x in range(1, 10)]
print(numbers)
print(f"Matches: {is_num_in_numbers(int(input()), numbers)}")

