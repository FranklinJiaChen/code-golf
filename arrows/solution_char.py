import sys
x=y=0
for a in sys.argv[1:]:x+=(a in '↘↳⇘→⇒⇨↗↱⇗')-(a in '↙↲⇙←⇐⇦↖↰⇖');y+=(a in '↖↰⇖↑⇑⇧↗↱⇗')-(a in '↙↲⇙↓⇓⇩↘↳⇘');print(x,y)