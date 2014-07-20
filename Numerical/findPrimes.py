import math


def findPrimes(max_number):
    is_composite = [False for x in range(max_number)]

    # "Cross out" multiples of 2
    for i in range(4, max_number, 2):
        is_composite[i] = True

    # "Cross out" multiples of primes found so far
    next_prime = 3
    stop_at = math.sqrt(max_number)
    while (next_prime < stop_at):
        # "Cross out" multiples of this prime
        for i in range(next_prime * 2, max_number, next_prime):
            is_composite[i] = True

        # Move to the next prime, skipping even numbers.
        next_prime = next_prime + 2
        while ((next_prime <= max_number) and is_composite[next_prime]):
            next_prime = next_prime + 2

    # Copy the primes into a list
    primes = []
    for i in range(2, max_number):
        if (not is_composite[i]):
            primes.append(i)

    return primes
