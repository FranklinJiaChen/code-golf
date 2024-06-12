i=3
print(2)
while i<24e6:
	if len(set(str(i)))==len(str(i))and list(str(i))==sorted(str(i))and(len([j for j in range(2,int(i**0.5)+1)if i%j<1])<1):print(i)
	i+=2