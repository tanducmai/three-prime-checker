#
# File:         main.py
# Author:       Tan Duc Mai
# Email:        tan.duc.work@gmail.com
# Date:         12/8/2021
# Description:  Three different functions to check if a number is prime.
#   I hereby declare that I completed this work without any improper help
#   from a third party and without using any aids other than those cited.
#

"""
Three different functions to check whether a given number is a prime.
Return True if it is a prime, False otherwise.
Those three functions, from a to c, decrease in efficiency (take longer time).
"""

from math import sqrt


def is_prime_a(n):
    if n < 2:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True


def is_prime_b(n):
    if n > 1:
        if n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True
    return False


def is_prime_c(n):
    divisible = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisible += 1
    if divisible == 2:
        return True
    return False

def prime_lessthan(function):
    result = []
    for i in range(2, 10000):
        if function(i):
            result.append(i)
    print(
        f'In a list of all prime numbers less than 10000:\n'
        f'The first ten are: {result[0:10]}\n'
        f'The last ten are: {result[-10:]}'
    )
