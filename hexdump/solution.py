import sys
for a in sys.argv[1:]:
	i=0
	while p:=a[:16]:
		a=a[16:];s=('0'*7+'%x: '%i)[-10:]
		for c in p:s+=len(s)%5//4*' '+['%x'%ord(c),'0a'][c=='\n']
		print(s+' '*(51-len(s))+p.replace('\n','.'));i+=16
	print()