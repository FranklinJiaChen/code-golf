import sys
for arg in sys.argv[1:]:
	for i in range((len(arg)-1)//16+1):
		s=('0'*7+hex(i*16)[2:])[-8:]+': '
		n=0
		for c in arg[i*16:(i+1)*16]:
			h=hex(ord(c))[2:]
			if c == '\n':h='0a'
			s+=h
			if n%2:s+=' '
			n+=1
		print(s+' '*(51-len(s))+arg[i*16:(i+1)*16].replace('\n','.'))
	print()