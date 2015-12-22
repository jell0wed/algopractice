__author__ = 'jeremiep'

# Knapsack problem
# You're given a list of items that you want to bring into your backpack
# each items has the following attributes :
#   - size s_i
#   - value v_i
# You have a knapsack of total size S
# You want to maximize the sum of values for a subset of items of total size <= S
#
# 1) Subproblems : those will be the suffixes of items up i \in integers & remaining capacity X
# 2) Guessing : is item i in the subset or not? 2 choices.
#
# 3) We can establish the following DP recurrence :
#    DP(i, X) = max( DP(i+1, X) ,
#                    DP(i+1, X-s_i) + v_i )
#
#   We consider suffixes of items with the remaining capacity of the knapsack. We're either:
#   - not including it: in this case we simply lookup the next item with the same rem. capacity
#   - include it: look at next item and decrease current rem. capacity, add value of the item
#
# subproblems : there are say n items to consider \theta(n*S)
# spend O(1) evaluating DP(i, X)
# pseudopoly-time : \theta(n*S) (in terms of n as input size & S as a value)
#

# Naive recursive implementation
def knapsack(items, max_size, rem_capacity):
    if len(items) == 0:
        return 0

    item = items[0]
    if item[1] > rem_capacity:  # obviously we can't fit it, pass to next one
        return knapsack(items[1:], max_size, rem_capacity)

    value_without_x = knapsack(items[1:], max_size, rem_capacity)
    value_with_x = knapsack(items[1:], max_size, (rem_capacity - item[1])) + item[0]
    return max(value_without_x, value_with_x)

max_size = 5
items = [(1,1), (2,2), (1,3), (2, 4)]
print knapsack(items, 5, max_size)

# Memoized recursive version

# memo[i][x]
#TODO : not working; Fix this later
memo = [[-1 for x in range(0, max_size)] for i in range(0, len(items))]
def knapsack_memo(items, i, X):
    if i >= len(items):
        return 0

    if memo[i][X - 1] > -1:
        return memo[i][X - 1]
    else:
        if items[i][1] > X:
            memo[i][X - 1] = 0
        else:
            knapsack_without_i = knapsack_memo(items, i+1, X)
            knapsack_with_i = knapsack_memo(items, i+1, X - items[i][1]) + items[i][0]

            memo[i][X - 1] = max(knapsack_without_i, knapsack_with_i)
        return memo[i][X - 1]

print knapsack_memo(items, 0, max_size)
print "finished"







