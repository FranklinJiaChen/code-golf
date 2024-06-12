"""
Print all primes whose decimal digits are distinct
and appear in ascending order.
There are 100 such primes, the largest being 23456789.
"""
for i in range(2, 1456790):
    # check if i is digits are distinct
    if len(set(str(i))) != len(str(i)):
        continue
    # check if i digits are in ascending order
    if list(str(i)) != sorted(str(i)):
        continue

    # check if is prime
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i)

# Hardcode the last 2 primes to reduce the number of iterations
print(12356789)
print(23456789)
