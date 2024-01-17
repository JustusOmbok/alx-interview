#!/usr/bin/python3
"""Module for task min operations
"""


def minOperations(n):
    """
    Generates the min number of operations required to write n chars.
    """
    if n <= 0:
        return 0

    # Initialize an array to store the minimum number of operations
    dp = [float('inf')] * (n + 1)

    # Base case: 0 operations needed for 1 character
    dp[1] = 0

    # Iterate from 2 to n to fill the dp array
    for i in range(2, n + 1):
        # Try all possible factors of i
        for j in range(2, i + 1):
            if i % j == 0:
                # If j is a factor of i, update the minimum operations
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
