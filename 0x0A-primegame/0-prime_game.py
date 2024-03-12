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


def sieve_with_tracking(n):
    """Gets prime numbers."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    trackers = [None] * (n + 1)

    for num in range(2, int(n**0.5) + 1):
        if primes[num]:
            for multiple in range(num * num, n + 1, num):
                primes[multiple] = False
                if trackers[multiple] is None:
                    trackers[multiple] = "Maria"

    for num in range(2, n + 1):
        if primes[num] and trackers[num] is None:
            trackers[num] = "Ben"

    return trackers


def isWinner(x, nums):
    """Gets the winner."""
    winners = {"Maria": 0, "Ben": 0}

    for n in nums:
        trackers = sieve_with_tracking(n)
        num_remaining = sum(1 for player in trackers[2:] if player == "Maria")

        if num_remaining % 2 == 0:
            winners["Ben"] += 1
        else:
            winners["Maria"] += 1

    max_wins = max(winners.values())
    if max_wins == 0:
        return None
    else:
        return max(winners, key=winners.get)
