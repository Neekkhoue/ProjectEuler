# Find the sum of all the even numbers in the Fibonacci series not exceeding 4,000,000
i = 1
j = 1
k = i + j
_sum = 0

while k <= 4000000:
    if not k % 2:
        _sum += k
    i = j
    j = k
    k = i + j

print(_sum)
# 4613732
