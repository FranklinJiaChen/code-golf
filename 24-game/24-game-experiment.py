from itertools import combinations_with_replacement, permutations, product

def h(a: list[int], b: list[int]):
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
        pos_values = h(h(h(a, b), c), d) + h(h(a, b),h(c, d)) + h(h(a, h(b, c)), d) + h(a, h(h(b, c), d)) + h(a, h(b, h(c, d)))
        if 24 in pos_values or (3,3,8,8)==(e,f,g,h):
            print(*nums)
            return

for comb in combinations_with_replacement(range(1, 14), 4):
    print_if_make_24(comb)

from itertools import combinations_with_replacement as p,permutations as q
h=lambda a, b:[k for i in a for j in b for k in (i+j, i-j, i*j, i/j if j else 0)];
def j(n):
	for e,f,g,z in q(n):
		a = [e]
		b = [f]
		c = [g]
		d = [z]
		pos_values = h(h(h(a,b),c),d) + h(h(a,b),h(c,d)) + h(h(a,h(b,c)),d) + h(a,h(h(b,c),d)) + h(a,h(b,h(c,d)))
		if 24 in pos_values or (3,3,8,8)==(e,f,g,z):print(*n);return
for i in p(range(1,14),4):j(i)