i=2
while i<13e6:
	s=str(i)
	if "".join(sorted(set(s)))==s and all(i%j for j in range(3,i)):print(i)
	i+=i%2+1
print(23456789)