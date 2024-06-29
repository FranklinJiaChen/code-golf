import sys
for a in sys.argv[1:]:
	t,l=[0]*99,[];h=p=0
	while p<len(a):
		c=a[p]
		if c=='.':print(chr(t[h]),end='')
		if c=='+':t[h]=(t[h]+1)%256
		if c=='-':t[h]=(t[h]-1)%256
		if c=='>':h+=1
		if c=='<':h-=1
		if c=='[':
			if t[h]<1:
				b=1
				while b:
					p+=1
					b+=a[p]=='[';b-=a[p]==']'
			else:l.append(p)
		if c==']':
			if t[h]:p=l[-1]
			else:l.pop()
		p+=1