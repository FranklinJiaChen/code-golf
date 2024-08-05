def f(n):
    s=0
    for d in str(n):
        s+=int(d)**2
    return s
for i in range(201):
    k=i
    for _ in range(9):
        k=f(k)
    if k==1:print(i)