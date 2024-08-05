import sys
for A in sys.argv[1:]:a,b,c,d,x,y,w,z=map(int,A.split(' '));h=min(a+c,x+w)-max(a,x);v=min(b+d,y+z)-max(b,y);print(h*v*(h>0<v))