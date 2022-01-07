# Find the largest prime factor of 60085145143 

from math import sqrt
number = 600851475143

allPrimes = []

i = 3
ifPrime = True
while i < sqrt(number):
    j = 2
    while j < sqrt(i):
        if not i % j:
            ifPrime = False
            break
        j += 1
    if ifPrime:
        allPrimes.append(i)
    ifPrime = True
    i += 2

primeFactors = []

for x in allPrimes:
    if not number % x:
        primeFactors.append(x)

print(max(primeFactors))