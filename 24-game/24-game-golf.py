from itertools import combinations_with_replacement as p,permutations as q,product as r
def j(n):
	for a,b,c,d in q(n):
		for e,f,g in r([lambda a,b:a+b,lambda a,b:a-b,lambda a,b:a*b,lambda a,b:b==0 or a/b],repeat=3):
			if any((abs(x-24)<1e-6) for x in [g(f(e(a,b),c),d),g(e(a,b),f(c,d)),g(f(a,e(b,c)),d),g(a,f(e(b,c),d)),g(a,f(b,e(c,d)))]):print(*n);return
for i in p(range(1,14),4):j(i)