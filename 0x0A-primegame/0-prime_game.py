#!/usr/bin/python3
"""finding winner of a game"""


def isWinner(x, nums):
    """primegame"""
    def count_primes(n):
        if n <= 1:
            return 0
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False
        count = 0
        for i in range(2, n + 1):
            if primes[i]:
                count += 1
        return count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_n = count_primes(n)
        if primes_in_n % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
