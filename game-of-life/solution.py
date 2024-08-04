import sys
i=sys.argv[1].replace('\n','');o=''
for c in range(1024):k=sum(i[c+j]<'$'for j in(33,32,31,1,-1,-31,-32,-33)if c+j<999);o+='.#'[1+(i[c]>'-')<k<4]+c%32//31*'\n'
print(o)