__author__ = 'jeremiep'

# Give a greedy way to make change for a specified amount of money
# Greedy solution : always choose to give the largest coin possible, when possible.
# This guarantees the global solution to be optimal.
#

def make_change(amount, coins = []):
    if coins == []:
        return []

    first_coin = coins[0]
    if amount > first_coin:
        other_coins = [first_coin]
        other_coins.extend(make_change(amount - first_coin, coins))
        return other_coins
    elif abs(amount - first_coin) <= 10e-9:
        return [first_coin]
    else: # amount < first_coin
        return make_change(amount, coins[1:])
#
# Iterative version
#
def make_change_iter(amount, coins = []):
    result = []
    while (len(coins) > 0) and not(abs(amount - 0) <= 10e-9):
        first_coin = coins[0]
        if amount > first_coin:
            result.extend([first_coin])
            amount -= first_coin
        elif abs(amount - first_coin) <= 10e-9:
            amount = 0
            result.extend([first_coin])
        else:
            coins = coins[1:]
    return result


print make_change_iter(2.35, [1.00, 0.25, 0.10, 0.05])

