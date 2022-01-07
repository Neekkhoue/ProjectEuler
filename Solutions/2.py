# Find the sum of all the number in the Fibonacci series below 4,000,000

fibonacci = [1,2]
fibSum = 2

i=2
while i <= 4000000:
    fibonacci.append(fibonacci[i-2] + fibonacci[i-1])
    if fibonacci[i] > 4000000:
        break
    if not fibonacci[i] % 2:
        fibSum += fibonacci[i]
    i += 1

print(fibSum)