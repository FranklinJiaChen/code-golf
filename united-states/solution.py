import sys
for a in sys.argv[1:]:
	s=''.join(c*(c.isupper()or c=='z') for c in a)+a[2]*(a[0]=='T')+a[-1]*(a[0]in'CVGHP'or'Io'<a<'Mas')
	for i in a[4::-1]:s+=i*(('Mid'<a<'New'or a=='Alaska')and a!='Nebraska'and'i'<i)
	print((s+a[1]).upper()[0:2])