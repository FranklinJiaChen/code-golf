l=[]
for d in range(1,51):
	for n in range(d+1):
		if n/d not in[n for(n,_)in l]:l+=[(n/d,str(n)+'/'+str(d))]
l.sort()
for i in l:print(i[1])