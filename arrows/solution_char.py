import sys
x=y=0
for a in sys.argv[1:]:
	if a in '↙↲⇙←⇐⇦↖↰⇖':x-=1
	if a in '↘↳⇘→⇒⇨↗↱⇗':x+=1
	if a in '↖↰⇖↑⇑⇧↗↱⇗':y+=1
	if a in '↙↲⇙↓⇓⇩↘↳⇘':y-=1
	print(x,y)