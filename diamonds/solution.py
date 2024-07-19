for i in range(9):
	for j in range(i+1):print(str(int('1'*(j+1))**2).center(19))
	for j in range(i-1,-1,-1):print(str(int('1'*(j+1))**2).center(19))
	print()