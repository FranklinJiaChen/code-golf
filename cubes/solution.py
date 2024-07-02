s,o,h,v,d,r,p=' ','█','─','│','╱',range,print
for n in r(1,8):
	a=s*(n*4);b,c=v+a+v,o+h*(n*4)+o;p(s*(n+1)+c)
	for i in r(3*n):p([s*(n-i)+d+a+d+" "*i+v,(c+s*n+v+'\n')*(i==n)+b+s*n+[v,o][i>2*n-2],b+s*(3*n-i-1)+d][i//n])
	p(c);p()