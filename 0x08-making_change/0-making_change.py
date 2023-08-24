#!/usr/bin/python3

"""
makeChange module
"""

def makeChange(coins, total):
    """

    Args:
      - coins(list): list of the values of the coins in possession
      - total(int): given amount

    Returns:
      - 0 if total is 0 or less
      - -1 if totalcannot be met by any number of coins
    """
    if total <= 0:
        return 0

    coins = sorted(coins, reverse=True)
    fewest_number = int(total / coins[0])
    fn = fewest_number
    remain = total - fewest_number * coins[0]
    idx = 0

    for i in range(1, len(coins)):
        fewest_number = int(remain / coins[i])
        idx = i
        if fewest_number == 0:
            pass
        remain = remain - fewest_number * coins[i]
        fn = fn + fewest_number
        if remain == 0:
            return fn

    if remain in coins:
        return fn + 1
    return -1
