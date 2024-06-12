import sys
x=y=0
for a in sys.argv[1:]:x+=a in'↘↳⇘→⇒⇨↗↱⇗';x-=a in'↙↲⇙←⇐⇦↖↰⇖';y+=a in'↖↰⇖↑⇑⇧↗↱⇗';y-=a in'↙↲⇙↓⇓⇩↘↳⇘';print(x,y)