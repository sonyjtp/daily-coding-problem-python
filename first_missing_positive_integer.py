import random


# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

def find_first_missing(nums):
    last_num = 0
    for num in nums:
        if num < 1:
            continue
        if num != 1 and last_num == 0:
            return 1
        if num - last_num > 1:
            return last_num + 1
        else:
            last_num = num
    return None


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


numbers = [random.randint(-3, 25) for x in range(1, 35)]
print(numbers)
merge_sort(numbers)
print(numbers)
print(find_first_missing(numbers))
