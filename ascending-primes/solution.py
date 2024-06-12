i=2
while i<2e6:
	if len(set(str(i)))==len(str(i))and list(str(i))==sorted(str(i))and(len([j for j in range(2, i-1)if i%j<1])<1):print(i)
	i+=1
print(12356789)
print(23456789)