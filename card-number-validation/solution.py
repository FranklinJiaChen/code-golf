import sys
for a in sys.argv[1:]:b=a.replace(" ","");(sum(int(i)for i in b[1::2])+sum(2*(int(i)%5)+(int(i)>4)for i in b[::2]))%10<1==print(a)