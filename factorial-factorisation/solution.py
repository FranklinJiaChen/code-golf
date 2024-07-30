d={}
for i in range(1001):
    j = 2
    while i>1:
        if i%j<1:
            i//=j
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        else:
            j+=1

s = ""
for key, value in d.items():
    s+=[f"{key}*",f"{key}^{value}*"][value>1]
print(s[:-1])