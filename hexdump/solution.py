import sys
for a in sys.argv[1:]:
	for i in range(~-len(a)//16+1):
		s=('0'*7+'%x: '%(i*16))[-10:];p=a[i*16:-~i*16]
		for c in p:s+=len(s)%5//4*' '+['%x'%ord(c),'0a'][c=='\n']
		print(s+' '*(51-len(s))+p.replace('\n','.'))
	print()