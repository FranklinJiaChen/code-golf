list = []

for d in range(1, 51):
	for n in range(d+1):
		num_list = [num for (num, _) in list]
		if n/d not in num_list:
			list.append((n/d, str(n) + '/' + str(d)))

list.sort()

for i in list:
	print(i[1])
