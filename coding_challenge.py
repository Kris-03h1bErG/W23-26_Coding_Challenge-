# copy this: python3 coding_challenge.py
# Project Euler Problem #46
# Goldbach Conjecture
# Find the smallest odd composite that is not the sum of a prime and twice a square
odd_composites_real = []
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = []

# takes a start and stop int > default of 2 int > default of 10
# returns list o' primes 
def prime_generator(start = 2, stop = 10):
    primes = []
    for num in range(start, stop):
        if num < 2:
            continue
        counter = 0
        for i in range(2, num):
            if num % i == 0:
                counter += 1
        if counter == 0:
            primes.append(num)
    return primes

# takes a start and stop int > default of 2 int > default of 10
# returns list o' composites 
def odd_composite_generator(start = 2, stop = 10):
    composites = []
    for num in range(start, stop):
        if num % 2 != 0:
            counter = 0
            for i in range(1, num + 1):
                if num % i == 0:
                    counter += 1
            if counter > 2:
                composites.append(num)
    #print(composites)
    return composites

def goldbachs_conjecture_checker(start = 5500, stop = 6000):
    for composite in odd_composite_generator(start, stop):
        counter = 0
        print(composite)
        for prime in prime_generator(start, stop):
            for square in squares:
                if prime + 2 * square**2 == composite:
                    counter += 1
                    print(counter)
                    continue
                if prime + 2 * square**2 != composite:
                    continue
                if counter == 0:
                    return composite

print(goldbachs_conjecture_checker())

            







