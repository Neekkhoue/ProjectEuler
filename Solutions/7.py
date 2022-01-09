# What is the 10,001st prime number?
from math import sqrt

def isPrime(x):
    for i in range(2, int(sqrt(x))+ 1):
        if not x % i:
            return False 
    return True

i = 1
j = 0
while j < 10001:
    i += 1  
    if isPrime(i):
        j += 1

print(i)
# 104743
