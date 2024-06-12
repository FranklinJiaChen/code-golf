import sys
x=y=0
d='↙↖←↲↰⇐⇙⇖⇦↘↗→↳↱⇒⇘⇗⇨'
for a in sys.argv[1:]:x-=(a in d)-2*(a in d[9:]);y+=(a in d[1::3]+'↑⇑⇧')-(a in d[::3]+'↓⇓⇩');print(x,y)