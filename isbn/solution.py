import sys
for a in sys.argv[1:]:
	i=1;s=0
	for c in a.replace("-",""):s+=int(c)*i;i+=1
	print(f"{a}{[s%11,"X"][s%11//10]}")