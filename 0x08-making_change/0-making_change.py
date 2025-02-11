#!/usr/bin/python3
""" using greedy algorithm to get minimum coin required to make change"""


def makeChange(coins, total):
    """the greedy algorithm"""
    if total <= 0:
        return 0
    numCoins = 0
    sortedCoins = sorted(coins, reverse=True)

    for coin in sortedCoins:
        if total == 0:
            break
        numCoins += total // coin
        total = total % coin
    if total == 0:
        return numCoins
    else:
        return -1
