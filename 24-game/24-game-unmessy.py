from itertools import combinations_with_replacement, permutations, product

def print_if_make_24(nums):
    for a, b, c, d in permutations(nums):
        for op1, op2, op3 in product([lambda a, b: a + b,
                          lambda a, b: a - b,
                          lambda a, b: a * b,
                          lambda a, b: a / b if b != 0 else 1e9], repeat=3):
            expressions = [op3(op2(op1(a, b), c), d),
                           op3(op1(a, b), op2(c, d)),
                           op3(op2(a, op1(b, c)), d),
                           op3(a, op2(op1(b, c), d)),
                           op3(a, op2(b, op1(c, d)))]
            if any(not(round(expr - 24,1) for expr in expressions)):
                print(*nums)
                return

for comb in combinations_with_replacement(range(1, 14), 4):
    print_if_make_24(comb)
