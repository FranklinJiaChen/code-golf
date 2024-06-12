i=2
while i<24e6:
	s=str(i)
	if "".join(sorted(set(s)))==s and all(i%j for j in range(3,int(i**0.7))):print(i)
	i+=i%2+1