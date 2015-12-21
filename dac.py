import math

#
# You are given a sorted array of numbers where every value except one appears exactly
# twice; the remaining value appears only once. Design an efficient algorithm
# for finding which value appears only once.
#
# Here are some example inputs to the problem:
# 1 1 2 2 3 4 4 5 5 6 6 7 7 8 8
# 10 10 17 17 18 18 19 19 21 21 23
# 1 3 3 5 5 7 7 8 8 9 9 10 10
# Clearly, this problem can be solved in O(n) time, where n is the number of elements in the array,
# by just scanning across the elements of the array one at a time and looking for one that isn't paired
# with the next or previous array element. But can we do better?

def unique_duplicate(nums):
    if len(nums) == 1:
        result = set()
        result.update(nums)
        return result
    else:
        mid = int(math.ceil(len(nums) / 2))
        left = nums[0:mid]
        right = nums[(mid):len(nums)]

        left = unique_duplicate(left)
        right = unique_duplicate(right)

        intruder = left.symmetric_difference(right)

        return intruder

print unique_duplicate([10, 10, 17, 17, 18, 18, 19, 19, 21, 21, 23])
