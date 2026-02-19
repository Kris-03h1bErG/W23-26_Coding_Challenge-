# copy this: python3 coding_challenge.py
# Project Euler Problem #46
# Goldbach Conjecture
# Find the smallest odd composite that is not the sum of a prime and twice a square
odd_composites = []
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = []

# arguments: start: int , stop:  int 
#starts at 2 normaly with no start value
def prime_generator(start = 2, stop = 10):
    primes
    for num in range(start, stop):
        counter = 0
        #print(f"dividee number {num}")
        for i in range(1, num):
            if num % i == 0:
                #print(f"passed num {num}")
                counter += 1
        if counter == 1:
            #print(f"further passed num {num}")
            primes.append(num)
    return primes


# def odd_composite_generator(start, primes, stop=6000):

print(prime_generator(2,100))


