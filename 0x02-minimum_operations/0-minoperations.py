#!/usr/bin/python3
"""Module for task min operations
"""


def minOperations(n):
    """
    Generates the min number of operations required to write n chars.
    """
    if n <= 0:
        return 0

    # Initialize the result
    result = 0

    # Find prime factorization and sum up the factors
    for i in range(2, n + 1):
        while n % i == 0:
            result += i
            n //= i

    return result
