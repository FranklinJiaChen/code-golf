import sys
x=y=0
a='↙↖←↲↰⇐⇙⇖⇦↘↗→↳↱⇒⇘⇗⇨'
u='↑⇑⇧'
d='↓⇓⇩'
m='↔↕⇔⇕⥀⥁'

ord_list = [ord(c) for c in a+u+d+m]
ord_list.sort()
print(ord_list)