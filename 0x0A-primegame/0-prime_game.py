#!/usr/bin/python3
''' module for prime game'''

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [num for num in range(2, n+1) if is_prime(num)]
        prime_count = len(primes)

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
