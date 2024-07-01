import sys,datetime as d
for a in sys.argv[1:]:print(d.datetime.strptime(a,'%Y-%m-%d').strftime('%A'))