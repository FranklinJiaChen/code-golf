import sys
x=y=0
d='↙↖←↲↰⇐⇙⇖⇦↘↗→↳↱⇒⇘⇗⇨'
for a in sys.argv[1:]:
	if a in d[:9]:x-=1
	if a in d[9:]:x+=1
	if a in d[1::3]+'↑⇑⇧':y+=1
	if a in d[::3]+'↓⇓⇩':y-=1
	print(x,y)