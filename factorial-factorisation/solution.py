s=""
for i in range(2,998):
	f=0;n=1000
	if all(i%j for j in range(2,i)):
		while n:f+=(n:=n//i)
		s+=[f"{i}*",f"{i}^{f}*"][f>1]
print(s[:-1])