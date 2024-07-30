s=""
for i in range(2,998):
    factors = 0
    num = 1000
    if all(i%j for j in range(2,i)):
        while num != 0:
            factors += num//i
            num //= i
        if factors > 1:
            s += f"{i}^{factors}*"
        else:
            s += f"{i}*"
print(s[:-1])
