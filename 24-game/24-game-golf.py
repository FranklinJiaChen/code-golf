from itertools import combinations_with_replacement as p,permutations as q,product as r
def j(nums):
    for a, b, c, d in q(nums):
        for e, f, g in r([lambda a,b:a+b,lambda a,b:a-b, lambda a,b:a*b, lambda a,b:a/b if b!= 0 else 1e9], repeat=3):
            if any((abs(expr-24)<1e-6) for expr in [g(f(e(a, b), c), d),g(e(a, b), f(c, d)),g(f(a, e(b, c)), d),g(a, f(e(b, c), d)),g(a, f(b, e(c, d)))]):print(*nums);return
for i in p(range(1, 14), 4):
    j(i)