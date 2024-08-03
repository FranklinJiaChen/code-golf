import sys
i=sys.argv[1].replace("\n", "")
o=""
for c in range(1024):
	is_alive = i[c]=="#"
	k=0
	if c-33 >= 0 and i[c-33]=="#":
		k+=1
	if c-32 >= 0 and i[c-32]=="#":
		k+=1
	if c-31 >= 0 and i[c-31]=="#":
		k+=1
	if c-1 >= 0 and i[c-1]=="#":
		k+=1
	if c+1 < 1024 and i[c+1]=="#":
		k+=1
	if c+31 < 1024 and i[c+31]=="#":
		k+=1
	if c+32 < 1024 and i[c+32]=="#":
		k+=1
	if c+33 < 1024 and i[c+33]=="#":
		k+=1
	if i[c]=="#":
		if k < 2 or k > 3:
			o+="."
		else:
			o+="#"
	else:
		if k == 3:
			o+="#"
		else:
			o+="."
	if (c+1)%32==0:
		o+="\n"
print(o)