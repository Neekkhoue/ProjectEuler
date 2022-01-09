# Find the largest palindrome that is the product of two 3-digit numbers
factor1 = list(range(100,1000))
factor2 = list(range(100,1000))
palindrome = 0

def isPalindrome(number):
    return str(number) == str(number)[::-1]

for x in factor1:
    for y in factor2:
        product = x * y
        if isPalindrome(product) and product > palindrome:
            palindrome = product

print(palindrome)
# 906609
