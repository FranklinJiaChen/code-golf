f=range
for n in f(992):
	r=int(str(n)[::-1])
	if all([n!=r]+[n%i for i in f(2,n)]+[r%i for i in f(2,r)]):print(n)