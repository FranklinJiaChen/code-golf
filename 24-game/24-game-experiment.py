from itertools import combinations_with_replacement, permutations, product

def return_possible_values(a: list[int], b: list[int]):
    """
    Return the possible values that a and b can produce by +, -, *, or /
    """
    possible_values = []
    for i in a:
        for j in b:
            possible_values.append(i + j)
            possible_values.append(i - j)
            possible_values.append(i * j)
            if j != 0:
                possible_values.append(i / j)
    return possible_values

def print_if_make_24(nums):
    for a, b, c, d in permutations(nums):
        a = [a]
        b = [b]
        c = [c]
        d = [d]
        pos_values = return_possible_values(return_possible_values(return_possible_values(a, b), c), d) + return_possible_values(return_possible_values(a, b),return_possible_values(c, d)) + return_possible_values(return_possible_values(a, return_possible_values(b, c)), d) + return_possible_values(a, return_possible_values(return_possible_values(b, c), d)) + return_possible_values(a, return_possible_values(b, return_possible_values(c, d)))
        if 24 in pos_values:
            print(*nums)
            return

for comb in combinations_with_replacement(range(1, 14), 4):
    print_if_make_24(comb)
