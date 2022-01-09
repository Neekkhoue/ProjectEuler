# Find abc where a^2 + b^2 = c^2 and a + b + c = 1000.
from math import sqrt

def pythTriple(a):
    for b in range(1,500):
        c = sqrt(a**2 + b**2)
        if a + b + c == 1000:
            return [a, b, c]
    return False

for x in range(1,1000):
    if pythTriple(x):
        print(int(pythTriple(x)[0] * pythTriple(x)[1] * pythTriple(x)[2]))
        break
# 31875000