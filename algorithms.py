import math

def is_prime_iterative(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_iterative(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime_iterative(i):
            count += 1
    return count

def is_prime_recursive(n, divisor=None):
    if divisor is None:
        divisor = int(math.sqrt(n))
    if n < 2:
        return False
    if divisor < 2:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor - 1)

def count_primes_recursive(n):
    if n < 2:
        return 0
    if is_prime_recursive(n):
        return 1 + count_primes_recursive(n - 1)
    else:
        return count_primes_recursive(n - 1)
