s,o,v,d,p=' ','█','│','╱',print
for n in range(1,8):
	a=s*(n*4);c=o+'─'*4*n+o;p(s*n+s+c)
	for i in range(3*n):p([s*(n-i)+d+a+d+" "*i+v,(c+s*n+v+'\n')*(i==n)+v+a+v+s*n+[v,o][i>2*n-2],v+a+v+s*(3*n+~i)+d][i//n])
	p(c);p()