s,o,h,v,d,r,p=' ','█','─','│','╱',range,print
for n in r(1,8):
	a=s*(n*4);b,c=v+a+v,o+h*(n*4)+o;p(s*(n+1)+c)
	for i in r(n):p(s*(n-i)+d+a+d+" "*i+v)
	p(c+(s*n)+v)
	for i in r(2*n):p([b+s*(2*n-i-1)+d,b+s*n+[v,o][i+1==n]][i<n])
	p(c);p()