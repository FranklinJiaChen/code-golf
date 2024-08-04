s='1'
while len(s)-1001:
	n=2;print(s[-1])
	for i in range(1,len(s)):
		while s.endswith(s[-i:]*n):n+=1
	s+=str(~-n)