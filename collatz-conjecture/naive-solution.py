"""
The Collatz conjecture states that, for any positive integer n, it will eventually reach 1 by repeatedly applying the following procedure:

If n is even, divide it by 2.
If n is odd, multiply by 3 and then add 1.
The number of steps needed for n to reach 1 is called its stopping time. For example, the stopping time of 10 is six:

10 → 5 → 16 → 8 → 4 → 2 → 1

Print the stopping times of all the numbers from 1 to 1,000 inclusive, each on their own line.
"""

for n in range(1, 1001):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    print(steps)