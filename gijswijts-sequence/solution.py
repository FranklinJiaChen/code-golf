s='1';z=1
while z-1e3:
	n=2
	for i in range(1,z):
		while i*n<z+1 and s.endswith(s[-i:]*n):n+=1
	s+=str(~-n);z=len(s)
for c in s:print(c)