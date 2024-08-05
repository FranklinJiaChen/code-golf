import sys
for a in sys.argv[1:]:
	for i in range(~-len(a)//16+1):
		s=('0'*7+hex(i*16)[2:])[-8:]+': ';n=0
		for c in a[i*16:-~i*16]:s+=[hex(ord(c))[2:],'0a'][c=='\n']+' '*(n%2);n+=1
		print(s+' '*(51-len(s))+a[i*16:-~i*16].replace('\n','.'))
	print()