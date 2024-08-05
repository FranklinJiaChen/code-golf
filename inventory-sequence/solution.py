l=[n:=0]
exec("print(l[-1]);l+=[a:=l.count(n)];n+=[1,-n][a<1];"*1000)