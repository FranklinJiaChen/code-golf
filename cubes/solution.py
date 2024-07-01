s,o,h,v,d=' ','█','─','│','╱'
for n in range(1, 8):
	a=s*(n*4);print(s*(n+1)+o+h*(n*4)+o);b=v+a+v
	for i in range(n):print(s*(n-i)+d+a+d+" "*i+v)
	print(o+h*(n*4)+o+(s*n)+v)
	for _ in range(n-1):print(b+s*n+v)
	print(b+s*n+o)
	for i in range(n):print(b+s*(n-i-1)+d)
	print(o+h*(n*4)+o+'\n')