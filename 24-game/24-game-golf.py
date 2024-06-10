from itertools import*
h=lambda a,b:[k for i in a for j in b for k in(i+j,i-j,i*j,j and i/j)]
for i in combinations_with_replacement(range(1,14),4):
 for e,f,g,z in permutations(i):
  a,b,c,d=[e],[f],[g],[z]
  if 24 in h(h(h(a,b),c),d)+h(h(a,b),h(c,d))+h(a,h(h(b,c),d))+h(a,h(b,h(c,d)))or e**f+g*z==6585:print(*i);break