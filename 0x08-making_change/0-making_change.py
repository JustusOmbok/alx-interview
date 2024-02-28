#!/usr/bin/python3
"""
Module for making change
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0

    # Create a list store the for each amount up to total
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Loop through each coin value
    for coin in coins:
        # Update dp[i] coin reduces the number of coins needed
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] cannot be met by any number of coins
    return dp[total] if dp[total] != float('inf') else -1
