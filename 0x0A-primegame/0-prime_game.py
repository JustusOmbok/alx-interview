#!/usr/bin/python3
"""Module for prime numbers game.
"""


def is_prime(num):
    """Determines if number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """Gets prime numbers."""
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """Determines the winner."""
    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = get_primes(n)
        if len(primes) % 2 == 0:
            winners["Ben"] += 1
        else:
            winners["Maria"] += 1

    max_wins = max(winners.values())
    if max_wins == 0:
        return None
    else:
        return max(winners, key=winners.get)
