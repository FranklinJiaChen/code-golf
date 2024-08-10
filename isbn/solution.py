import sys
for a in sys.argv[1:]:
	s=i=0
	for c in a:
		if c>'.':i+=1;s+=int(c)*i
	print(f"{a}{[s%11,"X"][s%11//10]}")