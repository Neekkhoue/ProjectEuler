# What is the 10,001st prime number?
from math import sqrt

def is_prime(input):

    # upper_limit = 0
    # while upper_limit < sqrt(input):
    #     upper_limit += 1

    for x in range(3, input):
        if input % x == 0:
            return False

    return True

i = 1
primes = []
while len(primes) < 10002:
    if is_prime(i):
        print(i)
        primes.append(i)
        i += 2
print(primes[10001])