t=[]
for i in range(9):
	t=[' '+x for x in t+['*'*(2*i+1)]];
	if i>1:*map(print,t+[t[0]+'\n']),