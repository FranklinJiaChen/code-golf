from itertools import permutations, product

# Define basic arithmetic operations
ops = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b, lambda a, b: a / b if b != 0 else 1e9]

# Tolerance for floating-point comparison
EPSILON = 1e-6

def is_close_to_24(value):
    return abs(value - 24) < EPSILON

def print_if_solve24(nums):
    for a, b, c, d in permutations(nums):
        for op1, op2, op3 in product(ops, repeat=3):
            if any(is_close_to_24(expr) for expr in [
                op3(op2(op1(a, b), c), d),
                op3(op1(a, b), op2(c, d)),
                op3(op2(a, op1(b, c)), d),
                op3(a, op2(op1(b, c), d)),
                op3(a, op2(b, op1(c, d)))
            ]):
                print(*nums)
                return

# Generate all possible combinations
possible_combinations = [(a, b, c, d) for a in range(1, 14) for b in range(a, 14) for c in range(b, 14) for d in range(c, 14)]

# Check each combination
for comb in possible_combinations:
    print_if_solve24(comb)
