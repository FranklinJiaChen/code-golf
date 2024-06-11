n=1
while n<10e3:a=[i for i in range(1,n+1) if n%i<1];sum(a)%len(a)<1and print(n);n+=1