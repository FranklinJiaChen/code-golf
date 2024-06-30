for n in range(1,1001):
	c=0
	while n!=1:n=[n//2,3*n+1][n%2];c+=1
	print(c)