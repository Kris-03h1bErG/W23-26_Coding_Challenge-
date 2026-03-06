# copy this: python3 coding_challenge.py
# Project Euler Problem #46
# Goldbach Conjecture
# Find the smallest odd composite that is not the sum of a prime and twice a square

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

def squares(start, stop):
    s_list = []
    for i in range(start, stop):
        s_list.append(i)
    return s_list

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

def goldbachs_conjecture_checker(start = 5000, stop = 6000):
    for composite in odd_composite_generator(start, stop):
        counter = 0
        print(composite)
        for prime in prime_generator(1, stop):
            for square in squares(1, 100):
                if prime + 2 * square**2 == composite:
                    counter += 1
                    print(counter)
                    continue
    if counter == 0:
        return composite

print(goldbachs_conjecture_checker())
            
# If you could revise this to make it less brute-forcey, what would you do?

# Add more logic to start and stop to avoid wasting time on equations that obviously won't solve the equation. (Like when the square is large enough to be bigger than the composite when squared)







