"""
The 24 game is an arithmetical puzzle in which the objective is to find a way to combine four integers using only basic arithmetic operations (+, -, ×, ÷) to get a result of 24. Each integer must be used exactly once.

The variation we use is played with a standard 52-card deck, with integers ranging from 1 to 13. Print all solvable quadruples of integers. The integers of each quadruple should be printed in non-decreasing order.

Keep in mind that some solutions involve fractions. For example, the only solution to 1 3 4 6 is 6/(1-3/4).
"""

from itertools import combinations_with_replacement, permutations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 1e9
    return a / b

# Tolerance for floating-point comparison
EPSILON = 1e-6

# Check if the result is close enough to 24
def is_close_to_24(value):
    return abs(value - 24) < EPSILON

def print_if_solve24(num1, num2, num3, num4):
    # using +, -, /, * => 4^3 = 64 possibilities left to right
    for a, b, c, d in permutations([num1, num2, num3, num4]):
        for op1 in [add, subtract, multiply, divide]:
            for op2 in [add, subtract, multiply, divide]:
                for op3 in [add, subtract, multiply, divide]:
                    # ((a?b)?c)?d
                    if is_close_to_24(op3(op2(op1(a, b), c), d)):
                        print(num1, num2, num3, num4)
                        return
                    # (a?b)?(c?d)
                    if is_close_to_24(op3(op1(a, b), op2(c, d))):
                        print(num1, num2, num3, num4)
                        return
                    # (a?(b?c))?d
                    if is_close_to_24(op3(op2(a, op1(b, c)), d)):
                        print(num1, num2, num3, num4)
                        return
                    # a?((b?c)?d)
                    if is_close_to_24(op3(a, op2(op1(b, c), d))):
                        print(num1, num2, num3, num4)
                        return
                    # a?(b?(c?d))
                    if is_close_to_24(op3(a, op2(b, op1(c, d)))):
                        print(num1, num2, num3, num4)
                        return

possible_combinations = combinations_with_replacement(range(1, 14), 4)

for comb in possible_combinations:
    print_if_solve24(*comb)
