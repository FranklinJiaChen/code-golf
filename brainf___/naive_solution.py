import sys
for a in sys.argv[1:]:
	t=[0]*99;h=p=0;l=[]
	while p<len(a):
		c=a[p];print(chr(t[h])*(c=='.'),end='');t[h]+=c=='+';t[h]-=c=='-';h+=c=='<';h-=c=='>'
		if c=='[':
			if t[h]<1:
				b=1
				while b:p+=1;b+=a[p]=='[';b-=a[p]==']'
			else:l+=[p]
		if c==']':
			if t[h]:*_,p=l
			else:*l,_=l
		p+=1