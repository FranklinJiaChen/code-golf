import sys
R=range
for A in sys.argv[1:]:a,b,c,d,x,y,w,z=map(int,A.split(' '));print(len({(x+i,y+j)for i in R(w)for j in R(z)}.intersection({(a+i,b+j)for i in R(c)for j in R(d)})))