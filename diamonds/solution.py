for i in range(9):
	for j in range(2*i+1):print(str(int('1'*[j+1,2*i-j+1][j>i])**2).center(19))
	print()