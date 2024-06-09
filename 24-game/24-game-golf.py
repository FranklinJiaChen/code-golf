from itertools import combinations_with_replacement, permutations, product

ops = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b, lambda a, b: a / b if b != 0 else 1e9]

def is_close_to_24(value):
    return abs(value - 24) < 1e-6

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

possible_combinations = combinations_with_replacement(range(1, 14), 4)

for comb in possible_combinations:
    print_if_solve24(comb)
