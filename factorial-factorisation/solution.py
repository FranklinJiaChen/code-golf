dict = {}

for i in range(1, 1001):
    j = 2
    while i != 1:
        if i % j == 0:
            i //= j
            if j in dict:
                dict[j] += 1
            else:
                dict[j] = 1
        else:
            j+=1

s = ""
for key, value in dict.items():
    s += f"{key}^{value}*"

print(s[:-1])
