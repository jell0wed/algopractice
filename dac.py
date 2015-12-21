import math
#
# Divide-and-conquer strategy problems
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

# By looking at consecutive pairs of elements, we consider the following pair of numbers (left, right).
# For every pair or numbers,
# - left == right iff the unique element hasn't been checked yet
# - left != right iff the unique element has been checked at some point
#   * either in the past sequence
#   * or the unique element is in either left or right
#
# So, clearly we can do better than O(n).
# Using a divide and conquer strategy:
#   Look at the pair made of the middle element + its consecutive neighbour
#
# If both are equal, from previous observation, we know that the unique element hasn't been checked yet.
#   Hence, the consecutive element can't be on the [0..mid+1] elements subarray
#   Recursive call on the second half of the array.
# If both are not equal, thus the unique element is either part of that specific pair or its part of the
#   [0..mid+1] subarray (dont forget to include that pair).as
#   Recursive call on the first half of the array.

def unique_duplicate(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        mid = int(math.trunc(len(nums) / 2))
        if nums[mid - 1] == nums[mid]:
            return unique_duplicate(nums[mid+1:len(nums)])

        return unique_duplicate(nums[0:mid+1])
print unique_duplicate([1,1,2,3,3,4,4,5,5,6,6])

# Analysis:
# The above algorithms yields the following recurrence relation :
# T(0) = \thetha(1)
# T(n) < T(n/2) + O(1)*
#
# It is solvable by the master theorem, having a=1, k=0
# Case 2 : f(n) is \thetha(n^{log_b a}*log^k n)
# hence T(N) is O(n^{log_2 1}*log^{k+1} n) is O(log n)
#

