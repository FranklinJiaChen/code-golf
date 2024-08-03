import sys
i=sys.argv[1].replace("\n","")
o=""
for c in range(1024):
	k=''
	for j in [33,32,31,1,-1,-31,-32,-33]:
		try:k+=i[c+j]
		except:1
	k=k.count('#');o+=[".","#"][i[c]<'$'and k==2or k==3]+'\n'*(-~c%32<1)
print(o)