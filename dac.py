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



# Find a Fixed Point in a given array
# Given an array of n distinct integers sorted in ascending order, write a function that returns a
# Fixed Point in the array, if there is any Fixed Point present in array, else returns -1.
# Fixed Point in an array is an index i such that arr[i] is equal to i.
#
# Note that integers in array can be negative.
#
# We can solve this problem using the divide and conquer paradigm.
# First, look at the middle element.
#  - If it is a fixed point (==), simply return it
#  - If the value is less than the current index, a fixed point must lie (or not) on the left-hand side.
#  - If the value is greater than the current index, a fixed point must lie (or not) on the right-hand side.

def fixed_point(nums, i, j):
    if i > j:
        return -1

    mid = int(math.floor((j - i) / 2)) + i
    if nums[mid] == mid:
        return nums[mid]
    elif nums[mid] < mid:
        return fixed_point(nums, mid+1, j)
    else:
        return fixed_point(nums, 0, mid-1)

nums = [5,10,100,200,300,400]
print fixed_point(nums, 0, len(nums) - 1)

# Again, the recurrence of this algorithm can be described as follows :
# T(1) < \theta(1)
# T(n) < T(n/2) + O(1)
# as before, this algorithm is (log n)
#


# Find the number of zeroes
# Given an array of 1s and 0s which has all 1s first followed by all 0s. Find the number of 0s.
# Count the number of zeroes in the given array.
#
# We know for fact that a bunch of 1s must be followed by a bunch of 0s.
# Hence know at any given index on which side the 1s or 0s are depending on the value at that given
# index. We can recursively resolve that problem in O(logn) time again.
#
# Take any middle element n,
# - if it is equal to 1, then we know that the bunch of zeros we wish to count is on the right side.
# - if it is equal to 0:
#   - and its prior element (n-1) is 0, we are in the middle of a bunch of zeros. In order to calculate to total number
#     of zeros, we must find the last 1. As n-1 is zero, we know that the last 1 is in the left subarray.
#   - and its prior element (n-1) is 1, we are at the first 0 of the whole 0s sequence. Simply return the number of 0s.
#

def num_zeros(nums, i, j):
    if i > j:
        return 0

    mid = int(math.floor((j - i) / 2)) + i
    if nums[mid] == 1: # bunch of zeros must be on the right side
        return num_zeros(nums, mid + 1, j)
    else:
        if nums[mid - 1] == 0: # last 1s is on the left side
            return num_zeros(nums, i, mid - 1)
        else:
            return ((len(nums) - 1) - mid) + 1

nums = [1, 0, 0, 0, 0, 0]
print num_zeros(nums, 0, len(nums) - 1)

# Analysis
# T(1) < \Theta(1)
# T(n) < T(n/2) + O(1)
# O(logn)
#

# McGill COMP 251 Final 2014 - Majority Element
# You are given an array A[1..n] of integers. You would like to determine whether A
# contains a majority element, that is, an element that appears more than n/2 times in A.
#
# Use this fact and the algorithm in b) to design a divide-and-conquer algorithm for solving this
# problem.
#

# We notice that an element is a majority iff it is either a majority in the A[0..floor(n/2)] subarray or the
# A[floor(n/2)+1..n] subarray. When comparing 2 distinct element (ie. len(A) == 2) we simply
# have to decided whether the two elements form a majority or not --ie. are they the same or not?
# The base case is trivial, n = 1 should simply return the first number as a majority
#
# Consider the following example :
#
# Nice example :
# 0 1 1 1 1 1 1 1
# 0 1 1 1 |      1 1 1 1
# 0 1 || 11 |    1 1 || 1 1
# (X)    (1)     (1)    (1)
#    (1)             (1)
# yields that 1 is a majority
#

def majority(nums):
    if len(nums) == 0:
        return None

    if len(nums) == 1:
        return nums[0]
    else:
        mid = int(math.floor((len(nums) - 1) / 2))
        left = majority(nums[0:mid])
        right = majority(nums[(mid+1):(len(nums) - 1)])
        print (left, right)
        if (left,right) == (None, None):
            return None
        elif left == None:
            return right
        elif right == None:
            return left
        else:
            if left != right:
                return None
            else:
                return left
# TODO : make this working
print majority([1,0,1,0,1,0,1,0,0])





