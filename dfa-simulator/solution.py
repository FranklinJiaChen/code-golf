import sys
for a in sys.argv[1:]:
	q=[];d={};s,*l,p=a.split("\n")
	for r,(e,f,n,*t)in enumerate(l):
		q.append({});d[n]=r;q[r]['']=['Reject','Accept'][f>'E']
		if e>'<':c=q[r];b=n
		for i,u in enumerate(t[1::2]):q[r][s.split()[i]]=u
	for j in p[1:-1]:c=q[d[b:=c[j]]]
	print(b,c[''])