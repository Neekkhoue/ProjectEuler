# Find the largest palindrome found from the product of two 3-digit numbers

# Create a list of all possible products of two 3-digit numbers
digits = range(0,9)
product1 = range(100,1000)
product2 = range(100,1000)
palindromes = []

for x in product1:
    for y in product2:
        product = x * y
        string_product = str(product)
        for i in digits:
            if string_product.startswith(i) and string_product.endswith(i):
                palindromes.append(product)

print(palindromes)