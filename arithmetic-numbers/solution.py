for n in range(1,10000):
	l=[i for i in range(1,n+1) if n%i<1]
	a=sum(l)/len(l)
	if a//1==a:print(n)