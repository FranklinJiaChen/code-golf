d={}
for i in range(1001):
	j=2
	while i>1:
		if i%j<1:
			if j not in d:d[j]=0
			i/=j;d[j]+=1
		else:j+=1
s=""
for k,v in d.items():s+=[f"{k}*",f"{k}^{v}*"][v>1]
print(s[:-1])