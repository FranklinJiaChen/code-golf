for n in range(1001):
	r=int(str(n)[::-1])
	if n!=r and all([n%i for i in range(2,n)]+[r%i for i in range(2,r)]):print(n)