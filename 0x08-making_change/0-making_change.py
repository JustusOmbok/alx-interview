#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Greedy approach
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

    if total == 0:
        return count

    # Dynamic programming approach
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return min(count, dp[total]) if dp[total] != float('inf') else -1
