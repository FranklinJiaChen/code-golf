for i in range(201):
	k=i;exec('s=0;s+=sum([int(d)**2for d in str(k)]);k=s;'*5);0<k<2==print(i)