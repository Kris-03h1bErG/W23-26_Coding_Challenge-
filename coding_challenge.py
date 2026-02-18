# copy this: python3 coding_challenge.py
# Project Euler Problem #46
# Goldbach Conjecture
# Find the smallest odd composite that is not the sum of a prime and twice a square
odd_composites = []
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = []

def prime_generator(start, stop=6000):
    for num in range(stop):
        for i in range(1, num):
            print(i)


# def odd_composite_generator(start, primes, stop=6000):

prime_generator(1)


