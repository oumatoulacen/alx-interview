#!/usr/bin/python3
''' Making Change '''

def makeChange(coins, total):
    ''' Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    '''
    if total <= 0:
        return 0
    if not coins or min(coins) > total:
        return -1
    coins.sort(reverse=True)
    n_coins = 0
    for coin in coins:
        if total <= 0:
            break
        n_coins += total // coin
        total %= coin
    return n_coins if total == 0 else -1
