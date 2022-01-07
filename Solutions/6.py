# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
sum_of_squares = 0
for x in range(1,101):
    sum_of_squares += x**2
print((sum(range(1,101)))**2 - sum_of_squares)