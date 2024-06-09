from itertools import combinations_with_replacement as p,permutations as q
h=lambda a,b:[k for i in a for j in b for k in (i+j,i-j,i*j,j==0 or i/j)]
def j(n):
	for e,f,g,z in q(n):
		a,b,c,d=[e],[f],[g],[z]
		v=h(h(h(a,b),c),d)+h(h(a,b),h(c,d))+h(h(a,h(b,c)),d)+h(a,h(h(b,c),d))+h(a,h(b,h(c,d)))
		if 24 or 8/(3-8/3) in v:print(*n);return
for i in p(range(1,14),4):j(i)