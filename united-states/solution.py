import sys
for a in sys.argv[1:]:
	s = ''.join(c for c in a if c.isupper()or c=='z')
	if a[0]=='T':s+=a[2]
	if a[0]in'CVGHP'or'Io'<a<'Mas':s+=a[-1]
	if('Mid'<a<'New'or a=='Alaska')and a!='Nebraska':
		for i in a[4::-1]:
			if'i'<i:s+=i;break
	if len(s)<2:s+=a[1]
	print(s.upper())