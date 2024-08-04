l=[];[l.append((n/d,f'{n}/{d}'))for d in range(1,51)for n in range(d+1)if n/d not in[n for(n,_)in l]]
for i in sorted(l):print(i[1])