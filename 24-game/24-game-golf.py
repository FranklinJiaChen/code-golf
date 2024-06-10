from itertools import*
h=lambda a,b:[k for i in a for j in b for k in(i+j,i-j,i*j,j and i/j)]
def j(n):
 for e,f,g,z in permutations(n):
  a,b,c,d=[e],[f],[g],[z]
  v=h(h(h(a,b),c),d)+h(h(a,b),h(c,d))+h(a,h(h(b,c),d))+h(a,h(b,h(c,d)))
  if 24 in v or 8/(3-8/3) in v:print(*n);break
for i in combinations_with_replacement(range(1,14),4):j(i)