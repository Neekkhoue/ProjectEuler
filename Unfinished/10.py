# Find the sum of all the primes below two million.
from math import sqrt

def isPrime(x):
    for i in range(3, int(sqrt(x))+ 1):
        if not x % i:
            return False 
    return True

primesSum = 0

for x in range(1, 2000001, 2):
    if isPrime(x):
        primesSum += x

print(primesSum)
# 142913828922