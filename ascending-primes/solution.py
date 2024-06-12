i=3
print(2)
while i<24e6:
	s=str(i)
	if len(set(s))==len(s)and list(s)==sorted(s)and all(i%j for j in range(2,int(i**0.7))):print(i)
	i+=2