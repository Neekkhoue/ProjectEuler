# Find the sum of all multiples of 3 or 5 below 1000

numbers = list(range(1,1000))
_sum = 0

for x in numbers:
    if not x % 5:
        _sum += x
    if (not x % 3) and x % 5:
        _sum += x

print(_sum)