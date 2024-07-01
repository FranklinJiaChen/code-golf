s,o,h,v,d,r,p=' ','█','─','│','╱',range,print
for n in r(1,8):
	a=s*(n*4);p(s*(n+1)+o+h*(n*4)+o);b=v+a+v
	for i in r(n):p(s*(n-i)+d+a+d+" "*i+v)
	p(o+h*(n*4)+o+(s*n)+v)
	for i in r(n):p(b+s*n+[v,o][i+1==n])
	for i in r(n):p(b+s*(n-i-1)+d)
	p(o+h*(n*4)+o+'\n')