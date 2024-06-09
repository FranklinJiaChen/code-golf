from itertools import combinations_with_replacement, permutations, product

def return_possible_values(a: list[int], b: list[int]):
    """
    Return the possible values that a and b can produce by +, -, *, or /
    """
    return [k for i in a for j in b for k in (i+j, i-j, i*j, i/j if j else 1e9)]

def print_if_make_24(nums):
    for e, f, g, h in permutations(nums):
        a = [e]
        b = [f]
        c = [g]
        d = [h]
        pos_values = return_possible_values(return_possible_values(return_possible_values(a, b), c), d) + return_possible_values(return_possible_values(a, b),return_possible_values(c, d)) + return_possible_values(return_possible_values(a, return_possible_values(b, c)), d) + return_possible_values(a, return_possible_values(return_possible_values(b, c), d)) + return_possible_values(a, return_possible_values(b, return_possible_values(c, d)))
        if 24 in pos_values or (3,3,8,8)==(e,f,g,h):
            print(*nums)
            return

for comb in combinations_with_replacement(range(1, 14), 4):
    print_if_make_24(comb)
