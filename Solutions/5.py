# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 
def is_divisible(input):
    i = 20
    while i > 1:
        if input % i != 0:
            return False
        i -= 1
    return True

i = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

while is_divisible(i) == False:
    i += 1
print(i)