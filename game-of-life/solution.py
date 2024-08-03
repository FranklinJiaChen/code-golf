import sys
i=sys.argv[1].replace("\n","")
o=""
for c in range(1024):k=(c>32and i[c-33]<'$')+(c>31and i[c-32]<'$')+(c>30and i[c-31]<'$')+(c>0and i[c-1]<'$')+(c<1023and i[c+1]<'$')+(c<993and i[c+31]<'$')+(c<992and i[c+32]<'$')+(c<991and i[c+33]<'$');o+=[".","#"][i[c]<'$'and k==2or k==3]+'\n'*(-~c%32<1)
print(o)